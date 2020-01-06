# Generated from Enquestes.g by ANTLR 4.7.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .EnquestesParser import EnquestesParser
else:
    from EnquestesParser import EnquestesParser

# This class defines a complete generic visitor for a parse tree produced by EnquestesParser.

class EnquestesVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by EnquestesParser#root.
    def visitRoot(self, ctx:EnquestesParser.RootContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EnquestesParser#preg.
    def visitPreg(self, ctx:EnquestesParser.PregContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EnquestesParser#resp.
    def visitResp(self, ctx:EnquestesParser.RespContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EnquestesParser#item.
    def visitItem(self, ctx:EnquestesParser.ItemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EnquestesParser#altr.
    def visitAltr(self, ctx:EnquestesParser.AltrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EnquestesParser#enqs.
    def visitEnqs(self, ctx:EnquestesParser.EnqsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EnquestesParser#opc.
    def visitOpc(self, ctx:EnquestesParser.OpcContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EnquestesParser#alt.
    def visitAlt(self, ctx:EnquestesParser.AltContext):
        return self.visitChildren(ctx)



del EnquestesParser