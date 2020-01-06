# Generated from Enquestes.g by ANTLR 4.7.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\25")
        buf.write("^\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\3\2\3\2\3\2\3\2\3\2\6\2\30\n\2\r\2\16\2\31")
        buf.write("\3\2\3\2\3\2\3\3\3\3\3\3\3\3\6\3#\n\3\r\3\16\3$\3\3\3")
        buf.write("\3\3\4\3\4\3\4\3\4\6\4-\n\4\r\4\16\4.\3\5\3\5\3\5\3\5")
        buf.write("\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\6\6>\n\6\r\6\16\6")
        buf.write("?\3\6\3\6\3\7\3\7\3\7\3\7\7\7H\n\7\f\7\16\7K\13\7\3\b")
        buf.write("\3\b\3\b\6\bP\n\b\r\b\16\bQ\3\b\3\b\3\t\3\t\3\t\3\t\3")
        buf.write("\t\3\t\5\t\\\n\t\3\t\2\2\n\2\4\6\b\n\f\16\20\2\2\2`\2")
        buf.write("\27\3\2\2\2\4\36\3\2\2\2\6(\3\2\2\2\b\60\3\2\2\2\n\67")
        buf.write("\3\2\2\2\fC\3\2\2\2\16L\3\2\2\2\20U\3\2\2\2\22\30\5\4")
        buf.write("\3\2\23\30\5\6\4\2\24\30\5\b\5\2\25\30\5\n\6\2\26\30\5")
        buf.write("\f\7\2\27\22\3\2\2\2\27\23\3\2\2\2\27\24\3\2\2\2\27\25")
        buf.write("\3\2\2\2\27\26\3\2\2\2\30\31\3\2\2\2\31\27\3\2\2\2\31")
        buf.write("\32\3\2\2\2\32\33\3\2\2\2\33\34\7\21\2\2\34\35\7\2\2\3")
        buf.write("\35\3\3\2\2\2\36\37\7\24\2\2\37 \7\3\2\2 \"\7\4\2\2!#")
        buf.write("\7\23\2\2\"!\3\2\2\2#$\3\2\2\2$\"\3\2\2\2$%\3\2\2\2%&")
        buf.write("\3\2\2\2&\'\7\5\2\2\'\5\3\2\2\2()\7\24\2\2)*\7\3\2\2*")
        buf.write(",\7\6\2\2+-\5\16\b\2,+\3\2\2\2-.\3\2\2\2.,\3\2\2\2./\3")
        buf.write("\2\2\2/\7\3\2\2\2\60\61\7\24\2\2\61\62\7\3\2\2\62\63\7")
        buf.write("\7\2\2\63\64\7\24\2\2\64\65\7\b\2\2\65\66\7\24\2\2\66")
        buf.write("\t\3\2\2\2\678\7\24\2\289\7\3\2\29:\7\t\2\2:;\7\24\2\2")
        buf.write(";=\7\n\2\2<>\5\20\t\2=<\3\2\2\2>?\3\2\2\2?=\3\2\2\2?@")
        buf.write("\3\2\2\2@A\3\2\2\2AB\7\13\2\2B\13\3\2\2\2CD\7\23\2\2D")
        buf.write("E\7\3\2\2EI\7\f\2\2FH\7\24\2\2GF\3\2\2\2HK\3\2\2\2IG\3")
        buf.write("\2\2\2IJ\3\2\2\2J\r\3\2\2\2KI\3\2\2\2LM\7\22\2\2MO\7\3")
        buf.write("\2\2NP\7\23\2\2ON\3\2\2\2PQ\3\2\2\2QO\3\2\2\2QR\3\2\2")
        buf.write("\2RS\3\2\2\2ST\7\r\2\2T\17\3\2\2\2UV\7\16\2\2VW\7\22\2")
        buf.write("\2WX\7\17\2\2XY\7\24\2\2Y[\7\20\2\2Z\\\7\17\2\2[Z\3\2")
        buf.write("\2\2[\\\3\2\2\2\\\21\3\2\2\2\n\27\31$.?IQ[")
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
    RULE_preg = 1
    RULE_resp = 2
    RULE_item = 3
    RULE_altr = 4
    RULE_enqs = 5
    RULE_opc = 6
    RULE_alt = 7

    ruleNames =  [ "root", "preg", "resp", "item", "altr", "enqs", "opc", 
                   "alt" ]

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

        def preg(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(EnquestesParser.PregContext)
            else:
                return self.getTypedRuleContext(EnquestesParser.PregContext,i)


        def resp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(EnquestesParser.RespContext)
            else:
                return self.getTypedRuleContext(EnquestesParser.RespContext,i)


        def item(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(EnquestesParser.ItemContext)
            else:
                return self.getTypedRuleContext(EnquestesParser.ItemContext,i)


        def altr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(EnquestesParser.AltrContext)
            else:
                return self.getTypedRuleContext(EnquestesParser.AltrContext,i)


        def enqs(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(EnquestesParser.EnqsContext)
            else:
                return self.getTypedRuleContext(EnquestesParser.EnqsContext,i)


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
            self.state = 21 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 21
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
                if la_ == 1:
                    self.state = 16
                    self.preg()
                    pass

                elif la_ == 2:
                    self.state = 17
                    self.resp()
                    pass

                elif la_ == 3:
                    self.state = 18
                    self.item()
                    pass

                elif la_ == 4:
                    self.state = 19
                    self.altr()
                    pass

                elif la_ == 5:
                    self.state = 20
                    self.enqs()
                    pass


                self.state = 23 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==EnquestesParser.TXT or _la==EnquestesParser.ID):
                    break

            self.state = 25
            self.match(EnquestesParser.END)
            self.state = 26
            self.match(EnquestesParser.EOF)
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
        self.enterRule(localctx, 2, self.RULE_preg)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 28
            self.match(EnquestesParser.ID)
            self.state = 29
            self.match(EnquestesParser.T__0)
            self.state = 30
            self.match(EnquestesParser.T__1)
            self.state = 32 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 31
                self.match(EnquestesParser.TXT)
                self.state = 34 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==EnquestesParser.TXT):
                    break

            self.state = 36
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
        self.enterRule(localctx, 4, self.RULE_resp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 38
            self.match(EnquestesParser.ID)
            self.state = 39
            self.match(EnquestesParser.T__0)
            self.state = 40
            self.match(EnquestesParser.T__3)
            self.state = 42 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 41
                self.opc()
                self.state = 44 
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
        self.enterRule(localctx, 6, self.RULE_item)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 46
            self.match(EnquestesParser.ID)
            self.state = 47
            self.match(EnquestesParser.T__0)
            self.state = 48
            self.match(EnquestesParser.T__4)
            self.state = 49
            self.match(EnquestesParser.ID)
            self.state = 50
            self.match(EnquestesParser.T__5)
            self.state = 51
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
        self.enterRule(localctx, 8, self.RULE_altr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 53
            self.match(EnquestesParser.ID)
            self.state = 54
            self.match(EnquestesParser.T__0)
            self.state = 55
            self.match(EnquestesParser.T__6)
            self.state = 56
            self.match(EnquestesParser.ID)
            self.state = 57
            self.match(EnquestesParser.T__7)
            self.state = 59 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 58
                self.alt()
                self.state = 61 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==EnquestesParser.T__11):
                    break

            self.state = 63
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
        self.enterRule(localctx, 10, self.RULE_enqs)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 65
            self.match(EnquestesParser.TXT)
            self.state = 66
            self.match(EnquestesParser.T__0)
            self.state = 67
            self.match(EnquestesParser.T__9)
            self.state = 71
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 68
                    self.match(EnquestesParser.ID) 
                self.state = 73
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
        self.enterRule(localctx, 12, self.RULE_opc)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 74
            self.match(EnquestesParser.NUM)
            self.state = 75
            self.match(EnquestesParser.T__0)
            self.state = 77 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 76
                self.match(EnquestesParser.TXT)
                self.state = 79 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==EnquestesParser.TXT):
                    break

            self.state = 81
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
        self.enterRule(localctx, 14, self.RULE_alt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 83
            self.match(EnquestesParser.T__11)
            self.state = 84
            self.match(EnquestesParser.NUM)
            self.state = 85
            self.match(EnquestesParser.T__12)
            self.state = 86
            self.match(EnquestesParser.ID)
            self.state = 87
            self.match(EnquestesParser.T__13)
            self.state = 89
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==EnquestesParser.T__12:
                self.state = 88
                self.match(EnquestesParser.T__12)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





