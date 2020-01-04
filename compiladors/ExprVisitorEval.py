from antlr4 import *
if __name__ is not None and "." in __name__:
    from .ExprParser import ExprParser
else:
    from ExprParser import ExprParser

class ExprVisitorEval(ParseTreeVisitor):
    def visitRoot(self, ctx:ExprParser.RootContext):
        n = next(ctx.getChildren())
        print(self.visit(n))
    def visitExpr(self, ctx:ExprParser.ExprContext):
        if ctx.getChildCount() == 1:
            n = next(ctx.getChildren())
            return int(n.getText())
        elif ctx.getChildCount() == 3:
            g = ctx.getChildren()
            l = [next(g) for i in range(3)]
            if (ExprParser.symbolicNames[l[1].getSymbol().type] == "MES"):
                return self.visit(l[0]) + self.visit(l[2])
            elif (ExprParser.symbolicNames[l[1].getSymbol().type] == "RES"):
                return self.visit(l[0]) - self.visit(l[2])
            elif (ExprParser.symbolicNames[l[1].getSymbol().type] == "MUL"):
                return self.visit(l[0]) * self.visit(l[2])
            elif (ExprParser.symbolicNames[l[1].getSymbol().type] == "DIV"):
                return self.visit(l[0]) / self.visit(l[2])
            elif (ExprParser.symbolicNames[l[1].getSymbol().type] == "POW"):
                return self.visit(l[0]) ** self.visit(l[2])
# del ExprParser
