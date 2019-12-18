# Generated from Enquestes.g by ANTLR 4.7.1
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\13")
        buf.write("G\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3")
        buf.write("\2\3\2\3\2\3\2\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4")
        buf.write("\3\4\3\4\3\4\3\5\3\5\3\6\3\6\3\7\6\7\63\n\7\r\7\16\7\64")
        buf.write("\3\b\6\b8\n\b\r\b\16\b9\3\t\6\t=\n\t\r\t\16\t>\3\n\6\n")
        buf.write("B\n\n\r\n\16\nC\3\n\3\n\2\2\13\3\3\5\4\7\5\t\6\13\7\r")
        buf.write("\b\17\t\21\n\23\13\3\2\6\6\2\"\"C\\c|\u0082\u0101\3\2")
        buf.write("\62;\5\2\62;C\\c|\4\2\f\f\"\"\2J\2\3\3\2\2\2\2\5\3\2\2")
        buf.write("\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2")
        buf.write("\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\3\25\3\2\2\2\5 ")
        buf.write("\3\2\2\2\7\"\3\2\2\2\t-\3\2\2\2\13/\3\2\2\2\r\62\3\2\2")
        buf.write("\2\17\67\3\2\2\2\21<\3\2\2\2\23A\3\2\2\2\25\26\7<\2\2")
        buf.write("\26\27\7\"\2\2\27\30\7R\2\2\30\31\7T\2\2\31\32\7G\2\2")
        buf.write("\32\33\7I\2\2\33\34\7W\2\2\34\35\7P\2\2\35\36\7V\2\2\36")
        buf.write("\37\7C\2\2\37\4\3\2\2\2 !\7A\2\2!\6\3\2\2\2\"#\7<\2\2")
        buf.write("#$\7\"\2\2$%\7T\2\2%&\7G\2\2&\'\7U\2\2\'(\7R\2\2()\7Q")
        buf.write("\2\2)*\7U\2\2*+\7V\2\2+,\7C\2\2,\b\3\2\2\2-.\7<\2\2.\n")
        buf.write("\3\2\2\2/\60\7=\2\2\60\f\3\2\2\2\61\63\t\2\2\2\62\61\3")
        buf.write("\2\2\2\63\64\3\2\2\2\64\62\3\2\2\2\64\65\3\2\2\2\65\16")
        buf.write("\3\2\2\2\668\t\3\2\2\67\66\3\2\2\289\3\2\2\29\67\3\2\2")
        buf.write("\29:\3\2\2\2:\20\3\2\2\2;=\t\4\2\2<;\3\2\2\2=>\3\2\2\2")
        buf.write("><\3\2\2\2>?\3\2\2\2?\22\3\2\2\2@B\t\5\2\2A@\3\2\2\2B")
        buf.write("C\3\2\2\2CA\3\2\2\2CD\3\2\2\2DE\3\2\2\2EF\b\n\2\2F\24")
        buf.write("\3\2\2\2\7\2\649>C\3\b\2\2")
        return buf.getvalue()


class EnquestesLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    TEXT = 6
    NUM = 7
    ID = 8
    WS = 9

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "': PREGUNTA'", "'?'", "': RESPOSTA'", "':'", "';'" ]

    symbolicNames = [ "<INVALID>",
            "TEXT", "NUM", "ID", "WS" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "TEXT", "NUM", 
                  "ID", "WS" ]

    grammarFileName = "Enquestes.g"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


