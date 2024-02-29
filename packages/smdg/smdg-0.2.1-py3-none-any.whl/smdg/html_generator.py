# -*- coding: utf-8 -*-

"""

smdg.html_generator

Minimalistic HTML generation helper module

THIS MODULE IMPLEMENTS ONLY A SMALL HTML ELEMENTS SUBSET
AND IS NOT INTENDED FOR GENERAL PURPOSES.


Copyright (C) 2024 Rainer Schwarzbach

This file is part of smdg.

smdg is free software: you can redistribute it and/or modify
it under the terms of the MIT License.

smdg is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
See the LICENSE file for more details.

"""


import html

from typing import List, Union


#
# Constants
#


BLANK = " "
EMPTY = ""
LF = "\n"
DASH = "-"
UNDERLINE = "_"
INDENT = "    "


__all__ = ["Element", "BlockElement"]

#
# Classes
#


class Element:
    """HTML base element:
    <span> as generic iniline element
    """

    name = "span"
    empty = False
    collapse_contents = True
    may_contain_block_elements = False

    def __init__(self, *contents: Union[str, "Element"], **attributes) -> None:
        """Initialize element and attributes"""
        self._attributes = attributes
        if not self.may_contain_block_elements:
            for item in contents:
                if isinstance(item, BlockElement):
                    raise ValueError(
                        f"{self.__class__.__name__} instances"
                        f" (here: {self.name})"
                        " must not contain block elements"
                    )
                #
            #
        #
        self._contents = contents

    def __str__(self) -> str:
        """String representation"""
        if self.empty:
            return f"<{self.name}{self.format_attributes()} />"
        #
        return (
            f"<{self.name}{self.format_attributes()}>"
            f"{self.format_contents()}</{self.name}>"
        )

    def format_attributes(self) -> str:
        """Format the attributes"""
        attributes_list: List[str] = [EMPTY]
        for key, value in self._attributes.items():
            attr_name = key.replace(UNDERLINE, DASH)
            if value is None:
                attributes_list.append(attr_name)
            else:
                attributes_list.append(
                    f'{attr_name}="{html.escape(str(value))}"'
                )
            #
        #
        return BLANK.join(attributes_list)

    def format_contents(self) -> str:
        """Format the contents"""
        output_list: List[str] = [str(item) for item in self._contents]
        if self.collapse_contents:
            return EMPTY.join(output_list)
        #
        output_block = LF.join(output_list)
        output_list = [EMPTY]
        for line in output_block.splitlines():
            output_list.append(f"{INDENT}{line}")
        #
        output_list.append(EMPTY)
        return LF.join(output_list)


class BlockElement(Element):
    """<div> as generic block element"""

    name = "div"
    collapse_contents = False
    may_contain_block_elements = True


class Header(BlockElement):
    """<h*>"""

    name = "h*"
    collapse_contents = True
    may_contain_block_elements = False

    def __init__(
        self, level: int, *contents: Union[str, "Element"], **attributes
    ) -> None:
        """Initialize element and attributes"""
        if not 0 < level < 7:
            raise ValueError("level must be between 1 and 6")
        #
        self.name = f"h{level}"
        super().__init__(*contents, **attributes)


class Paragraph(BlockElement):
    """<p>"""

    name = "p"
    collapse_contents = True


class Table(BlockElement):
    """<table>"""

    name = "table"
    collapse_contents = False


class TableRow(BlockElement):
    """<tr>"""

    name = "tr"
    collapse_contents = False


class TableCell(Element):
    """<td>"""

    name = "td"


# vim: fileencoding=utf-8 ts=4 sts=4 sw=4 autoindent expandtab syntax=python:
