from antlr4 import *
if __name__ is not None and "." in __name__:
    from .ExprParser import ExprParser
else:
    from ExprParser import ExprParser

class ExprVisitorTree(ParseTreeVisitor):
    def __init__(self):
        self.nivell = 0  # nivell de profunditat del node
    def visitExpr(self, ctx:ExprParser.ExprContext):
        if ctx.getChildCount() == 1:
            n = next(ctx.getChildren())
            print(" " * self.nivell + \
                  ExprParser.symbolicNames[n.getSymbol().type] + \
                  '(' +n.getText() + ')')
            self.nivell -= 1
        elif ctx.getChildCount() == 3:
            l = [i for i in ctx.getChildren()]
            print(' ' * self.nivell + ExprParser.symbolicNames[l[1].getSymbol().type] + "(" + l[1].getText() + ")")
            self.nivell += 1
            self.visit(ctx.expr(0))
            self.nivell += 1
            self.visit(ctx.expr(1))
            self.nivell -= 1
#del ExprParser
