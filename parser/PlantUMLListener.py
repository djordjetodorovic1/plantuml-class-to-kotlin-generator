# Generated from ../grammar/PlantUML.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .PlantUMLParser import PlantUMLParser
else:
    from PlantUMLParser import PlantUMLParser

# This class defines a complete listener for a parse tree produced by PlantUMLParser.
class PlantUMLListener(ParseTreeListener):

    # Enter a parse tree produced by PlantUMLParser#diagram.
    def enterDiagram(self, ctx:PlantUMLParser.DiagramContext):
        pass

    # Exit a parse tree produced by PlantUMLParser#diagram.
    def exitDiagram(self, ctx:PlantUMLParser.DiagramContext):
        pass


    # Enter a parse tree produced by PlantUMLParser#element.
    def enterElement(self, ctx:PlantUMLParser.ElementContext):
        pass

    # Exit a parse tree produced by PlantUMLParser#element.
    def exitElement(self, ctx:PlantUMLParser.ElementContext):
        pass


    # Enter a parse tree produced by PlantUMLParser#classDecl.
    def enterClassDecl(self, ctx:PlantUMLParser.ClassDeclContext):
        pass

    # Exit a parse tree produced by PlantUMLParser#classDecl.
    def exitClassDecl(self, ctx:PlantUMLParser.ClassDeclContext):
        pass


    # Enter a parse tree produced by PlantUMLParser#interfaceDecl.
    def enterInterfaceDecl(self, ctx:PlantUMLParser.InterfaceDeclContext):
        pass

    # Exit a parse tree produced by PlantUMLParser#interfaceDecl.
    def exitInterfaceDecl(self, ctx:PlantUMLParser.InterfaceDeclContext):
        pass


    # Enter a parse tree produced by PlantUMLParser#enumDecl.
    def enterEnumDecl(self, ctx:PlantUMLParser.EnumDeclContext):
        pass

    # Exit a parse tree produced by PlantUMLParser#enumDecl.
    def exitEnumDecl(self, ctx:PlantUMLParser.EnumDeclContext):
        pass


    # Enter a parse tree produced by PlantUMLParser#classBody.
    def enterClassBody(self, ctx:PlantUMLParser.ClassBodyContext):
        pass

    # Exit a parse tree produced by PlantUMLParser#classBody.
    def exitClassBody(self, ctx:PlantUMLParser.ClassBodyContext):
        pass


    # Enter a parse tree produced by PlantUMLParser#classMember.
    def enterClassMember(self, ctx:PlantUMLParser.ClassMemberContext):
        pass

    # Exit a parse tree produced by PlantUMLParser#classMember.
    def exitClassMember(self, ctx:PlantUMLParser.ClassMemberContext):
        pass


    # Enter a parse tree produced by PlantUMLParser#visibility.
    def enterVisibility(self, ctx:PlantUMLParser.VisibilityContext):
        pass

    # Exit a parse tree produced by PlantUMLParser#visibility.
    def exitVisibility(self, ctx:PlantUMLParser.VisibilityContext):
        pass


    # Enter a parse tree produced by PlantUMLParser#attribute.
    def enterAttribute(self, ctx:PlantUMLParser.AttributeContext):
        pass

    # Exit a parse tree produced by PlantUMLParser#attribute.
    def exitAttribute(self, ctx:PlantUMLParser.AttributeContext):
        pass


    # Enter a parse tree produced by PlantUMLParser#method.
    def enterMethod(self, ctx:PlantUMLParser.MethodContext):
        pass

    # Exit a parse tree produced by PlantUMLParser#method.
    def exitMethod(self, ctx:PlantUMLParser.MethodContext):
        pass


    # Enter a parse tree produced by PlantUMLParser#paramList.
    def enterParamList(self, ctx:PlantUMLParser.ParamListContext):
        pass

    # Exit a parse tree produced by PlantUMLParser#paramList.
    def exitParamList(self, ctx:PlantUMLParser.ParamListContext):
        pass


    # Enter a parse tree produced by PlantUMLParser#param.
    def enterParam(self, ctx:PlantUMLParser.ParamContext):
        pass

    # Exit a parse tree produced by PlantUMLParser#param.
    def exitParam(self, ctx:PlantUMLParser.ParamContext):
        pass


    # Enter a parse tree produced by PlantUMLParser#type.
    def enterType(self, ctx:PlantUMLParser.TypeContext):
        pass

    # Exit a parse tree produced by PlantUMLParser#type.
    def exitType(self, ctx:PlantUMLParser.TypeContext):
        pass


    # Enter a parse tree produced by PlantUMLParser#relation.
    def enterRelation(self, ctx:PlantUMLParser.RelationContext):
        pass

    # Exit a parse tree produced by PlantUMLParser#relation.
    def exitRelation(self, ctx:PlantUMLParser.RelationContext):
        pass


    # Enter a parse tree produced by PlantUMLParser#relationOp.
    def enterRelationOp(self, ctx:PlantUMLParser.RelationOpContext):
        pass

    # Exit a parse tree produced by PlantUMLParser#relationOp.
    def exitRelationOp(self, ctx:PlantUMLParser.RelationOpContext):
        pass


    # Enter a parse tree produced by PlantUMLParser#label.
    def enterLabel(self, ctx:PlantUMLParser.LabelContext):
        pass

    # Exit a parse tree produced by PlantUMLParser#label.
    def exitLabel(self, ctx:PlantUMLParser.LabelContext):
        pass



del PlantUMLParser