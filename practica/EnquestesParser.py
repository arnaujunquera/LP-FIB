# Generated from Enquestes.g by ANTLR 4.7.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\25")
        buf.write("c\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\3\2\6\2\26\n\2\r\2\16\2\27\3\2\3")
        buf.write("\2\3\2\3\3\3\3\3\3\3\3\3\3\5\3\"\n\3\3\4\3\4\3\4\3\4\6")
        buf.write("\4(\n\4\r\4\16\4)\3\4\3\4\3\5\3\5\3\5\3\5\6\5\62\n\5\r")
        buf.write("\5\16\5\63\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7")
        buf.write("\3\7\3\7\6\7C\n\7\r\7\16\7D\3\7\3\7\3\b\3\b\3\b\3\b\7")
        buf.write("\bM\n\b\f\b\16\bP\13\b\3\t\3\t\3\t\6\tU\n\t\r\t\16\tV")
        buf.write("\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\5\na\n\n\3\n\2\2\13\2")
        buf.write("\4\6\b\n\f\16\20\22\2\2\2d\2\25\3\2\2\2\4!\3\2\2\2\6#")
        buf.write("\3\2\2\2\b-\3\2\2\2\n\65\3\2\2\2\f<\3\2\2\2\16H\3\2\2")
        buf.write("\2\20Q\3\2\2\2\22Z\3\2\2\2\24\26\5\4\3\2\25\24\3\2\2\2")
        buf.write("\26\27\3\2\2\2\27\25\3\2\2\2\27\30\3\2\2\2\30\31\3\2\2")
        buf.write("\2\31\32\7\21\2\2\32\33\7\2\2\3\33\3\3\2\2\2\34\"\5\6")
        buf.write("\4\2\35\"\5\b\5\2\36\"\5\n\6\2\37\"\5\f\7\2 \"\5\16\b")
        buf.write("\2!\34\3\2\2\2!\35\3\2\2\2!\36\3\2\2\2!\37\3\2\2\2! \3")
        buf.write("\2\2\2\"\5\3\2\2\2#$\7\24\2\2$%\7\3\2\2%\'\7\4\2\2&(\7")
        buf.write("\23\2\2\'&\3\2\2\2()\3\2\2\2)\'\3\2\2\2)*\3\2\2\2*+\3")
        buf.write("\2\2\2+,\7\5\2\2,\7\3\2\2\2-.\7\24\2\2./\7\3\2\2/\61\7")
        buf.write("\6\2\2\60\62\5\20\t\2\61\60\3\2\2\2\62\63\3\2\2\2\63\61")
        buf.write("\3\2\2\2\63\64\3\2\2\2\64\t\3\2\2\2\65\66\7\24\2\2\66")
        buf.write("\67\7\3\2\2\678\7\7\2\289\7\24\2\29:\7\b\2\2:;\7\24\2")
        buf.write("\2;\13\3\2\2\2<=\7\24\2\2=>\7\3\2\2>?\7\t\2\2?@\7\24\2")
        buf.write("\2@B\7\n\2\2AC\5\22\n\2BA\3\2\2\2CD\3\2\2\2DB\3\2\2\2")
        buf.write("DE\3\2\2\2EF\3\2\2\2FG\7\13\2\2G\r\3\2\2\2HI\7\23\2\2")
        buf.write("IJ\7\3\2\2JN\7\f\2\2KM\7\24\2\2LK\3\2\2\2MP\3\2\2\2NL")
        buf.write("\3\2\2\2NO\3\2\2\2O\17\3\2\2\2PN\3\2\2\2QR\7\22\2\2RT")
        buf.write("\7\3\2\2SU\7\23\2\2TS\3\2\2\2UV\3\2\2\2VT\3\2\2\2VW\3")
        buf.write("\2\2\2WX\3\2\2\2XY\7\r\2\2Y\21\3\2\2\2Z[\7\16\2\2[\\\7")
        buf.write("\22\2\2\\]\7\17\2\2]^\7\24\2\2^`\7\20\2\2_a\7\17\2\2`")
        buf.write("_\3\2\2\2`a\3\2\2\2a\23\3\2\2\2\n\27!)\63DNV`")
        return buf.getvalue()


