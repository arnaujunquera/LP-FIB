grammar Expr;

root : expr EOF;

expr : expr POW expr | expr MUL expr | expr (MES|RES) expr | NUM;

NUM : [0-9]+;
MES : '+';
RES : '-';
MUL : '*';
POW : '**';
WS : [ \n]+ -> skip;
