"""pygments lexer for W3C EBNF grammars."""

from pygments.lexer import RegexLexer, include, bygroups
from pygments.token import \
    Operator, String, Punctuation, Comment, Text, Literal, Name


class AbnfLexer(RegexLexer):

    """
    Lexer for IETF ABNF grammars.

    Formal specification: <http://tools.ietf.org/html/rfc5234>.

    """

    name = 'ABNF'
    aliases = ['abnf', 'rfc5234']
    filenames = ['*.abnf']
    mimetypes = ['text/x-abnf']

    tokens = {
        'root': [
            (r'^\s+', Text, 'production'), # rule continues if starts with whitespace
            include('whitespace'),
            include('comment'),
            include('identifier'),
            (r'=', Operator, 'production'),
        ],
        'production': [
            (r'\n', Text.Break, '#pop'),
            include('whitespace'),
            include('comment'),
            include('identifier'),
            include('codepoint'),
            (r'"[^"]*"', String.Double),
            (r'\d+', Literal),
            # (r"'[^']*'", String.Single),
            (r'[()\[\]]', Punctuation),
            (r'[-*\/]', Operator),
        ],
        'codepoint': [
            # hex
            (r'(%x[0-9A-Fa-f]+)(-)([0-9A-Fa-f]+)',
             bygroups(Literal, Operator, Literal)),
            (r'%x[0-9A-Fa-f]+(\.[0-9A-Fa-f]]+)?', Literal),
            # decimal
            (r'(%d\d+)(-)(\d+)', bygroups(Literal, Operator, Literal)),
            (r'%d\d+(\.\d+)?', Literal),
            # binary
            (r'(%b[01]+)(-)([01]+)', bygroups(Literal, Operator, Literal)),
            (r'%b[01]+(\.[01]+)?', Literal),
        ],
        'whitespace': [
            (r'\s+', Text),
        ],
        'comment': [
            (r';(.*)$', Comment),
        ],
        'identifier': [
            (r'([A-Z]+)', Name),
            (r'([a-zA-Z][a-zA-Z0-9\-]*)', Name),
            (r'(<)([ -=?-~]*)(>)', bygroups(Punctuation, Name, Punctuation)),
        ],
    }
