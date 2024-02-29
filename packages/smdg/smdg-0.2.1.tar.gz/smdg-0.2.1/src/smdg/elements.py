# -*- coding: utf-8 -*-

"""

smdg.elements

Markdown elements


Copyright (C) 2024 Rainer Schwarzbach

This file is part of smdg.

smdg is free software: you can redistribute it and/or modify
it under the terms of the MIT License.

smdg is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
See the LICENSE file for more details.

"""


# import logging

from typing import List, Optional, Set, Tuple, Union

# local modules

from smdg import html_generator
from smdg import strings


#
# Constants
#


ARGS_JOINER = ", "

# SafeStrinmg instances for single characters
SAFE_LF = strings.declare_as_safe(strings.LF)
SAFE_BLANK = strings.declare_as_safe(strings.BLANK)
SAFE_DOUBLE_QUOTE = strings.declare_as_safe('"')
SAFE_SINGLE_QUOTE = strings.declare_as_safe("'")
SAFE_EMPTY = strings.declare_as_safe(strings.EMPTY)
SAFE_EXCLAMATION_MARK = strings.declare_as_safe("!")
SAFE_BACKTICK = strings.declare_as_safe(strings.BACKTICK)
SAFE_UNDERLINE = strings.declare_as_safe(strings.UNDERLINE)
SAFE_ASTERISK = strings.declare_as_safe(strings.ASTERISK)
SAFE_POUND = strings.declare_as_safe(strings.POUND)
# Blockquote prefix
SAFE_BLOCKQUOTE_PREFIX = strings.declare_as_safe("> ")
# Left and Right Angle Brackets
SAFE_LAB = strings.declare_as_safe("<")
SAFE_RAB = strings.declare_as_safe(">")
# Left and Right Square Brackets
SAFE_LSB = strings.declare_as_safe("[")
SAFE_RSB = strings.declare_as_safe("]")
# Left and Right Parentheses
SAFE_LP = strings.declare_as_safe("(")
SAFE_RP = strings.declare_as_safe(")")
# Indent
INDENT = 4 * strings.BLANK
SAFE_INDENT = strings.declare_as_safe(INDENT)

__all__ = [
    "BaseElement",
    "InlineElement",
    "CompoundElement",
    "CompoundInlineElement",
    "BlockElement",
    "Paragraph",
    "RawHTMLBlock",
]


def render(
    *elements_sequence: Union[
        str, "InlineElement", "BlockElement", strings.SafeString
    ],
    indent_level: int = 0,
) -> str:
    """Render a sequence of elements"""
    indent = strings.EMPTY
    if indent_level > 0:
        indent = INDENT * indent_level
    #
    output_lines: List[str] = []
    previous_element: Optional[
        Union[str, InlineElement, BlockElement, strings.SafeString]
    ] = None
    for element in elements_sequence:
        # ensure block elements are divided by blank lines
        if (
            isinstance(element, BlockElement) and previous_element is not None
        ) or (
            isinstance(previous_element, BlockElement)
            and not isinstance(element, BlockElement)
        ):
            output_lines.append(strings.EMPTY)
        #
        #
        for line in element.splitlines():
            output_lines.append(f"{indent}{str(line)}")
        #
        previous_element = element
    #
    return strings.LF.join(output_lines)


class BaseElement(strings.SafeString):
    """MarkDown base class"""

    def __init__(self, source: Union[str, strings.SafeString]) -> None:
        """Store the defused internal source"""
        self.original_source_repr = repr(source)
        if isinstance(source, str):
            defused = strings.sanitize(source)
        else:
            defused = source
        #
        super().__init__(defused)

    def __repr__(self) -> str:
        """String representation"""
        return f"{self.__class__.__name__}({self.original_source_repr})"


class InlineElement(BaseElement):
    """Inline element, must not contain newlines"""

    def __init__(self, source: Union[str, strings.SafeString]) -> None:
        """Store the defused internal source"""
        super().__init__(source)
        if strings.LF in self:
            raise ValueError("Inline elements must not contain line feeds")
        #


