# Generated from ../grammar/PlantUML.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,32,158,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,1,0,1,0,5,0,35,8,0,10,0,12,0,38,9,0,1,0,1,0,
        1,0,1,1,1,1,1,1,1,1,3,1,47,8,1,1,2,3,2,50,8,2,1,2,1,2,1,2,3,2,55,
        8,2,1,3,1,3,1,3,3,3,60,8,3,1,4,1,4,1,4,1,4,1,4,3,4,67,8,4,1,4,5,
        4,70,8,4,10,4,12,4,73,9,4,1,4,1,4,1,5,1,5,5,5,79,8,5,10,5,12,5,82,
        9,5,1,5,1,5,1,6,1,6,3,6,88,8,6,1,7,1,7,1,8,3,8,93,8,8,1,8,3,8,96,
        8,8,1,8,1,8,1,8,1,8,1,9,3,9,103,8,9,1,9,3,9,106,8,9,1,9,3,9,109,
        8,9,1,9,1,9,1,9,3,9,114,8,9,1,9,1,9,1,9,3,9,119,8,9,1,10,1,10,1,
        10,5,10,124,8,10,10,10,12,10,127,9,10,1,11,1,11,1,11,1,11,1,12,1,
        12,1,12,3,12,136,8,12,1,13,1,13,3,13,140,8,13,1,13,1,13,3,13,144,
        8,13,1,13,1,13,1,13,3,13,149,8,13,1,14,1,14,1,15,4,15,154,8,15,11,
        15,12,15,155,1,15,0,0,16,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,
        30,0,3,1,0,14,17,1,0,8,13,2,0,26,26,28,29,165,0,32,1,0,0,0,2,46,
        1,0,0,0,4,49,1,0,0,0,6,56,1,0,0,0,8,61,1,0,0,0,10,76,1,0,0,0,12,
        87,1,0,0,0,14,89,1,0,0,0,16,92,1,0,0,0,18,102,1,0,0,0,20,120,1,0,
        0,0,22,128,1,0,0,0,24,132,1,0,0,0,26,137,1,0,0,0,28,150,1,0,0,0,
        30,153,1,0,0,0,32,36,5,1,0,0,33,35,3,2,1,0,34,33,1,0,0,0,35,38,1,
        0,0,0,36,34,1,0,0,0,36,37,1,0,0,0,37,39,1,0,0,0,38,36,1,0,0,0,39,
        40,5,2,0,0,40,41,5,0,0,1,41,1,1,0,0,0,42,47,3,4,2,0,43,47,3,6,3,
        0,44,47,3,8,4,0,45,47,3,26,13,0,46,42,1,0,0,0,46,43,1,0,0,0,46,44,
        1,0,0,0,46,45,1,0,0,0,47,3,1,0,0,0,48,50,5,6,0,0,49,48,1,0,0,0,49,
        50,1,0,0,0,50,51,1,0,0,0,51,52,5,3,0,0,52,54,5,26,0,0,53,55,3,10,
        5,0,54,53,1,0,0,0,54,55,1,0,0,0,55,5,1,0,0,0,56,57,5,4,0,0,57,59,
        5,26,0,0,58,60,3,10,5,0,59,58,1,0,0,0,59,60,1,0,0,0,60,7,1,0,0,0,
        61,62,5,5,0,0,62,63,5,26,0,0,63,64,5,18,0,0,64,71,5,26,0,0,65,67,
        5,25,0,0,66,65,1,0,0,0,66,67,1,0,0,0,67,68,1,0,0,0,68,70,5,26,0,
        0,69,66,1,0,0,0,70,73,1,0,0,0,71,69,1,0,0,0,71,72,1,0,0,0,72,74,
        1,0,0,0,73,71,1,0,0,0,74,75,5,19,0,0,75,9,1,0,0,0,76,80,5,18,0,0,
        77,79,3,12,6,0,78,77,1,0,0,0,79,82,1,0,0,0,80,78,1,0,0,0,80,81,1,
        0,0,0,81,83,1,0,0,0,82,80,1,0,0,0,83,84,5,19,0,0,84,11,1,0,0,0,85,
        88,3,16,8,0,86,88,3,18,9,0,87,85,1,0,0,0,87,86,1,0,0,0,88,13,1,0,
        0,0,89,90,7,0,0,0,90,15,1,0,0,0,91,93,3,14,7,0,92,91,1,0,0,0,92,
        93,1,0,0,0,93,95,1,0,0,0,94,96,5,7,0,0,95,94,1,0,0,0,95,96,1,0,0,
        0,96,97,1,0,0,0,97,98,5,26,0,0,98,99,5,24,0,0,99,100,3,24,12,0,100,
        17,1,0,0,0,101,103,3,14,7,0,102,101,1,0,0,0,102,103,1,0,0,0,103,
        105,1,0,0,0,104,106,5,7,0,0,105,104,1,0,0,0,105,106,1,0,0,0,106,
        108,1,0,0,0,107,109,5,6,0,0,108,107,1,0,0,0,108,109,1,0,0,0,109,
        110,1,0,0,0,110,111,5,26,0,0,111,113,5,20,0,0,112,114,3,20,10,0,
        113,112,1,0,0,0,113,114,1,0,0,0,114,115,1,0,0,0,115,118,5,21,0,0,
        116,117,5,24,0,0,117,119,3,24,12,0,118,116,1,0,0,0,118,119,1,0,0,
        0,119,19,1,0,0,0,120,125,3,22,11,0,121,122,5,25,0,0,122,124,3,22,
        11,0,123,121,1,0,0,0,124,127,1,0,0,0,125,123,1,0,0,0,125,126,1,0,
        0,0,126,21,1,0,0,0,127,125,1,0,0,0,128,129,5,26,0,0,129,130,5,24,
        0,0,130,131,3,24,12,0,131,23,1,0,0,0,132,135,5,26,0,0,133,134,5,
        22,0,0,134,136,5,23,0,0,135,133,1,0,0,0,135,136,1,0,0,0,136,25,1,
        0,0,0,137,139,5,26,0,0,138,140,5,27,0,0,139,138,1,0,0,0,139,140,
        1,0,0,0,140,141,1,0,0,0,141,143,3,28,14,0,142,144,5,27,0,0,143,142,
        1,0,0,0,143,144,1,0,0,0,144,145,1,0,0,0,145,148,5,26,0,0,146,147,
        5,24,0,0,147,149,3,30,15,0,148,146,1,0,0,0,148,149,1,0,0,0,149,27,
        1,0,0,0,150,151,7,1,0,0,151,29,1,0,0,0,152,154,7,2,0,0,153,152,1,
        0,0,0,154,155,1,0,0,0,155,153,1,0,0,0,155,156,1,0,0,0,156,31,1,0,
        0,0,22,36,46,49,54,59,66,71,80,87,92,95,102,105,108,113,118,125,
        135,139,143,148,155
    ]

