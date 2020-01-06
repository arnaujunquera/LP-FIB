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
                self.graph.add_node('END')
                nx.write_gpickle(self.graph, "graph.gpickle")
            else:
                self.visit(l[i])


    # Visit a parse tree produced by EnquestesParser#preg.
    def visitPreg(self, ctx:EnquestesParser.PregContext):
        n = next(ctx.getChildren())
        self.graph.add_node(n.getText())


    # Visit a parse tree produced by EnquestesParser#resp.
    def visitResp(self, ctx:EnquestesParser.RespContext):
        n = next(ctx.getChildren())
        self.graph.add_node(n.getText())


    # Visit a parse tree produced by EnquestesParser#item.
    def visitItem(self, ctx:EnquestesParser.ItemContext):
        # n = next(ctx.getChildren())
        # self.graph.add_node(n.getText())
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EnquestesParser#altr.
    def visitAltr(self, ctx:EnquestesParser.AltrContext):
        # n = next(ctx.getChildren())
        # self.graph.add_node(n.getText())
        return self.visitChildren(ctx)

    # Visit a parse tree produced by EnquestesParser#enqs.
    def visitEnqs(self, ctx:EnquestesParser.EnqsContext):
        n = next(ctx.getChildren())
        self.graph.add_node(n.getText())


    # Visit a parse tree produced by EnquestesParser#opc.
    def visitOpc(self, ctx:EnquestesParser.OpcContext):
        # n = next(ctx.getChildren())
        # self.graph.add_node(n.getText())
        return self.visitChildren(ctx)

    # Visit a parse tree produced by EnquestesParser#alt.
    def visitAlt(self, ctx:EnquestesParser.AltContext):
        # n = next(ctx.getChildren())
        # self.graph.add_node(n.getText())
        return self.visitChildren(ctx)


del EnquestesParser