class CompoundElement(BaseElement):
    """Compound MarkDown Element"""

    joiner: strings.SafeString = SAFE_EMPTY

    def __init__(
        self,
        *sources: Union[str, strings.SafeString],
    ) -> None:
        """Store the parts in a list"""
        self._sources: List[BaseElement] = []
        for item in sources:
            if isinstance(item, BaseElement):
                self._sources.append(item)
            else:
                self._sources.append(BaseElement(item))
            #
        #
        super().__init__(self.joiner.join(self._sources))
        self.original_source_repr = ARGS_JOINER.join(
            repr(single_source) for single_source in sources
        )

    def flattened(self):
        """return an iterator over flattened contents"""
        for item in self._sources:
            try:
                yield from item.flattened()
            except AttributeError:
                yield item
            #
        #


class CompoundInlineElement(CompoundElement, InlineElement):
    """Compound inline element"""

    def __init__(
        self,
        *sources: Union[str, strings.SafeString],
    ) -> None:
        """Ensure only inline elements are stored"""
        components: List[InlineElement] = []
        for item in sources:
            if isinstance(item, InlineElement):
                components.append(item)
            else:
                components.append(InlineElement(item))
            #
        #
        super().__init__(*components)
        self.original_source_repr = ARGS_JOINER.join(
            repr(single_source) for single_source in sources
        )


class BaseEmphasis(CompoundInlineElement):
    """Inline container element for emphasized text, base class"""

    description = "Emphasized"
    escape_pattern = strings.PRX_SPECIALS
    forbidden_contents: Set[strings.SafeString] = set()

    def __init__(
        self,
        source: Union[str, BaseElement],
        delimiter: strings.SafeString = SAFE_EMPTY,
    ) -> None:
        """Ensure the source does not contain forbidden contents"""
        if len(source) < 1:
            raise ValueError(
                f"Empty {self.description.lower()} text is not supported"
            )
        #
        if isinstance(source, str):
            checked_source: strings.SafeString = strings.sanitize(
                source, pattern=self.escape_pattern
            )
        else:
            if isinstance(source, CompoundElement):
                for item in source.flattened():
                    if item in self.forbidden_contents:
                        raise ValueError(
                            f"{self.description} text must not be nested"
                        )
                    #
                #
            #
            checked_source = source
        #
        super().__init__(delimiter, checked_source, delimiter)
        self.original_source_repr = (
            f"{source!r}{ARGS_JOINER}delimiter={delimiter!r}"
        )


class ItalicText(BaseEmphasis):
    """Italic text element"""

    description = "Italic"
    forbidden_contents: Set[strings.SafeString] = {SAFE_UNDERLINE}

    def __init__(self, source: Union[str, BaseElement]) -> None:
        """Make sure the source contains neither unescaped underlines
        nor any newlines, and prohibit nested italic text
        """
        super().__init__(source, delimiter=SAFE_UNDERLINE)
        self.original_source_repr = repr(source)


class BoldText(BaseEmphasis):
    """Bold text element"""

    description = "Bold"
    forbidden_contents: Set[strings.SafeString] = {
        SAFE_ASTERISK,
        2 * SAFE_ASTERISK,
    }

    def __init__(self, source: Union[str, BaseElement]) -> None:
        """Make sure the source contains neither unescaped asterisks
        nor any newlines, and prohibit nested bold text
        """
        super().__init__(source, delimiter=2 * SAFE_ASTERISK)
        self.original_source_repr = repr(source)


