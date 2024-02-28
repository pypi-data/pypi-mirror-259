# -*- coding: utf-8 -*-

"""

tests.test_elements

Unit test the elements module (ie. Markdown source generation)


Copyright (C) 2024 Rainer Schwarzbach

This file is part of smdg.

smdg is free software: you can redistribute it and/or modify
it under the terms of the MIT License.

smdg is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
See the LICENSE file for more details.

"""


from unittest import TestCase

from smdg import elements
from smdg import html_generator as hg


EXPECTED_BQ_SIMPLE = "\n".join(("> line 1", "> line 2", "> line 3"))

# Examples from
# <https://daringfireball.net/projects/markdown/syntax#blockquote>

EXPECTED_RAW_HTML_EXAMPLE = """
This is a regular paragraph.

<table>
    <tr>
        <td>Foo</td>
    </tr>
</table>

This is another regular paragraph.
""".strip()

EXPECTED_SETEXT_HEADERS = """
This is an H1
=============

This is an H2
-------------
""".strip()

EXPECTED_ATX_HEADERS = """
# This is an H1

## This is an H2

###### This is an H6
""".strip()

EXPECTED_BQ_2_PARA = """
> This is a blockquote with two paragraphs. Lorem ipsum dolor sit amet,
> consectetuer adipiscing elit. Aliquam hendrerit mi posuere lectus.
> Vestibulum enim wisi, viverra nec, fringilla in, laoreet vitae, risus.
>
> Donec sit amet nisl. Aliquam semper ipsum sit amet velit. Suspendisse
> id sem consectetuer libero luctus adipiscing.
""".strip()

EXPECTED_BQ_NESTED = """
> This is the first level of quoting.
>
> > This is nested blockquote.
>
> Back to the first level.
""".strip()

EXPECTED_BQ_CONTAINER = """
> ## This is a header.
>
> 1.  This is the first list item.
> 2.  This is the second list item.
>
> Here's some example code:
>
>     return shell_exec("echo $input | $markdown_script");
""".strip()

EXPECTED_UNORDERED_LIST = """
*   Red
*   Green
*   Blue
""".strip()

EXPECTED_UNORDERED_LIST_HANGING_INDENTS = """
*   Lorem ipsum dolor sit amet, consectetuer adipiscing elit.
    Aliquam hendrerit mi posuere lectus. Vestibulum enim wisi,
    viverra nec, fringilla in, laoreet vitae, risus.
*   Donec sit amet nisl. Aliquam semper ipsum sit amet velit.
    Suspendisse id sem consectetuer libero luctus adipiscing.
""".strip()

EXPECTED_UNORDERED_LIST_OF_PARAGRAPHS = """
*   Bird

*   Magic
""".strip()

EXPECTED_UNORDERED_LIST_WITH_BLOCKQUOTE = """
*   A list item with a blockquote:

    > This is a blockquote
    > inside a list item.
""".strip()

EXPECTED_UNORDERED_LIST_WITH_CODEBLOCK = """
*   A list item with a code block:

        <code goes here>
""".strip()

EXPECTED_ORDERED_LIST = """
1.  Bird
2.  McHale
3.  Parish
""".strip()

EXPECTED_ORDERED_LIST_WITH_PARAGRAPHS = """
1.  This is a list item with two paragraphs. Lorem ipsum dolor
    sit amet, consectetuer adipiscing elit. Aliquam hendrerit
    mi posuere lectus.

    Vestibulum enim wisi, viverra nec, fringilla in, laoreet
    vitae, risus. Donec sit amet nisl. Aliquam semper ipsum
    sit amet velit.

2.  Suspendisse id sem consectetuer libero luctus adipiscing.
""".strip()

EXPECTED_CODEBLOCK = """    Here is an example of AppleScript:

        tell application "Foo"
            beep
        end tell
""".rstrip()

EXPECTED_CODEBLOCK_HTML = """    <div class="footer">
        &copy; 2004 Foo Corporation
    </div>
""".rstrip()

EXPECTED_HR_3_DASHES = "---"
EXPECTED_HR_7_ASTERISKS = "*******"

