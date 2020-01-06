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
        self.graph = nx.Graph()

    # Visit a parse tree produced by EnquestesParser#root.
    def visitRoot(self, ctx:EnquestesParser.RootContext):
        g = ctx.getChildren()
        l = [next(g) for i in range(ctx.getChildCount())]
        self.graph = nx.Graph()
        for i in range(len(l)):
            if (l[i].getText() == 'END'):
                print('END')
                nx.write_gpickle(self.graph, "graph.gpickle")
            else:
                self.visit(l[i])


    # Visit a parse tree produced by EnquestesParser#preg.
    def visitPreg(self, ctx:EnquestesParser.PregContext):
        n = next(ctx.getChildren())
        print(n)
        self.graph.add_node(n.getText())
        print("PREGUNTA")


    # Visit a parse tree produced by EnquestesParser#resp.
    def visitResp(self, ctx:EnquestesParser.RespContext):
        # self.graph.add_node(n.getText())
        print("RESPOSTA")


    # Visit a parse tree produced by EnquestesParser#item.
    def visitItem(self, ctx:EnquestesParser.ItemContext):
        # self.graph.add_node(n.getText())
        print("ITEM")


    # Visit a parse tree produced by EnquestesParser#altr.
    def visitAltr(self, ctx:EnquestesParser.AltrContext):
        # self.graph.add_node(n.getText())
        print("ALTERNATIVA")


    # Visit a parse tree produced by EnquestesParser#enqs.
    def visitEnqs(self, ctx:EnquestesParser.EnqsContext):
        # self.graph.add_node(n.getText())
        print("ENQUESTA")


    # Visit a parse tree produced by EnquestesParser#opc.
    def visitOpc(self, ctx:EnquestesParser.OpcContext):
        # self.graph.add_node(n.getText())
        print("opcio")


    # Visit a parse tree produced by EnquestesParser#alt.
    def visitAlt(self, ctx:EnquestesParser.AltContext):
        # self.graph.add_node(n.getText())
        print("alternativa")



del EnquestesParser