class BlockElement(CompoundElement):
    """Block element"""

    joiner: strings.SafeString = SAFE_LF
    prefix: Optional[strings.SafeString] = None
    indent_level = 0

    def __init__(self, *sources: Union[str, strings.SafeString]) -> None:
        """Store the lines in a CompoundElement,
        sanitize strings if necessary
        """
        source_elements: List[strings.SafeString] = []
        for element in sources:
            if isinstance(element, strings.SafeString):
                source_elements.append(element)
            else:
                source_elements.append(strings.sanitize(element))
            #
        #
        for element in source_elements:
            # Forbid Raw HTML elements inside other Elements
            if isinstance(element, RawHTMLBlock):
                raise ValueError(
                    "RawHTMLBlock elements must not be contained"
                    " in other elements"
                )
            #
        #
        self._source_lines: List[InlineElement] = []
        for line in render(*source_elements).splitlines():
            self._source_lines.append(
                self._prefixed_line(strings.declare_as_safe(line))
            )
        #
        super().__init__(*self._source_lines)
        self.original_source_repr = ARGS_JOINER.join(
            repr(single_source) for single_source in sources
        )

    def _prefixed_line(
        self, line: Union[str, strings.SafeString]
    ) -> InlineElement:
        """Prefix the line if a prefix has been set"""
        if self.prefix is None:
            return InlineElement(line)
        #
        if len(line) < 1:
            return InlineElement(self.prefix.rstrip())
        #
        return CompoundInlineElement(self.prefix, line)


class RawHTMLBlock(BlockElement):
    """Raw HTML block"""

    def __init__(
        self, html_block_element: html_generator.BlockElement
    ) -> None:
        """Initialize with the HTML block 'as is'"""
        super().__init__(strings.declare_as_safe(str(html_block_element)))
        self.original_source_repr = repr(html_block_element)


class Paragraph(BlockElement):
    """Paragraph"""


class Header(BlockElement):
    """Header"""

    setext_underline: Tuple[str, str, str] = ("", "=", "-")

    def __init__(
        self,
        level: int,
        source: Union[str, strings.SafeString],
        setext: bool = False,
    ) -> None:
        """Initialize element and attributes"""
        if not 0 < level < 7:
            raise ValueError("level must be between 1 and 6")
        #
        if isinstance(source, str):
            source = strings.sanitize(source)
        #
        if strings.LF in str(source):
            raise ValueError("Headers must not contain line feeds")
        #
        contents: List[strings.SafeString] = []
        if setext and level < 3:
            contents.append(source)
            contents.append(
                strings.declare_as_safe(
                    self.setext_underline[level] * len(source)
                )
            )
        else:
            contents.append(
                CompoundInlineElement(SAFE_POUND * level, SAFE_BLANK, source)
            )
        #
        super().__init__(*contents)
        self.original_source_repr = (
            f"{level}{ARGS_JOINER}{source!r}" f"{ARGS_JOINER}setext={setext!r}"
        )


class HorizontalRule(BlockElement):
    """Horizontal rule"""

    allowed_characters = "*-_"

    def __init__(
        self,
        number: int = 3,
        character: str = "-",
    ) -> None:
        """Initialize element and attributes"""
        if number < 3:
            raise ValueError("number of characters must be >= 3")
        #
        if len(character) != 1:
            raise ValueError("exactly one character is required")
        #
        if character not in self.allowed_characters:
            raise ValueError(
                f"character must be one of {self.allowed_characters.split()}"
            )
        #
        super().__init__(strings.declare_as_safe(number * character))
        self.original_source_repr = (
            f"number={number}{ARGS_JOINER}character={character!r}"
        )


class BlockQuote(BlockElement):
    """BlockQuote"""

    prefix = SAFE_BLOCKQUOTE_PREFIX


class ListItem(CompoundElement):
    """Base class for list elements"""

    joiner: strings.SafeString = SAFE_LF

    def __init__(
        self,
        *sources: Union[str, strings.SafeString],
        number: Optional[int] = None,
    ) -> None:
        """Store the lines of the indented list element"""
        self.block_display = False
        self.source_elements: List[strings.SafeString] = []
        for element in sources:
            if isinstance(element, BlockElement):
                self.block_display = True
            #
            if isinstance(element, strings.SafeString):
                self.source_elements.append(element)
            else:
                self.source_elements.append(strings.sanitize(element))
            #
        #
        if number is None:
            # unordered list
            prefix = "*"
        else:
            prefix = f"{number}."
        #
        additional_indent = len(prefix) // 4
        indent_level = 1 + additional_indent
        indent_chars = 4 * indent_level
        list_item_prefix = f"{prefix:<{indent_chars}}"
        blank_prefix = strings.BLANK * indent_chars
        # render contents, indented
        first_line = True
        item_lines: List[strings.SafeString] = []
        for line in render(*self.source_elements).splitlines():
            if first_line:
                output_prefix = list_item_prefix
                first_line = False
            else:
                output_prefix = blank_prefix
            #
            current_line = line
            if line or output_prefix.strip():
                current_line = f"{output_prefix}{line}"
            #
            item_lines.append(strings.declare_as_safe(current_line))
        #
        super().__init__(*item_lines)
        self.original_source_repr = ARGS_JOINER.join(
            [repr(single_source) for single_source in sources]
            + [f"number={number!r}"]
        )