EXPECTED_LABEL_WITH_TITLE = '[foo]: http://example.com/ "Optional Title Here"'

EXPECTED_LABEL_WITH_LONGISH_URL_AND_TITLE = """
[id]: http://example.com/longish/path/to/resource/here
    "Optional Title Here"
""".strip()

EXPECTED_LABEL_WITH_PARENTHESIZED_TITLE = (
    """[foo]: http://example.com/ (Optional "Title" 'Here')"""
)
EXPECTED_LABEL_WITHOUT_TITLE = "[Daring Fireball]: http://daringfireball.net/"
EXPECTED_LABEL_REPR_WITH_TITLE = (
    "Label('foo', 'http://example.com/', title='Optional Title Here')"
)

EXPECTED_LINK_INLINE = "[example](http://example.com/)"
EXPECTED_LINK_REPR_INLINE = (
    "Link('example', ref=None, url='http://example.com/', title=None)"
)
EXPECTED_LINK_INLINE_WITH_TITLE = (
    """[example](http://example.com/ "Optional Title Here")"""
)
EXPECTED_LINK_REPR_INLINE_WITH_TITLE = (
    "Link('example', ref=None, url='http://example.com/',"
    " title='Optional Title Here')"
)
EXPECTED_LINK_REFERENCE = "[example][foo]"
EXPECTED_LINK_REPR_REFERENCE = (
    "Link('example', ref='foo', url=None, title=None)"
)

EXPECTED_IMAGE_INLINE = "![example](http://example.com/)"
EXPECTED_IMAGE_REPR_INLINE = (
    "Image('example', ref=None, url='http://example.com/', title=None)"
)
EXPECTED_IMAGE_INLINE_WITH_TITLE = (
    """![example](http://example.com/ "Optional Title Here")"""
)
EXPECTED_IMAGE_REPR_INLINE_WITH_TITLE = (
    "Image('example', ref=None, url='http://example.com/',"
    " title='Optional Title Here')"
)
EXPECTED_IMAGE_REFERENCE = "![example][foo]"
EXPECTED_IMAGE_REPR_REFERENCE = (
    "Image('example', ref='foo', url=None, title=None)"
)

EXPECTED_BOLD_TEXT = "**bold example**"
EXPECTED_ITALICS_INSIDE_BOLD_TEXT = "**bold _and italics_ example**"
EXPECTED_ITALICS = "_italics example_"
EXPECTED_BOLD_TEXT_INSIDE_ITALICS = "_italics **and bold** example_"

EXPECTED_CODESPAN_SIMPLE = "`<code_example>`"
EXPECTED_CODESPAN_WITH_BACKTICKS = "````md ```literal``` in code span````"
EXPECTED_CODESPAN_WITH_ADDITIONAL_SPACING = (
    "`` `nested code` with additional spacing ``"
)

EXPECTED_AUTOLINK_SIMPLE = "<email@example.com>"
EXPECTED_AUTOLINK_REPR = "AutoLink('email@example.com')"


class BaseElement(TestCase):
    """Test the RawHTMLBlock class"""

    maxDiff = None

    def test_str_simple(self) -> None:
        """test the string output"""
        b_elem = elements.BaseElement("This _is_ a base element.")
        self.assertEqual(
            str(b_elem),
            "This \\_is\\_ a base element.",
        )

    def test_repr_simple(self) -> None:
        """test the representation"""
        b_elem = elements.BaseElement("This _is_ a base element.")
        self.assertEqual(
            repr(b_elem),
            "BaseElement('This _is_ a base element.')",
        )


class InlineElement(TestCase):
    """Test the InlineElement class"""

    def test_init(self) -> None:
        """test the LF check"""
        self.assertRaisesRegex(
            ValueError,
            "^Inline elements must not contain line feeds$",
            elements.InlineElement,
            "more\nthan\na single line",
        )
        b_elem = elements.BaseElement("This _is_ a base element.")
        self.assertEqual(
            str(b_elem),
            "This \\_is\\_ a base element.",
        )