class PlantUMLParser ( Parser ):

    grammarFileName = "PlantUML.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'@startuml'", "'@enduml'", "'class'", 
                     "'interface'", "'enum'", "'abstract'", "'static'", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'+'", "'-'", "'#'", "'~'", 
                     "'{'", "'}'", "'('", "')'", "'['", "']'", "':'", "','" ]

    symbolicNames = [ "<INVALID>", "STARTUML", "ENDUML", "CLASS", "INTERFACE", 
                      "ENUM", "ABSTRACT", "STATIC", "EXTENDS_ARROW", "IMPLEMENTS_ARROW", 
                      "COMPOSITION_ARROW", "AGGREGATION_ARROW", "DEPENDENCY_ARROW", 
                      "ASSOCIATION_ARROW", "PLUS", "MINUS", "HASH", "TILDE", 
                      "LBRACE", "RBRACE", "LPAREN", "RPAREN", "LBRACK", 
                      "RBRACK", "COLON", "COMMA", "IDENTIFIER", "MULTIPLICITY", 
                      "STRING", "NUMBER", "LINE_COMMENT", "BLOCK_COMMENT", 
                      "WS" ]

    RULE_diagram = 0
    RULE_element = 1
    RULE_classDecl = 2
    RULE_interfaceDecl = 3
    RULE_enumDecl = 4
    RULE_classBody = 5
    RULE_classMember = 6
    RULE_visibility = 7
    RULE_attribute = 8
    RULE_method = 9
    RULE_paramList = 10
    RULE_param = 11
    RULE_type = 12
    RULE_relation = 13
    RULE_relationOp = 14
    RULE_label = 15

    ruleNames =  [ "diagram", "element", "classDecl", "interfaceDecl", "enumDecl", 
                   "classBody", "classMember", "visibility", "attribute", 
                   "method", "paramList", "param", "type", "relation", "relationOp", 
                   "label" ]

    EOF = Token.EOF
    STARTUML=1
    ENDUML=2
    CLASS=3
    INTERFACE=4
    ENUM=5
    ABSTRACT=6
    STATIC=7
    EXTENDS_ARROW=8
    IMPLEMENTS_ARROW=9
    COMPOSITION_ARROW=10
    AGGREGATION_ARROW=11
    DEPENDENCY_ARROW=12
    ASSOCIATION_ARROW=13
    PLUS=14
    MINUS=15
    HASH=16
    TILDE=17
    LBRACE=18
    RBRACE=19
    LPAREN=20
    RPAREN=21
    LBRACK=22
    RBRACK=23
    COLON=24
    COMMA=25
    IDENTIFIER=26
    MULTIPLICITY=27
    STRING=28
    NUMBER=29
    LINE_COMMENT=30
    BLOCK_COMMENT=31
    WS=32

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class DiagramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STARTUML(self):
            return self.getToken(PlantUMLParser.STARTUML, 0)

        def ENDUML(self):
            return self.getToken(PlantUMLParser.ENDUML, 0)

        def EOF(self):
            return self.getToken(PlantUMLParser.EOF, 0)

        def element(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PlantUMLParser.ElementContext)
            else:
                return self.getTypedRuleContext(PlantUMLParser.ElementContext,i)


        def getRuleIndex(self):
            return PlantUMLParser.RULE_diagram

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDiagram" ):
                listener.enterDiagram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDiagram" ):
                listener.exitDiagram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDiagram" ):
                return visitor.visitDiagram(self)
            else:
                return visitor.visitChildren(self)




    def diagram(self):

        localctx = PlantUMLParser.DiagramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_diagram)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 32
            self.match(PlantUMLParser.STARTUML)
            self.state = 36
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 67108984) != 0):
                self.state = 33
                self.element()
                self.state = 38
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 39
            self.match(PlantUMLParser.ENDUML)
            self.state = 40
            self.match(PlantUMLParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def classDecl(self):
            return self.getTypedRuleContext(PlantUMLParser.ClassDeclContext,0)


        def interfaceDecl(self):
            return self.getTypedRuleContext(PlantUMLParser.InterfaceDeclContext,0)


        def enumDecl(self):
            return self.getTypedRuleContext(PlantUMLParser.EnumDeclContext,0)


        def relation(self):
            return self.getTypedRuleContext(PlantUMLParser.RelationContext,0)


        def getRuleIndex(self):
            return PlantUMLParser.RULE_element

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElement" ):
                listener.enterElement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElement" ):
                listener.exitElement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElement" ):
                return visitor.visitElement(self)
            else:
                return visitor.visitChildren(self)




    def element(self):

        localctx = PlantUMLParser.ElementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_element)
        try:
            self.state = 46
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3, 6]:
                self.enterOuterAlt(localctx, 1)
                self.state = 42
                self.classDecl()
                pass
            elif token in [4]:
                self.enterOuterAlt(localctx, 2)
                self.state = 43
                self.interfaceDecl()
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 3)
                self.state = 44
                self.enumDecl()
                pass
            elif token in [26]:
                self.enterOuterAlt(localctx, 4)
                self.state = 45
                self.relation()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ClassDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CLASS(self):
            return self.getToken(PlantUMLParser.CLASS, 0)

        def IDENTIFIER(self):
            return self.getToken(PlantUMLParser.IDENTIFIER, 0)

        def ABSTRACT(self):
            return self.getToken(PlantUMLParser.ABSTRACT, 0)

        def classBody(self):
            return self.getTypedRuleContext(PlantUMLParser.ClassBodyContext,0)


        def getRuleIndex(self):
            return PlantUMLParser.RULE_classDecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterClassDecl" ):
                listener.enterClassDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitClassDecl" ):
                listener.exitClassDecl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClassDecl" ):
                return visitor.visitClassDecl(self)
            else:
                return visitor.visitChildren(self)




    def classDecl(self):

        localctx = PlantUMLParser.ClassDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_classDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 49
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==6:
                self.state = 48
                self.match(PlantUMLParser.ABSTRACT)


            self.state = 51
            self.match(PlantUMLParser.CLASS)
            self.state = 52
            self.match(PlantUMLParser.IDENTIFIER)
            self.state = 54
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==18:
                self.state = 53
                self.classBody()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InterfaceDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTERFACE(self):
            return self.getToken(PlantUMLParser.INTERFACE, 0)

        def IDENTIFIER(self):
            return self.getToken(PlantUMLParser.IDENTIFIER, 0)

        def classBody(self):
            return self.getTypedRuleContext(PlantUMLParser.ClassBodyContext,0)


        def getRuleIndex(self):
            return PlantUMLParser.RULE_interfaceDecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInterfaceDecl" ):
                listener.enterInterfaceDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInterfaceDecl" ):
                listener.exitInterfaceDecl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInterfaceDecl" ):
                return visitor.visitInterfaceDecl(self)
            else:
                return visitor.visitChildren(self)




    def interfaceDecl(self):

        localctx = PlantUMLParser.InterfaceDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_interfaceDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 56
            self.match(PlantUMLParser.INTERFACE)
            self.state = 57
            self.match(PlantUMLParser.IDENTIFIER)
            self.state = 59
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==18:
                self.state = 58
                self.classBody()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EnumDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ENUM(self):
            return self.getToken(PlantUMLParser.ENUM, 0)

        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(PlantUMLParser.IDENTIFIER)
            else:
                return self.getToken(PlantUMLParser.IDENTIFIER, i)

        def LBRACE(self):
            return self.getToken(PlantUMLParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(PlantUMLParser.RBRACE, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(PlantUMLParser.COMMA)
            else:
                return self.getToken(PlantUMLParser.COMMA, i)

        def getRuleIndex(self):
            return PlantUMLParser.RULE_enumDecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEnumDecl" ):
                listener.enterEnumDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEnumDecl" ):
                listener.exitEnumDecl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEnumDecl" ):
                return visitor.visitEnumDecl(self)
            else:
                return visitor.visitChildren(self)




    def enumDecl(self):

        localctx = PlantUMLParser.EnumDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_enumDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 61
            self.match(PlantUMLParser.ENUM)
            self.state = 62
            self.match(PlantUMLParser.IDENTIFIER)
            self.state = 63
            self.match(PlantUMLParser.LBRACE)
            self.state = 64
            self.match(PlantUMLParser.IDENTIFIER)
            self.state = 71
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==25 or _la==26:
                self.state = 66
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==25:
                    self.state = 65
                    self.match(PlantUMLParser.COMMA)


                self.state = 68
                self.match(PlantUMLParser.IDENTIFIER)
                self.state = 73
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 74
            self.match(PlantUMLParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ClassBodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACE(self):
            return self.getToken(PlantUMLParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(PlantUMLParser.RBRACE, 0)

        def classMember(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PlantUMLParser.ClassMemberContext)
            else:
                return self.getTypedRuleContext(PlantUMLParser.ClassMemberContext,i)


        def getRuleIndex(self):
            return PlantUMLParser.RULE_classBody

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterClassBody" ):
                listener.enterClassBody(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitClassBody" ):
                listener.exitClassBody(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClassBody" ):
                return visitor.visitClassBody(self)
            else:
                return visitor.visitChildren(self)




    def classBody(self):

        localctx = PlantUMLParser.ClassBodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_classBody)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 76
            self.match(PlantUMLParser.LBRACE)
            self.state = 80
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 67354816) != 0):
                self.state = 77
                self.classMember()
                self.state = 82
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 83
            self.match(PlantUMLParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ClassMemberContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def attribute(self):
            return self.getTypedRuleContext(PlantUMLParser.AttributeContext,0)


        def method(self):
            return self.getTypedRuleContext(PlantUMLParser.MethodContext,0)


        def getRuleIndex(self):
            return PlantUMLParser.RULE_classMember

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterClassMember" ):
                listener.enterClassMember(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitClassMember" ):
                listener.exitClassMember(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClassMember" ):
                return visitor.visitClassMember(self)
            else:
                return visitor.visitChildren(self)




    def classMember(self):

        localctx = PlantUMLParser.ClassMemberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_classMember)
        try:
            self.state = 87
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 85
                self.attribute()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 86
                self.method()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VisibilityContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PLUS(self):
            return self.getToken(PlantUMLParser.PLUS, 0)

        def MINUS(self):
            return self.getToken(PlantUMLParser.MINUS, 0)

        def HASH(self):
            return self.getToken(PlantUMLParser.HASH, 0)

        def TILDE(self):
            return self.getToken(PlantUMLParser.TILDE, 0)

        def getRuleIndex(self):
            return PlantUMLParser.RULE_visibility

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVisibility" ):
                listener.enterVisibility(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVisibility" ):
                listener.exitVisibility(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVisibility" ):
                return visitor.visitVisibility(self)
            else:
                return visitor.visitChildren(self)




    def visibility(self):

        localctx = PlantUMLParser.VisibilityContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_visibility)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 89
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 245760) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AttributeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(PlantUMLParser.IDENTIFIER, 0)

        def COLON(self):
            return self.getToken(PlantUMLParser.COLON, 0)

        def type_(self):
            return self.getTypedRuleContext(PlantUMLParser.TypeContext,0)


        def visibility(self):
            return self.getTypedRuleContext(PlantUMLParser.VisibilityContext,0)


        def STATIC(self):
            return self.getToken(PlantUMLParser.STATIC, 0)

        def getRuleIndex(self):
            return PlantUMLParser.RULE_attribute

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAttribute" ):
                listener.enterAttribute(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAttribute" ):
                listener.exitAttribute(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttribute" ):
                return visitor.visitAttribute(self)
            else:
                return visitor.visitChildren(self)




    def attribute(self):

        localctx = PlantUMLParser.AttributeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_attribute)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 92
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 245760) != 0):
                self.state = 91
                self.visibility()


            self.state = 95
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==7:
                self.state = 94
                self.match(PlantUMLParser.STATIC)


            self.state = 97
            self.match(PlantUMLParser.IDENTIFIER)
            self.state = 98
            self.match(PlantUMLParser.COLON)
            self.state = 99
            self.type_()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MethodContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(PlantUMLParser.IDENTIFIER, 0)

        def LPAREN(self):
            return self.getToken(PlantUMLParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(PlantUMLParser.RPAREN, 0)

        def visibility(self):
            return self.getTypedRuleContext(PlantUMLParser.VisibilityContext,0)


        def STATIC(self):
            return self.getToken(PlantUMLParser.STATIC, 0)

        def ABSTRACT(self):
            return self.getToken(PlantUMLParser.ABSTRACT, 0)

        def paramList(self):
            return self.getTypedRuleContext(PlantUMLParser.ParamListContext,0)


        def COLON(self):
            return self.getToken(PlantUMLParser.COLON, 0)

        def type_(self):
            return self.getTypedRuleContext(PlantUMLParser.TypeContext,0)


        def getRuleIndex(self):
            return PlantUMLParser.RULE_method

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMethod" ):
                listener.enterMethod(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMethod" ):
                listener.exitMethod(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethod" ):
                return visitor.visitMethod(self)
            else:
                return visitor.visitChildren(self)




    def method(self):

        localctx = PlantUMLParser.MethodContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_method)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 102
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 245760) != 0):
                self.state = 101
                self.visibility()


            self.state = 105
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==7:
                self.state = 104
                self.match(PlantUMLParser.STATIC)


            self.state = 108
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==6:
                self.state = 107
                self.match(PlantUMLParser.ABSTRACT)


            self.state = 110
            self.match(PlantUMLParser.IDENTIFIER)
            self.state = 111
            self.match(PlantUMLParser.LPAREN)
            self.state = 113
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==26:
                self.state = 112
                self.paramList()


            self.state = 115
            self.match(PlantUMLParser.RPAREN)
            self.state = 118
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==24:
                self.state = 116
                self.match(PlantUMLParser.COLON)
                self.state = 117
                self.type_()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def param(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PlantUMLParser.ParamContext)
            else:
                return self.getTypedRuleContext(PlantUMLParser.ParamContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(PlantUMLParser.COMMA)
            else:
                return self.getToken(PlantUMLParser.COMMA, i)

        def getRuleIndex(self):
            return PlantUMLParser.RULE_paramList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParamList" ):
                listener.enterParamList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParamList" ):
                listener.exitParamList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParamList" ):
                return visitor.visitParamList(self)
            else:
                return visitor.visitChildren(self)




    def paramList(self):

        localctx = PlantUMLParser.ParamListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_paramList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 120
            self.param()
            self.state = 125
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==25:
                self.state = 121
                self.match(PlantUMLParser.COMMA)
                self.state = 122
                self.param()
                self.state = 127
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(PlantUMLParser.IDENTIFIER, 0)

        def COLON(self):
            return self.getToken(PlantUMLParser.COLON, 0)

        def type_(self):
            return self.getTypedRuleContext(PlantUMLParser.TypeContext,0)


        def getRuleIndex(self):
            return PlantUMLParser.RULE_param

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParam" ):
                listener.enterParam(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParam" ):
                listener.exitParam(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam" ):
                return visitor.visitParam(self)
            else:
                return visitor.visitChildren(self)




    def param(self):

        localctx = PlantUMLParser.ParamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_param)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 128
            self.match(PlantUMLParser.IDENTIFIER)
            self.state = 129
            self.match(PlantUMLParser.COLON)
            self.state = 130
            self.type_()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(PlantUMLParser.IDENTIFIER, 0)

        def LBRACK(self):
            return self.getToken(PlantUMLParser.LBRACK, 0)

        def RBRACK(self):
            return self.getToken(PlantUMLParser.RBRACK, 0)

        def getRuleIndex(self):
            return PlantUMLParser.RULE_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterType" ):
                listener.enterType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitType" ):
                listener.exitType(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitType" ):
                return visitor.visitType(self)
            else:
                return visitor.visitChildren(self)




    def type_(self):

        localctx = PlantUMLParser.TypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 132
            self.match(PlantUMLParser.IDENTIFIER)
            self.state = 135
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==22:
                self.state = 133
                self.match(PlantUMLParser.LBRACK)
                self.state = 134
                self.match(PlantUMLParser.RBRACK)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RelationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(PlantUMLParser.IDENTIFIER)
            else:
                return self.getToken(PlantUMLParser.IDENTIFIER, i)

        def relationOp(self):
            return self.getTypedRuleContext(PlantUMLParser.RelationOpContext,0)


        def MULTIPLICITY(self, i:int=None):
            if i is None:
                return self.getTokens(PlantUMLParser.MULTIPLICITY)
            else:
                return self.getToken(PlantUMLParser.MULTIPLICITY, i)

        def COLON(self):
            return self.getToken(PlantUMLParser.COLON, 0)

        def label(self):
            return self.getTypedRuleContext(PlantUMLParser.LabelContext,0)


        def getRuleIndex(self):
            return PlantUMLParser.RULE_relation

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRelation" ):
                listener.enterRelation(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRelation" ):
                listener.exitRelation(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRelation" ):
                return visitor.visitRelation(self)
            else:
                return visitor.visitChildren(self)




    def relation(self):

        localctx = PlantUMLParser.RelationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_relation)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 137
            self.match(PlantUMLParser.IDENTIFIER)
            self.state = 139
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==27:
                self.state = 138
                self.match(PlantUMLParser.MULTIPLICITY)


            self.state = 141
            self.relationOp()
            self.state = 143
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==27:
                self.state = 142
                self.match(PlantUMLParser.MULTIPLICITY)


            self.state = 145
            self.match(PlantUMLParser.IDENTIFIER)
            self.state = 148
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==24:
                self.state = 146
                self.match(PlantUMLParser.COLON)
                self.state = 147
                self.label()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RelationOpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EXTENDS_ARROW(self):
            return self.getToken(PlantUMLParser.EXTENDS_ARROW, 0)

        def IMPLEMENTS_ARROW(self):
            return self.getToken(PlantUMLParser.IMPLEMENTS_ARROW, 0)

        def COMPOSITION_ARROW(self):
            return self.getToken(PlantUMLParser.COMPOSITION_ARROW, 0)

        def AGGREGATION_ARROW(self):
            return self.getToken(PlantUMLParser.AGGREGATION_ARROW, 0)

        def DEPENDENCY_ARROW(self):
            return self.getToken(PlantUMLParser.DEPENDENCY_ARROW, 0)

        def ASSOCIATION_ARROW(self):
            return self.getToken(PlantUMLParser.ASSOCIATION_ARROW, 0)

        def getRuleIndex(self):
            return PlantUMLParser.RULE_relationOp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRelationOp" ):
                listener.enterRelationOp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRelationOp" ):
                listener.exitRelationOp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRelationOp" ):
                return visitor.visitRelationOp(self)
            else:
                return visitor.visitChildren(self)




    def relationOp(self):

        localctx = PlantUMLParser.RelationOpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_relationOp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 150
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 16128) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LabelContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(PlantUMLParser.IDENTIFIER)
            else:
                return self.getToken(PlantUMLParser.IDENTIFIER, i)

        def STRING(self, i:int=None):
            if i is None:
                return self.getTokens(PlantUMLParser.STRING)
            else:
                return self.getToken(PlantUMLParser.STRING, i)

        def NUMBER(self, i:int=None):
            if i is None:
                return self.getTokens(PlantUMLParser.NUMBER)
            else:
                return self.getToken(PlantUMLParser.NUMBER, i)

        def getRuleIndex(self):
            return PlantUMLParser.RULE_label

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLabel" ):
                listener.enterLabel(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLabel" ):
                listener.exitLabel(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLabel" ):
                return visitor.visitLabel(self)
            else:
                return visitor.visitChildren(self)




    def label(self):

        localctx = PlantUMLParser.LabelContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_label)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 153 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 152
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 872415232) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()

                else:
                    raise NoViableAltException(self)
                self.state = 155 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,21,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