class BaseList(BlockElement):
    """Base class for list elements"""

    start_number: Optional[int] = None
    increment: int = 1

    def __init__(self, *sources: Union[str, strings.SafeString]) -> None:
        """Store the list items ..."""
        items: List[ListItem] = []
        self.block_items = False
        current_number: Optional[int] = self.start_number
        for element in sources:
            if isinstance(element, ListItem):
                current_item: ListItem = element
            else:
                current_item = ListItem(element, number=current_number)
            #
            if current_item.block_display:
                self.block_items = True
            #
            items.append(current_item)
            if isinstance(current_number, int):
                current_number += self.increment
            #
        #
        separator = strings.LF
        if self.block_items:
            separator = 2 * strings.LF
        #
        output_parts: List[str] = []
        first_item = True
        for single_item in items:
            if first_item:
                output_parts.append(str(single_item))
                first_item = False
            else:
                output_parts.append(f"{separator}{str(single_item)}")
            #
        #
        # logging.warning("Output parts: %r", output_parts)
        super().__init__(
            strings.declare_as_safe(strings.EMPTY.join(output_parts))
        )
        self.original_source_repr = ARGS_JOINER.join(
            repr(single_source) for single_source in sources
        )


class UnorderedList(BaseList):
    """Unordered list"""


class OrderedList(BaseList):
    """Ordered list"""

    def __init__(
        self, *sources: Union[str, strings.SafeString], start_number: int = 1
    ) -> None:
        """Store the list items ..."""
        if start_number < 1:
            raise ValueError(f"Invalid start number: {start_number}")
        #
        self.start_number = start_number
        super().__init__(*sources)
        self.original_source_repr = ARGS_JOINER.join(
            [repr(single_source) for single_source in sources]
            + [f"start_number={start_number!r}"]
        )


class CodeBlock(BlockElement):
    """Indented code block"""

    prefix = SAFE_INDENT

    def __init__(self, *sources: Union[str, strings.SafeString]) -> None:
        """Store the lines as-is"""
        source_elements: List[strings.SafeString] = []
        for element in sources:
            if isinstance(element, strings.SafeString):
                source_elements.append(element)
            else:
                source_elements.append(strings.declare_as_safe(element))
            #
        #
        super().__init__(*source_elements)
        self.original_source_repr = ARGS_JOINER.join(
            repr(single_source) for single_source in sources
        )


class Label(BlockElement):
    """Label for a reference-style link or image"""

    break_threshold = 65

    def __init__(
        self, label_id: str, url: str, title: Optional[str] = None
    ) -> None:
        """Initialize"""
        core_label = CompoundInlineElement(
            SAFE_LSB,
            strings.sanitize(label_id),
            SAFE_RSB,
            strings.declare_as_safe(": "),
            strings.declare_as_safe(url),
        )
        lines: List[CompoundInlineElement] = []
        if title is None:
            lines.append(core_label)
        else:
            add_line_break = (
                len(title) + len(label_id) + len(url) >= self.break_threshold
            )
            components: List[strings.SafeString] = []
            if add_line_break:
                components.append(SAFE_INDENT)
            else:
                components.append(SAFE_BLANK)
            #
            if '"' not in title:
                safe_title_start = safe_title_end = SAFE_DOUBLE_QUOTE
            elif "'" not in title:
                safe_title_start = safe_title_end = SAFE_SINGLE_QUOTE
            else:
                safe_title_start = SAFE_LP
                safe_title_end = SAFE_RP
            #
            components.extend(
                (
                    safe_title_start,
                    strings.sanitize(title),
                    safe_title_end,
                )
            )
            title_part = CompoundInlineElement(*components)
            if add_line_break:
                lines.extend((core_label, title_part))
            else:
                lines.append(CompoundInlineElement(core_label, title_part))
            #
        #
        # TODO: sanitize label_id and URL
        super().__init__(*lines)
        self.original_source_repr = (
            f"{label_id!r}{ARGS_JOINER}{url!r}{ARGS_JOINER}title={title!r}"
        )


