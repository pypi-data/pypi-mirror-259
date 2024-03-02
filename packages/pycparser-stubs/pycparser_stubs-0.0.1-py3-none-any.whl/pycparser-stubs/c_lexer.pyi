from typing import Any, Callable

from pycparser.ply.lex import LexToken


class CLexer(object):
    """ A lexer for the C language. After building it, set the
        input text with input(), and call token() to get new
        tokens.

        The public attribute filename can be set to an initial
        filename, but the lexer will update it upon #line
        directives.
    """
    
    def __init__(self,
        error_func: Callable[[str, int, int], Any],
        on_lbrace_func: Callable[[], Any],
        on_rbrace_func: Callable[[], Any],
        type_lookup_func: Callable[[str], bool],
    ):
        """ Create a new Lexer.

            error_func:
                An error function. Will be called with an error
                message, line and column as arguments, in case of
                an error during lexing.

            on_lbrace_func, on_rbrace_func:
                Called when an LBRACE or RBRACE is encountered
                (likely to push/pop type_lookup_func's scope)

            type_lookup_func:
                A type lookup function. Given a string, it must
                return True IFF this string is a name of a type
                that was defined with a typedef earlier.
        """
    
    def build(self, **kwargs) -> None:
        """ Builds the lexer from the specification. Must be
            called after the lexer object is created.

            This method exists separately, because the PLY
            manual warns against calling lex.lex inside
            __init__
        """

    def reset_lineno(self) -> None:
        """ Resets the internal line number counter of the lexer.
        """

    def input(self, text: str) -> None: ...

    def token(self) -> LexToken: ...

    def find_tok_column(self, token: LexToken) -> int:
        """ Find the column of the token in its line.
        """