class RawHTMLBlock(TestCase):
    """Test the RawHTMLBlock class"""

    maxDiff = None

    def test_str_simple(self) -> None:
        """test the string representation"""
        paragraph_1 = elements.Paragraph("This is a regular paragraph.")
        raw_html_block = elements.RawHTMLBlock(
            hg.Table(hg.TableRow(hg.TableCell("Foo")))
        )
        paragraph_2 = elements.Paragraph("This is another regular paragraph.")
        self.assertEqual(
            elements.render(paragraph_1, raw_html_block, paragraph_2),
            EXPECTED_RAW_HTML_EXAMPLE,
        )


class Header(TestCase):
    """Test the Header class"""

    maxDiff = None

    def test_setext_style(self) -> None:
        """test the setext style string representation"""
        header_1 = elements.Header(1, "This is an H1", setext=True)
        header_2 = elements.Header(2, "This is an H2", setext=True)
        self.assertEqual(
            elements.render(header_1, header_2),
            EXPECTED_SETEXT_HEADERS,
        )

    def test_atx_style(self) -> None:
        """test the setext style string representation"""
        header_1 = elements.Header(1, "This is an H1")
        header_2 = elements.Header(2, "This is an H2")
        header_6 = elements.Header(6, "This is an H6")
        self.assertEqual(
            elements.render(header_1, header_2, header_6),
            EXPECTED_ATX_HEADERS,
        )

    def test_str_nested(self) -> None:
        """test the string representation"""
        bq_elem = elements.BlockQuote(
            "This is the first level of quoting.",
            elements.BlockQuote("This is nested blockquote."),
            "Back to the first level.",
        )
        self.assertEqual(str(bq_elem), EXPECTED_BQ_NESTED)


class BlockQuote(TestCase):
    """Test the BlockQuote class"""

    maxDiff = None

    def test_simple(self) -> None:
        """simple blockquote"""
        bq_elem = elements.BlockQuote("line 1\nline 2\nline 3")
        self.assertEqual(str(bq_elem), EXPECTED_BQ_SIMPLE)

    def test_2_paragraphs(self) -> None:
        """Two-paragraphs example from the spec"""
        para_1 = elements.Paragraph(
            "This is a blockquote with two paragraphs."
            " Lorem ipsum dolor sit amet,",
            "consectetuer adipiscing elit."
            " Aliquam hendrerit mi posuere lectus.",
            "Vestibulum enim wisi, viverra nec,"
            " fringilla in, laoreet vitae, risus.",
        )
        para_2 = elements.Paragraph(
            "Donec sit amet nisl. Aliquam semper ipsum sit amet velit."
            " Suspendisse",
            "id sem consectetuer libero luctus adipiscing.",
        )
        bq_2_para = elements.BlockQuote(para_1, para_2)
        self.assertEqual(str(bq_2_para), EXPECTED_BQ_2_PARA)

    def test_nested(self) -> None:
        """nested blockquotes"""
        bq_elem = elements.BlockQuote(
            "This is the first level of quoting.",
            elements.BlockQuote("This is nested blockquote."),
            "Back to the first level.",
        )
        self.assertEqual(str(bq_elem), EXPECTED_BQ_NESTED)

    def test_containers(self) -> None:
        """container lements"""
        bq_elem = elements.BlockQuote(
            elements.Header(2, "This is a header."),
            elements.OrderedList(
                "This is the first list item.",
                "This is the second list item.",
            ),
            elements.Paragraph("Here's some example code:"),
            elements.CodeBlock(
                'return shell_exec("echo $input | $markdown_script");'
            ),
        )
        self.assertEqual(str(bq_elem), EXPECTED_BQ_CONTAINER)


class CodeBlock(TestCase):
    """Test the CodeBlock class"""

    maxDiff = None

    def test_applescript(self) -> None:
        """code block: apple script, from the spec"""
        cb_elem = elements.CodeBlock(
            "Here is an example of AppleScript:\n"
            "\n"
            '    tell application "Foo"\n'
            "        beep\n"
            "    end tell"
        )
        self.assertEqual(str(cb_elem), EXPECTED_CODEBLOCK)

    def test_html(self) -> None:
        """code block: HTML, from the spec"""
        cb_elem = elements.CodeBlock(
            '<div class="footer">',
            "    &copy; 2004 Foo Corporation",
            "</div>",
        )
        self.assertEqual(str(cb_elem), EXPECTED_CODEBLOCK_HTML)


