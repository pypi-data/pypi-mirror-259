# Simple (pythonic) MarkDown Generator

_Modules to programmatically generate MarkDown source code in a pythonic way_

```
pip install smdg
```

Installation in a virtual environment is strongly recommended.


## Example usage

Use the classes in the **smdg.elements** module
to create MarkDown elements.

Some elements may be nested,
and the **smdg.elements.render()** function
can be used to return a MarkDown document
(consisting of the provided elements)
as a single string.


```
>>> from smdg import elements as me
>>>
>>> h1 = me.Header(1, "Main header")
>>> h2 = me.Header(2, "Printing colors:")
>>> p = me.Paragraph("Lorem ipsum dolor sit amet,\nconsectetuer adipiscing elit.")
>>> pre = me.CodeBlock('def main() -> int:\n    """main function"""\n    return 0')
>>> ul = me.UnorderedList("Cyan", "Magenta", "Yellow", "Key")
>>>
>>> print(h1)
# Main header
>>> print(h2)
## Printing colors:
>>> print(p)
Lorem ipsum dolor sit amet,
consectetuer adipiscing elit.
>>>
>>> print(me.render(h1, p, pre, h2, ul))
# Main header

Lorem ipsum dolor sit amet,
consectetuer adipiscing elit.

    def main() -> int:
        """main function"""
        return 0

## Printing colors:

*   Cyan
*   Magenta
*   Yellow
*   Key
>>>
>>> print(me.BlockQuote(h1, p, pre, h2, ul))
> # Main header
>
> Lorem ipsum dolor sit amet,
> consectetuer adipiscing elit.
>
>     def main() -> int:
>         """main function"""
>         return 0
>
> ## Printing colors:
>
> *   Cyan
> *   Magenta
> *   Yellow
> *   Key
>>>
```


## Further reading

Please see the documentation at <https://blackstream-x.gitlab.io/smdg>
for detailed usage information.

If you found a bug or have a feature suggestion,
please open an issue [here](https://gitlab.com/blackstream-x/smdg/-/issues)

