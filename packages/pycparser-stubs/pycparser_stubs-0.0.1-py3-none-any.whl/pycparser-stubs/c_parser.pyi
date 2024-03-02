from typing import Any

from pycparser.c_ast import *
from pycparser.c_lexer import CLexer
from pycparser.plyparser import PLYParser


class CParser(PLYParser):
    def __init__(self,
        lex_optimize: bool = True,
        lexer: Any = CLexer,
        lextab: str = 'pycparser.lextab',
        yacc_optimize: bool = True,
        yacctab: str = 'pycparser.yacctab',
        yacc_debug: bool = False,
        taboutputdir: str = ''
    ) -> None:
        """ Create a new CParser.

            Some arguments for controlling the debug/optimization
            level of the parser are provided. The defaults are
            tuned for release/performance mode.
            The simple rules for using them are:
            *) When tweaking CParser/CLexer, set these to False
            *) When releasing a stable parser, set to True

            lex_optimize:
                Set to False when you're modifying the lexer.
                Otherwise, changes in the lexer won't be used, if
                some lextab.py file exists.
                When releasing with a stable lexer, set to True
                to save the re-generation of the lexer table on
                each run.

            lexer:
                Set this parameter to define the lexer to use if
                you're not using the default CLexer.

            lextab:
                Points to the lex table that's used for optimized
                mode. Only if you're modifying the lexer and want
                some tests to avoid re-generating the table, make
                this point to a local lex table file (that's been
                earlier generated with lex_optimize=True)

            yacc_optimize:
                Set to False when you're modifying the parser.
                Otherwise, changes in the parser won't be used, if
                some parsetab.py file exists.
                When releasing with a stable parser, set to True
                to save the re-generation of the parser table on
                each run.

            yacctab:
                Points to the yacc table that's used for optimized
                mode. Only if you're modifying the parser, make
                this point to a local yacc table file

            yacc_debug:
                Generate a parser.out file that explains how yacc
                built the parsing table from the grammar.

            taboutputdir:
                Set this parameter to control the location of generated
                lextab and yacctab files.
        """

    def parse(self, text: str, filename: str = '', debug: bool = False) -> FileAST:
        """ Parses C code and returns an AST.

            text:
                A string containing the C source code

            filename:
                Name of the file being parsed (for meaningful
                error messages)

            debug:
                Debug flag to YACC
        """
