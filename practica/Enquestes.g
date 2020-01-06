grammar Enquestes;

root:
  (preg | resp | item | altr | enqs)+ END EOF;


preg:
  ID ':' 'PREGUNTA' TXT+ '?';

resp:
  ID ':' 'RESPOSTA' opc+;

item:
  ID ':' 'ITEM' ID '->' ID;

altr:
  ID ':' 'ALTERNATIVA' ID '[' alt+ ']';

enqs:
  TXT ':' 'ENQUESTA' ID*;



opc:
  NUM':' TXT+ ';';

alt:
  '(' NUM ',' ID ')' ','?;



END : 'END' ;
NUM : [0-9]+ ;
TXT : [a-zA-Z\u0080-\u00FF]+ ;
ID : [a-zA-Z][a-zA-Z0-9]* ;
WS : [ \n] -> skip ;
