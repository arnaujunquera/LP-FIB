import sys
from antlr4 import *
from EnquestesLexer import EnquestesLexer
from EnquestesParser import EnquestesParser
from antlr4.InputStream import InputStream
from EnquestesVisitorAST import EnquestesVisitorAST

if len(sys.argv) > 1:
    input_stream = FileStream(sys.argv[1], 'UTF-8')
else:
    input_stream = InputStream(input('? '))

lexer = EnquestesLexer(input_stream)
token_stream = CommonTokenStream(lexer)
parser = EnquestesParser(token_stream)
tree = parser.root()

visitor = EnquestesVisitorAST()
visitor.visit(tree)