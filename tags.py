"""A tiny HTML builder so every page is written in Python, with no template files."""

from html import escape


class Raw(str):
    """A string that is already safe HTML and must not be escaped."""


VOID = {"meta", "link", "br", "hr", "img", "input"}


def h(tag, *children, **attrs):
    """Build an element: h("a", "Home", href="/") -> <a href="/">Home</a>.

    Use class_="x" for the class attribute and data_foo="y" for data-foo.
    Children can be strings (escaped), Raw, None/False (skipped), or lists.
    """
    parts = []
    for key, value in attrs.items():
        if value is None or value is False:
            continue
        name = key.rstrip("_").replace("_", "-")
        parts.append(name if value is True else f'{name}="{escape(str(value))}"')
    open_tag = f"<{tag}{' ' + ' '.join(parts) if parts else ''}>"
    if tag in VOID:
        return Raw(open_tag)
    return Raw(open_tag + render(children) + f"</{tag}>")


def render(node):
    if node is None or node is False:
        return ""
    if isinstance(node, Raw):
        return str(node)
    if isinstance(node, (list, tuple)):
        return "".join(render(child) for child in node)
    return escape(str(node))


def __getattr__(tag):
    # Lets pages write tags.div(...), tags.section(...), etc.
    return lambda *children, **attrs: h(tag, *children, **attrs)
