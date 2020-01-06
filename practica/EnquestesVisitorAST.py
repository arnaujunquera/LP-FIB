import networkx as nx
import matplotlib.pyplot as plt

# Generated from Enquestes.g by ANTLR 4.7.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .EnquestesParser import EnquestesParser
else:
    from EnquestesParser import EnquestesParser

# This class defines a complete generic visitor for a parse tree produced by EnquestesParser.

class EnquestesVisitorAST(ParseTreeVisitor):
    def __init__(self):
        self.graf = nx.Graph()

    # Visit a parse tree produced by EnquestesParser#root.
    def visitRoot(self, ctx:EnquestesParser.RootContext):
        g = ctx.getChildren()
        l = [next(g) for i in range(ctx.getChildCount())]
        for i in range(len(l)):
            if (l[i].getText() == 'END'):
                print('END')
            else:
                print(self.visit(l[i]))


    # Visit a parse tree produced by EnquestesParser#preg.
    def visitPreg(self, ctx:EnquestesParser.PregContext):
        return "PREGUNTA"


    # Visit a parse tree produced by EnquestesParser#resp.
    def visitResp(self, ctx:EnquestesParser.RespContext):
        return "RESPOSTA"


    # Visit a parse tree produced by EnquestesParser#item.
    def visitItem(self, ctx:EnquestesParser.ItemContext):
        return "ITEM"


    # Visit a parse tree produced by EnquestesParser#altr.
    def visitAltr(self, ctx:EnquestesParser.AltrContext):
        return "ALTERNATIVA"


    # Visit a parse tree produced by EnquestesParser#enqs.
    def visitEnqs(self, ctx:EnquestesParser.EnqsContext):
        return "ENQUESTA"


    # Visit a parse tree produced by EnquestesParser#opc.
    def visitOpc(self, ctx:EnquestesParser.OpcContext):
        return "opcio"


    # Visit a parse tree produced by EnquestesParser#alt.
    def visitAlt(self, ctx:EnquestesParser.AltContext):
        return "alternativa"



del EnquestesParser
