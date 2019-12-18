grammar Enquestes;

root : expr+ EOF;

expr : preg | resp;

preg : ID ': PREGUNTA' TEXT '?';

resp : ID ': RESPOSTA' TEXT opcn+;
opcn : NUM ':' TEXT ';'; 

TEXT : [a-zA-Z\u0080-\u00FF ]+;
NUM  : [0-9]+;
ID	 : [a-zA-Z0-9]+;
WS   : [ \n]+ -> skip;