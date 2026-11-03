"""Syntax highlighting for the tutorial code, written with Python's own tokenizer.

highlight(source) returns HTML where keywords, strings, comments, numbers,
built-in names and function names are wrapped in <span class="..."> tags.
"""

import builtins
import io
import keyword
import tokenize
from html import escape

BUILTINS = set(dir(builtins))


def _kind(tok, prev):
    if tok.type == tokenize.COMMENT:
        return "c"
    if tok.type == tokenize.STRING or tok.type in _FSTRING:
        return "s"
    if tok.type == tokenize.NUMBER:
        return "n"
    if tok.type == tokenize.NAME:
        if keyword.iskeyword(tok.string):
            return "k"
        if prev is not None and prev.string in ("def", "class"):
            return "f"
        if tok.string in BUILTINS:
            return "b"
    return None


_FSTRING = {getattr(tokenize, n) for n in ("FSTRING_START", "FSTRING_MIDDLE", "FSTRING_END") if hasattr(tokenize, n)}


def highlight(source):
    lines = source.splitlines(keepends=True)
    offsets = [0]
    for line in lines:
        offsets.append(offsets[-1] + len(line))

    def pos(row, col):
        return offsets[row - 1] + col

    out, cursor, prev = [], 0, None
    for tok in tokenize.generate_tokens(io.StringIO(source).readline):
        if tok.type in (tokenize.ENDMARKER, tokenize.DEDENT, tokenize.INDENT, tokenize.NEWLINE, tokenize.NL):
            continue
        start, end = pos(*tok.start), pos(*tok.end)
        kind = _kind(tok, prev)
        if start < cursor:  # pieces inside an f-string already written
            continue
        out.append(escape(source[cursor:start], quote=False))
        text = escape(source[start:end], quote=False)
        out.append(f'<span class="{kind}">{text}</span>' if kind else text)
        cursor = end
        prev = tok
    out.append(escape(source[cursor:], quote=False))
    return "".join(out)
