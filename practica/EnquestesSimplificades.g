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
  ID ': PREGUNTA' textpreg;

resp:
  ID ': RESPOSTA' textresp;

item:
  ID ': ITEM' textitem;

altr:
  ID ': ALTERNATIVA' textaltr;

enqs:
  ID ': ENQUESTA' textenqs;




textpreg:
  TXT '?';

textresp:
  opc+;

textitem:
  ID'->'ID;

textaltr:
  ID '[' alts ']';

textenqs:
  ID+;




opc:
  NUM ':' TXT ';';

alts:
  alt (',' alt)*;

alt:
  '(' NUM ',' ID ')';



END : 'END';
NUM : [0-9]+;
ID  : [a-zA-Z][a-zA-Z0-9]* ;
TXT : [0-9a-zA-Z\u0080-\u00FF ]+;
WS  : [ \n]+ -> skip;
