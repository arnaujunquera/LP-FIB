import sys
from antlr4 import *
from ExprLexer import ExprLexer
from ExprParser import ExprParser
from antlr4.InputStream import InputStream

if len(sys.argv) > 1:
    input_stream = FileStream(sys.argv[1])
else:
    input_stream = InputStream(input('? '))

lexer = ExprLexer(input_stream)
token_stream = CommonTokenStream(lexer)
parser = ExprParser(token_stream)
tree = parser.root()
print(tree.toStringTree(recog=parser))