class HorizontalRule(TestCase):
    """Test the HorizontalRule class"""

    maxDiff = None

    def test_default(self) -> None:
        """default horizontal rule with 3 dashes"""
        hr_elem = elements.HorizontalRule()
        self.assertEqual(str(hr_elem), EXPECTED_HR_3_DASHES)

    def test_7_asterisks(self) -> None:
        """horizontal rule with 7 asterisks"""
        hr_elem = elements.HorizontalRule(7, "*")
        self.assertEqual(str(hr_elem), EXPECTED_HR_7_ASTERISKS)


class UnorderedList(TestCase):
    """Test the UnorderedList class"""

    def test_simple(self) -> None:
        """unordered list with simple elements"""
        ul_elem = elements.UnorderedList("Red", "Green", "Blue")
        self.assertEqual(str(ul_elem), EXPECTED_UNORDERED_LIST)

    def test_hanging_indents(self) -> None:
        """unordered list with simple elements and hanging indents"""
        ul_elem = elements.UnorderedList(
            "Lorem ipsum dolor sit amet, consectetuer adipiscing elit.\n"
            "Aliquam hendrerit mi posuere lectus. Vestibulum enim wisi,\n"
            "viverra nec, fringilla in, laoreet vitae, risus.",
            "Donec sit amet nisl. Aliquam semper ipsum sit amet velit.\n"
            "Suspendisse id sem consectetuer libero luctus adipiscing.",
        )
        self.assertEqual(str(ul_elem), EXPECTED_UNORDERED_LIST_HANGING_INDENTS)

    def test_with_blockquote(self) -> None:
        """unordered list with a blockquote"""
        ul_elem = elements.UnorderedList(
            elements.ListItem(
                "A list item with a blockquote:",
                elements.BlockQuote(
                    "This is a blockquote",
                    "inside a list item.",
                ),
            )
        )
        self.assertEqual(str(ul_elem), EXPECTED_UNORDERED_LIST_WITH_BLOCKQUOTE)

    def test_with_codeblock(self) -> None:
        """unordered list with a code block"""
        ul_elem = elements.UnorderedList(
            elements.ListItem(
                "A list item with a code block:",
                elements.CodeBlock("<code goes here>"),
            )
        )
        self.assertEqual(str(ul_elem), EXPECTED_UNORDERED_LIST_WITH_CODEBLOCK)

    def test_with_parapraphs(self) -> None:
        """unordered list with pragraphs"""
        ul_elem = elements.UnorderedList(
            elements.Paragraph("Bird"),
            elements.Paragraph("Magic"),
        )
        self.assertEqual(str(ul_elem), EXPECTED_UNORDERED_LIST_OF_PARAGRAPHS)


class OrderedList(TestCase):
    """Test the OrderedList class"""

    def test_simple(self) -> None:
        """unordered list with simple elements"""
        ol_elem = elements.OrderedList("Bird", "McHale", "Parish")
        self.assertEqual(str(ol_elem), EXPECTED_ORDERED_LIST)

    def test_with_paragraphs(self) -> None:
        """unordered list with simple elements"""
        ol_elem = elements.OrderedList(
            elements.ListItem(
                elements.Paragraph(
                    "This is a list item with two paragraphs."
                    " Lorem ipsum dolor",
                    "sit amet, consectetuer adipiscing elit."
                    " Aliquam hendrerit",
                    "mi posuere lectus.",
                ),
                elements.Paragraph(
                    "Vestibulum enim wisi, viverra nec, fringilla in, laoreet",
                    "vitae, risus. Donec sit amet nisl. Aliquam semper ipsum",
                    "sit amet velit.",
                ),
                number=1,
            ),
            elements.ListItem(
                elements.Paragraph(
                    "Suspendisse id sem consectetuer libero luctus adipiscing."
                ),
                number=2,
            ),
        )
        self.assertEqual(str(ol_elem), EXPECTED_ORDERED_LIST_WITH_PARAGRAPHS)