class BaseLink(CompoundInlineElement):
    """Link and image base class"""

    prefix: Optional[strings.SafeString] = None

    def __init__(
        self,
        text: str,
        ref: Optional[str] = None,
        url: Optional[str] = None,
        title: Optional[str] = None,
    ) -> None:
        """Initialize"""
        if (url is None and ref is None) or (
            url is not None and ref is not None
        ):
            raise ValueError("Specify either url or ref")
        #
        components: List[strings.SafeString] = []
        if isinstance(self.prefix, strings.SafeString):
            components.append(self.prefix)
        #
        components.extend((SAFE_LSB, strings.sanitize(text), SAFE_RSB))
        if isinstance(ref, str):
            components.extend(
                (
                    SAFE_LSB,
                    strings.sanitize(ref),
                    SAFE_RSB,
                )
            )
        elif isinstance(url, str):
            # TODO: sanitize URL
            parenthesized_content: List[strings.SafeString] = [
                strings.declare_as_safe(url)
            ]
            if isinstance(title, str):
                if '"' in title:
                    raise ValueError("Title must not contain double quotes")
                #
                parenthesized_content.extend(
                    (
                        SAFE_BLANK,
                        SAFE_DOUBLE_QUOTE,
                        strings.sanitize(title),
                        SAFE_DOUBLE_QUOTE,
                    )
                )
            #
            components.extend(
                (
                    SAFE_LP,
                    *parenthesized_content,
                    SAFE_RP,
                )
            )
        #
        super().__init__(*components)
        self.original_source_repr = (
            f"{text!r}{ARGS_JOINER}ref={ref!r}{ARGS_JOINER}url={url!r}"
            f"{ARGS_JOINER}title={title!r}"
        )


class Link(BaseLink):
    """Hyperlink"""


class Image(BaseLink):
    """Image"""

    prefix: strings.SafeString = SAFE_EXCLAMATION_MARK


class CodeSpan(CompoundInlineElement):
    """Backticks quoted inline literal"""

    def __init__(self, source: Union[str, strings.SafeString]) -> None:
        """Declare the internal source as safe and surround with backticks"""
        if len(source) < 1:
            raise ValueError("Empty code blocks are not supported")
        #
        quote = SAFE_BACKTICK
        if isinstance(source, strings.SafeString):
            safe_source = source
        else:
            safe_source = strings.declare_as_safe(source)
        #
        # Increase number of quotes if required
        while quote in safe_source:
            quote += SAFE_BACKTICK
        #
        # Surround enclosed text with blanks if it starts or ends
        # with a backtick
        raw = str(safe_source)
        if any(raw[index] == strings.BACKTICK for index in (0, -1)):
            safe_source = SAFE_BLANK + safe_source + SAFE_BLANK
        #
        super().__init__(quote, safe_source, quote)
        self.original_source_repr = repr(source)


class AutoLink(CompoundInlineElement):
    """Backticks quoted inline literal"""

    def __init__(self, url: Union[str, strings.SafeString]) -> None:
        """Declare the internal source as safe and surround with backticks"""
        if len(url) < 1:
            raise ValueError("Empty urls are not supported")
        #
        # TODO: sanitize URL
        if isinstance(url, strings.SafeString):
            safe_url = url
        else:
            safe_url = strings.declare_as_safe(url)
        #
        super().__init__(SAFE_LAB, safe_url, SAFE_RAB)
        self.original_source_repr = repr(url)


# vim: fileencoding=utf-8 ts=4 sts=4 sw=4 autoindent expandtab syntax=python:
