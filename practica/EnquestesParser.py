# Generated from Enquestes.g by ANTLR 4.7.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\13")
        buf.write("(\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\3\2\6\2\16\n")
        buf.write("\2\r\2\16\2\17\3\2\3\2\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\5")
        buf.write("\3\5\3\5\3\5\6\5\37\n\5\r\5\16\5 \3\6\3\6\3\6\3\6\3\6")
        buf.write("\3\6\2\2\7\2\4\6\b\n\2\2\2$\2\r\3\2\2\2\4\23\3\2\2\2\6")
        buf.write("\25\3\2\2\2\b\32\3\2\2\2\n\"\3\2\2\2\f\16\5\4\3\2\r\f")
        buf.write("\3\2\2\2\16\17\3\2\2\2\17\r\3\2\2\2\17\20\3\2\2\2\20\21")
        buf.write("\3\2\2\2\21\22\7\2\2\3\22\3\3\2\2\2\23\24\5\6\4\2\24\5")
        buf.write("\3\2\2\2\25\26\7\n\2\2\26\27\7\3\2\2\27\30\7\b\2\2\30")
        buf.write("\31\7\4\2\2\31\7\3\2\2\2\32\33\7\n\2\2\33\34\7\5\2\2\34")
        buf.write("\36\7\b\2\2\35\37\5\n\6\2\36\35\3\2\2\2\37 \3\2\2\2 \36")
        buf.write("\3\2\2\2 !\3\2\2\2!\t\3\2\2\2\"#\7\t\2\2#$\7\6\2\2$%\7")
        buf.write("\b\2\2%&\7\7\2\2&\13\3\2\2\2\4\17 ")
        return buf.getvalue()


class EnquestesParser ( Parser ):

    grammarFileName = "Enquestes.g"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "': PREGUNTA'", "'?'", "': RESPOSTA'", 
                     "':'", "';'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "TEXT", "NUM", "ID", "WS" ]

    RULE_root = 0
    RULE_expr = 1
    RULE_preg = 2
    RULE_resp = 3
    RULE_opcn = 4

    ruleNames =  [ "root", "expr", "preg", "resp", "opcn" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    TEXT=6
    NUM=7
    ID=8
    WS=9

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class RootContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(EnquestesParser.EOF, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(EnquestesParser.ExprContext)
            else:
                return self.getTypedRuleContext(EnquestesParser.ExprContext,i)


        def getRuleIndex(self):
            return EnquestesParser.RULE_root




    def root(self):

        localctx = EnquestesParser.RootContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_root)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 11 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 10
                self.expr()
                self.state = 13 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==EnquestesParser.ID):
                    break

            self.state = 15
            self.match(EnquestesParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ExprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def preg(self):
            return self.getTypedRuleContext(EnquestesParser.PregContext,0)


        def getRuleIndex(self):
            return EnquestesParser.RULE_expr




    def expr(self):

        localctx = EnquestesParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 17
            self.preg()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class PregContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(EnquestesParser.ID, 0)

        def TEXT(self):
            return self.getToken(EnquestesParser.TEXT, 0)

        def getRuleIndex(self):
            return EnquestesParser.RULE_preg




    def preg(self):

        localctx = EnquestesParser.PregContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_preg)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 19
            self.match(EnquestesParser.ID)
            self.state = 20
            self.match(EnquestesParser.T__0)
            self.state = 21
            self.match(EnquestesParser.TEXT)
            self.state = 22
            self.match(EnquestesParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class RespContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(EnquestesParser.ID, 0)

        def TEXT(self):
            return self.getToken(EnquestesParser.TEXT, 0)

        def opcn(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(EnquestesParser.OpcnContext)
            else:
                return self.getTypedRuleContext(EnquestesParser.OpcnContext,i)


        def getRuleIndex(self):
            return EnquestesParser.RULE_resp




    def resp(self):

        localctx = EnquestesParser.RespContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_resp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 24
            self.match(EnquestesParser.ID)
            self.state = 25
            self.match(EnquestesParser.T__2)
            self.state = 26
            self.match(EnquestesParser.TEXT)
            self.state = 28 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 27
                self.opcn()
                self.state = 30 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==EnquestesParser.NUM):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class OpcnContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUM(self):
            return self.getToken(EnquestesParser.NUM, 0)

        def TEXT(self):
            return self.getToken(EnquestesParser.TEXT, 0)

        def getRuleIndex(self):
            return EnquestesParser.RULE_opcn




    def opcn(self):

        localctx = EnquestesParser.OpcnContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_opcn)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 32
            self.match(EnquestesParser.NUM)
            self.state = 33
            self.match(EnquestesParser.T__3)
            self.state = 34
            self.match(EnquestesParser.TEXT)
            self.state = 35
            self.match(EnquestesParser.T__4)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