class Label(TestCase):
    """Test the Label class"""

    def test_with_title(self) -> None:
        """Test a label with title"""
        with self.subTest("default: title in parentheses"):
            label = elements.Label(
                "foo", "http://example.com/", title="Optional Title Here"
            )
            self.assertEqual(str(label), EXPECTED_LABEL_WITH_TITLE)
        #
        with self.subTest("fallback: title in quotes"):
            label = elements.Label(
                "foo",
                "http://example.com/",
                title="""Optional "Title" 'Here'""",
            )
            self.assertEqual(
                str(label), EXPECTED_LABEL_WITH_PARENTHESIZED_TITLE
            )
        #

    def test_with_lonmgish_url_and_title(self) -> None:
        """Test a label with title"""
        label = elements.Label(
            "id",
            "http://example.com/longish/path/to/resource/here",
            title="Optional Title Here",
        )
        self.assertEqual(str(label), EXPECTED_LABEL_WITH_LONGISH_URL_AND_TITLE)

    def test_without_title(self) -> None:
        """Test a label without title"""
        label = elements.Label("Daring Fireball", "http://daringfireball.net/")
        self.assertEqual(str(label), EXPECTED_LABEL_WITHOUT_TITLE)

    def test_repr_with_title(self) -> None:
        """Test a label representation with title"""
        label = elements.Label(
            "foo", "http://example.com/", title="Optional Title Here"
        )
        self.assertEqual(repr(label), EXPECTED_LABEL_REPR_WITH_TITLE)


class Link(TestCase):
    """Test the Link class"""

    def test_inline(self) -> None:
        """inline style"""
        link = elements.Link("example", url="http://example.com/")
        self.assertEqual(str(link), EXPECTED_LINK_INLINE)

    def test_repr_inline(self) -> None:
        """representation of an inline style link"""
        link = elements.Link("example", url="http://example.com/")
        self.assertEqual(repr(link), EXPECTED_LINK_REPR_INLINE)

    def test_inline_with_title(self) -> None:
        """inline style"""
        link = elements.Link(
            "example", url="http://example.com/", title="Optional Title Here"
        )
        self.assertEqual(str(link), EXPECTED_LINK_INLINE_WITH_TITLE)

    def test_repr_inline_with_title(self) -> None:
        """representation of an inline style link"""
        link = elements.Link(
            "example", url="http://example.com/", title="Optional Title Here"
        )
        self.assertEqual(repr(link), EXPECTED_LINK_REPR_INLINE_WITH_TITLE)

    def test_reference(self) -> None:
        """reference style"""
        link = elements.Link("example", ref="foo")
        self.assertEqual(str(link), EXPECTED_LINK_REFERENCE)

    def test_repr_reference(self) -> None:
        """representation of an reference style link"""
        link = elements.Link("example", ref="foo")
        self.assertEqual(repr(link), EXPECTED_LINK_REPR_REFERENCE)


class Image(TestCase):
    """Test the Image class"""

    def test_inline(self) -> None:
        """inline style"""
        image = elements.Image("example", url="http://example.com/")
        self.assertEqual(str(image), EXPECTED_IMAGE_INLINE)

    def test_repr_inline(self) -> None:
        """representation of an inline style image"""
        image = elements.Image("example", url="http://example.com/")
        self.assertEqual(repr(image), EXPECTED_IMAGE_REPR_INLINE)

    def test_inline_with_title(self) -> None:
        """inline style"""
        image = elements.Image(
            "example", url="http://example.com/", title="Optional Title Here"
        )
        self.assertEqual(str(image), EXPECTED_IMAGE_INLINE_WITH_TITLE)

    def test_repr_inline_with_title(self) -> None:
        """representation of an inline style image"""
        image = elements.Image(
            "example", url="http://example.com/", title="Optional Title Here"
        )
        self.assertEqual(repr(image), EXPECTED_IMAGE_REPR_INLINE_WITH_TITLE)

    def test_reference(self) -> None:
        """reference style"""
        image = elements.Image("example", ref="foo")
        self.assertEqual(str(image), EXPECTED_IMAGE_REFERENCE)

    def test_repr_reference(self) -> None:
        """representation of an reference style image"""
        image = elements.Image("example", ref="foo")
        self.assertEqual(repr(image), EXPECTED_IMAGE_REPR_REFERENCE)


