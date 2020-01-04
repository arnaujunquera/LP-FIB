grammar Enquestes;

root:
  expr+ END EOF;

expr:
  preg |
  resp |
  item |
  altr |
  enqs;




preg:
  ide ': PREGUNTA' textpreg;

resp:
  ide ': RESPOSTA' textresp;

item:
  ide ': ITEM' textitem;

altr:
  ide ': ALTERNATIVA' textaltr;

enqs:
  ide ': ENQUESTA' textenqs;




textpreg:
  text+ '?';

textresp:
  opc+;

textitem:
  ide '->' ide;

textaltr:
  ide '[' alts ']';

textenqs:
  ide+;




ide:
  char+;

text:
  ichar+;

opc:
  NUM+ ':' text+ ';';

alts:
  alt (',' alt)*;

alt:
  '(' NUM+ ',' ide ')';





char:
  LET |
  NUM;

ichar:
  LET |
  ACC |
  NUM;


END : 'END';
NUM : [0-9];
LET : [a-zA-Z];
ACC : [\u0080-\u00FF];
WS  : [ \n]+ -> skip;
