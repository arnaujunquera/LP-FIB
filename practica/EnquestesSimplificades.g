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
  IDE ': PREGUNTA' textpreg;

resp:
  IDE ': RESPOSTA' textresp;

item:
  IDE ': ITEM' textitem;

altr:
  IDE ': ALTERNATIVA' textaltr;

enqs:
  IDE ': ENQUESTA' textenqs;




textpreg:
  TXT '?';

textresp:
  opc+;

textitem:
  IDE'->'IDE;

textaltr:
  IDE '[' alts ']';

textenqs:
  IDE+;




opc:
  NUM ':' TXT ';';

alts:
  alt (',' alt)*;

alt:
  '(' NUM ',' IDE ')';




END : 'END';
NUM : [0-9]+;
IDE : [0-9a-zA-Z]+;
TXT : [0-9a-zA-Z\u0080-\u00FF ]+;
WS  : [ \n]+ -> skip;