class EnquestesParser ( Parser ):

    grammarFileName = "Enquestes.g"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "':'", "'PREGUNTA'", "'?'", "'RESPOSTA'", 
                     "'ITEM'", "'->'", "'ALTERNATIVA'", "'['", "']'", "'ENQUESTA'", 
                     "';'", "'('", "','", "')'", "'END'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "END", "NUM", 
                      "TXT", "ID", "WS" ]

    RULE_root = 0
    RULE_expr = 1
    RULE_preg = 2
    RULE_resp = 3
    RULE_item = 4
    RULE_altr = 5
    RULE_enqs = 6
    RULE_opc = 7
    RULE_alt = 8

    ruleNames =  [ "root", "expr", "preg", "resp", "item", "altr", "enqs", 
                   "opc", "alt" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    END=15
    NUM=16
    TXT=17
    ID=18
    WS=19

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class RootContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def END(self):
            return self.getToken(EnquestesParser.END, 0)

        def EOF(self):
            return self.getToken(EnquestesParser.EOF, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(EnquestesParser.ExprContext)
            else:
                return self.getTypedRuleContext(EnquestesParser.ExprContext,i)


        def getRuleIndex(self):
            return EnquestesParser.RULE_root

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRoot" ):
                return visitor.visitRoot(self)
            else:
                return visitor.visitChildren(self)




    def root(self):

        localctx = EnquestesParser.RootContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_root)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 19 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 18
                self.expr()
                self.state = 21 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==EnquestesParser.TXT or _la==EnquestesParser.ID):
                    break

            self.state = 23
            self.match(EnquestesParser.END)
            self.state = 24
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


        def resp(self):
            return self.getTypedRuleContext(EnquestesParser.RespContext,0)


        def item(self):
            return self.getTypedRuleContext(EnquestesParser.ItemContext,0)


        def altr(self):
            return self.getTypedRuleContext(EnquestesParser.AltrContext,0)


        def enqs(self):
            return self.getTypedRuleContext(EnquestesParser.EnqsContext,0)


        def getRuleIndex(self):
            return EnquestesParser.RULE_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)




    def expr(self):

        localctx = EnquestesParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_expr)
        try:
            self.state = 31
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 26
                self.preg()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 27
                self.resp()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 28
                self.item()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 29
                self.altr()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 30
                self.enqs()
                pass


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

        def TXT(self, i:int=None):
            if i is None:
                return self.getTokens(EnquestesParser.TXT)
            else:
                return self.getToken(EnquestesParser.TXT, i)

        def getRuleIndex(self):
            return EnquestesParser.RULE_preg

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPreg" ):
                return visitor.visitPreg(self)
            else:
                return visitor.visitChildren(self)




    def preg(self):

        localctx = EnquestesParser.PregContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_preg)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 33
            self.match(EnquestesParser.ID)
            self.state = 34
            self.match(EnquestesParser.T__0)
            self.state = 35
            self.match(EnquestesParser.T__1)
            self.state = 37 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 36
                self.match(EnquestesParser.TXT)
                self.state = 39 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==EnquestesParser.TXT):
                    break

            self.state = 41
            self.match(EnquestesParser.T__2)
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

        def opc(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(EnquestesParser.OpcContext)
            else:
                return self.getTypedRuleContext(EnquestesParser.OpcContext,i)


        def getRuleIndex(self):
            return EnquestesParser.RULE_resp

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitResp" ):
                return visitor.visitResp(self)
            else:
                return visitor.visitChildren(self)




    def resp(self):

        localctx = EnquestesParser.RespContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_resp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 43
            self.match(EnquestesParser.ID)
            self.state = 44
            self.match(EnquestesParser.T__0)
            self.state = 45
            self.match(EnquestesParser.T__3)
            self.state = 47 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 46
                self.opc()
                self.state = 49 
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

    class ItemContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(EnquestesParser.ID)
            else:
                return self.getToken(EnquestesParser.ID, i)

        def getRuleIndex(self):
            return EnquestesParser.RULE_item

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitItem" ):
                return visitor.visitItem(self)
            else:
                return visitor.visitChildren(self)




    def item(self):

        localctx = EnquestesParser.ItemContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_item)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 51
            self.match(EnquestesParser.ID)
            self.state = 52
            self.match(EnquestesParser.T__0)
            self.state = 53
            self.match(EnquestesParser.T__4)
            self.state = 54
            self.match(EnquestesParser.ID)
            self.state = 55
            self.match(EnquestesParser.T__5)
            self.state = 56
            self.match(EnquestesParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class AltrContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(EnquestesParser.ID)
            else:
                return self.getToken(EnquestesParser.ID, i)

        def alt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(EnquestesParser.AltContext)
            else:
                return self.getTypedRuleContext(EnquestesParser.AltContext,i)


        def getRuleIndex(self):
            return EnquestesParser.RULE_altr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAltr" ):
                return visitor.visitAltr(self)
            else:
                return visitor.visitChildren(self)




    def altr(self):

        localctx = EnquestesParser.AltrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_altr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 58
            self.match(EnquestesParser.ID)
            self.state = 59
            self.match(EnquestesParser.T__0)
            self.state = 60
            self.match(EnquestesParser.T__6)
            self.state = 61
            self.match(EnquestesParser.ID)
            self.state = 62
            self.match(EnquestesParser.T__7)
            self.state = 64 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 63
                self.alt()
                self.state = 66 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==EnquestesParser.T__11):
                    break

            self.state = 68
            self.match(EnquestesParser.T__8)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class EnqsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TXT(self):
            return self.getToken(EnquestesParser.TXT, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(EnquestesParser.ID)
            else:
                return self.getToken(EnquestesParser.ID, i)

        def getRuleIndex(self):
            return EnquestesParser.RULE_enqs

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEnqs" ):
                return visitor.visitEnqs(self)
            else:
                return visitor.visitChildren(self)




    def enqs(self):

        localctx = EnquestesParser.EnqsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_enqs)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 70
            self.match(EnquestesParser.TXT)
            self.state = 71
            self.match(EnquestesParser.T__0)
            self.state = 72
            self.match(EnquestesParser.T__9)
            self.state = 76
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 73
                    self.match(EnquestesParser.ID) 
                self.state = 78
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class OpcContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUM(self):
            return self.getToken(EnquestesParser.NUM, 0)

        def TXT(self, i:int=None):
            if i is None:
                return self.getTokens(EnquestesParser.TXT)
            else:
                return self.getToken(EnquestesParser.TXT, i)

        def getRuleIndex(self):
            return EnquestesParser.RULE_opc

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOpc" ):
                return visitor.visitOpc(self)
            else:
                return visitor.visitChildren(self)




    def opc(self):

        localctx = EnquestesParser.OpcContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_opc)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 79
            self.match(EnquestesParser.NUM)
            self.state = 80
            self.match(EnquestesParser.T__0)
            self.state = 82 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 81
                self.match(EnquestesParser.TXT)
                self.state = 84 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==EnquestesParser.TXT):
                    break

            self.state = 86
            self.match(EnquestesParser.T__10)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class AltContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUM(self):
            return self.getToken(EnquestesParser.NUM, 0)

        def ID(self):
            return self.getToken(EnquestesParser.ID, 0)

        def getRuleIndex(self):
            return EnquestesParser.RULE_alt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAlt" ):
                return visitor.visitAlt(self)
            else:
                return visitor.visitChildren(self)




    def alt(self):

        localctx = EnquestesParser.AltContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_alt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 88
            self.match(EnquestesParser.T__11)
            self.state = 89
            self.match(EnquestesParser.NUM)
            self.state = 90
            self.match(EnquestesParser.T__12)
            self.state = 91
            self.match(EnquestesParser.ID)
            self.state = 92
            self.match(EnquestesParser.T__13)
            self.state = 94
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==EnquestesParser.T__12:
                self.state = 93
                self.match(EnquestesParser.T__12)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





