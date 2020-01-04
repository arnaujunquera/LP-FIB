grammar Expr;

root : stat+ EOF;

stat : ID ASSIG expr
    | WR expr
    ;

expr : <assoc=right> expr POW expr
    | expr (MUL|DIV) expr
    | expr (MES|RES) expr
    | NUM
    | ID;

ID    : [a-z]+
ASSIG : '='

NUM : [0-9]+;

MES : '+';
RES : '-';
MUL : '*';
DIV : '/';
POW : '**';


WS : [ \n]+ -> skip;
