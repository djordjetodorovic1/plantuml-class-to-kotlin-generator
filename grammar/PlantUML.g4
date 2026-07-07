grammar PlantUML;
// PlantUML gramatika za dijagrame klasa

diagram: STARTUML element* ENDUML EOF;

element
    : classDecl
    | interfaceDecl
    | enumDecl
    | relation
    ;

classDecl: ABSTRACT? CLASS IDENTIFIER classBody?;

interfaceDecl: INTERFACE IDENTIFIER classBody?;

enumDecl: ENUM IDENTIFIER LBRACE IDENTIFIER (COMMA? IDENTIFIER)* RBRACE;

classBody: LBRACE classMember* RBRACE;

classMember
    : attribute
    | method
    ;

// Atributi i metode

visibility
    : PLUS   // public
    | MINUS  // private
    | HASH   // protected
    | TILDE  // package/internal
    ;

attribute: visibility? STATIC? IDENTIFIER COLON type;

method: visibility? STATIC? ABSTRACT? IDENTIFIER LPAREN paramList? RPAREN (COLON type)?;

paramList: param (COMMA param)*;

param: IDENTIFIER COLON type;

type: IDENTIFIER (LBRACK RBRACK)?;

// Relacije izmedju klasa

relation: IDENTIFIER MULTIPLICITY? relationOp MULTIPLICITY? IDENTIFIER (COLON label)?;

relationOp
    : EXTENDS_ARROW        // nasljedjivanje (--|> ili <|--)
    | IMPLEMENTS_ARROW     // implementacija (..|> ili <|..)
    | COMPOSITION_ARROW    // kompozicija    (*-- ili --*) 
    | AGGREGATION_ARROW    // agregacija     (o-- ili --o)
    | DEPENDENCY_ARROW     // zavisnost      (..> ili <..)
    | ASSOCIATION_ARROW    // asocijacija    (--> ili <-- ili --)
    ;

label: (IDENTIFIER | STRING | NUMBER)+;

// Kljucne rijeci i simboli

STARTUML   : '@startuml' ;
ENDUML     : '@enduml' ;

CLASS      : 'class' ;
INTERFACE  : 'interface' ;
ENUM       : 'enum' ;
ABSTRACT   : 'abstract' ;
STATIC     : 'static' ;

EXTENDS_ARROW     : '--|>' | '<|--' ;
IMPLEMENTS_ARROW  : '..|>' | '<|..' ;
COMPOSITION_ARROW : '*--'  | '--*'  ;
AGGREGATION_ARROW : 'o--'  | '--o'  ;
DEPENDENCY_ARROW  : '..>'  | '<..'  ;
ASSOCIATION_ARROW : '-->'  | '<--'  | '--' ;

PLUS   : '+' ;
MINUS  : '-' ;
HASH   : '#' ;
TILDE  : '~' ;

LBRACE : '{' ;
RBRACE : '}' ;
LPAREN : '(' ;
RPAREN : ')' ;
LBRACK : '[' ;
RBRACK : ']' ;
COLON  : ':' ;
COMMA  : ',' ;

IDENTIFIER : [a-zA-Z_][a-zA-Z0-9_]*;
fragment DIGIT  : [0-9] ;
fragment DIGITS : DIGIT+ ;
fragment MULT_VALUE
    : DIGITS '..' DIGITS
    | DIGITS '..' '*'
    | DIGITS
    | '*'            
    | 'many'
    ;
MULTIPLICITY : '"' MULT_VALUE '"';
STRING : '"' ( ~["\r\n] )* '"';
NUMBER : [0-9]+;

LINE_COMMENT  : '\'' ~[\r\n]* -> skip;
BLOCK_COMMENT : '/\'' .*? '\'/' -> skip;
WS : [ \t\r\n]+ -> skip;