class Emphasis(TestCase):
    """Test the BoldText and ItalicText classes"""

    def test_simple_bold(self) -> None:
        """simple bold text"""
        bold_elem = elements.BoldText("bold example")
        self.assertEqual(str(bold_elem), EXPECTED_BOLD_TEXT)

    def test_italics_inside_bold(self) -> None:
        """italics nested in bold text"""
        bold_elem = elements.BoldText(
            elements.CompoundInlineElement(
                "bold ", elements.ItalicText("and italics"), " example"
            )
        )
        self.assertEqual(str(bold_elem), EXPECTED_ITALICS_INSIDE_BOLD_TEXT)

    def test_nested_bold(self) -> None:
        """bold text nested in bold text: error"""
        self.assertRaisesRegex(
            ValueError,
            "^Bold text must not be nested",
            elements.BoldText,
            elements.CompoundInlineElement(
                "bold ", elements.BoldText("and bold"), " example"
            ),
        )

    def test_simple_italics(self) -> None:
        """simple italics text"""
        italics_elem = elements.ItalicText("italics example")
        self.assertEqual(str(italics_elem), EXPECTED_ITALICS)

    def test_bold_inside_italics(self) -> None:
        """bold text nested in italics"""
        italics_elem = elements.ItalicText(
            elements.CompoundInlineElement(
                "italics ", elements.BoldText("and bold"), " example"
            )
        )
        self.assertEqual(str(italics_elem), EXPECTED_BOLD_TEXT_INSIDE_ITALICS)

    def test_empty_italics(self) -> None:
        """Initialization with empty contents: error"""
        self.assertRaisesRegex(
            ValueError,
            "^Empty italic text is not supported",
            elements.ItalicText,
            "",
        )


class CodeSpan(TestCase):
    """Test the CodeSpan class"""

    def test_simple(self) -> None:
        """simple code span"""
        cs_elem = elements.CodeSpan("<code_example>")
        self.assertEqual(str(cs_elem), EXPECTED_CODESPAN_SIMPLE)

    def test_with_backticks(self) -> None:
        """code span with backticks"""
        cs_elem = elements.CodeSpan("md ```literal``` in code span")
        self.assertEqual(str(cs_elem), EXPECTED_CODESPAN_WITH_BACKTICKS)

    def test_with_additional_spacing(self) -> None:
        """code span with automatically inserted additional soacing"""
        cs_elem = elements.CodeSpan("`nested code` with additional spacing")
        self.assertEqual(
            str(cs_elem), EXPECTED_CODESPAN_WITH_ADDITIONAL_SPACING
        )

    def test_contents_required(self) -> None:
        """Empty code blocks are not allowed"""
        self.assertRaisesRegex(
            ValueError,
            "^Empty code blocks are not supported",
            elements.CodeSpan,
            "",
        )

    def test_no_lf_allowed(self) -> None:
        """No line feed allowed in code span"""
        self.assertRaisesRegex(
            ValueError,
            "^Inline elements must not contain line feeds",
            elements.CodeSpan,
            "one line \n another line",
        )


class AutoLink(TestCase):
    """Test the AutoLink class"""

    def test_simple(self) -> None:
        """simple AutoLink"""
        al_elem = elements.AutoLink("email@example.com")
        self.assertEqual(str(al_elem), EXPECTED_AUTOLINK_SIMPLE)

    def test_repr(self) -> None:
        """simple AutoLink representation"""
        al_elem = elements.AutoLink("email@example.com")
        self.assertEqual(repr(al_elem), EXPECTED_AUTOLINK_REPR)


# vim: fileencoding=utf-8 ts=4 sts=4 sw=4 autoindent expandtab syntax=python:
