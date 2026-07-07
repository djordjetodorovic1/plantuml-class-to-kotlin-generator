# Generated from ../grammar/PlantUML.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .PlantUMLParser import PlantUMLParser
else:
    from PlantUMLParser import PlantUMLParser

# This class defines a complete generic visitor for a parse tree produced by PlantUMLParser.

class PlantUMLVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by PlantUMLParser#diagram.
    def visitDiagram(self, ctx:PlantUMLParser.DiagramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlantUMLParser#element.
    def visitElement(self, ctx:PlantUMLParser.ElementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlantUMLParser#classDecl.
    def visitClassDecl(self, ctx:PlantUMLParser.ClassDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlantUMLParser#interfaceDecl.
    def visitInterfaceDecl(self, ctx:PlantUMLParser.InterfaceDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlantUMLParser#enumDecl.
    def visitEnumDecl(self, ctx:PlantUMLParser.EnumDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlantUMLParser#classBody.
    def visitClassBody(self, ctx:PlantUMLParser.ClassBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlantUMLParser#classMember.
    def visitClassMember(self, ctx:PlantUMLParser.ClassMemberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlantUMLParser#visibility.
    def visitVisibility(self, ctx:PlantUMLParser.VisibilityContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlantUMLParser#attribute.
    def visitAttribute(self, ctx:PlantUMLParser.AttributeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlantUMLParser#method.
    def visitMethod(self, ctx:PlantUMLParser.MethodContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlantUMLParser#paramList.
    def visitParamList(self, ctx:PlantUMLParser.ParamListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlantUMLParser#param.
    def visitParam(self, ctx:PlantUMLParser.ParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlantUMLParser#type.
    def visitType(self, ctx:PlantUMLParser.TypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlantUMLParser#relation.
    def visitRelation(self, ctx:PlantUMLParser.RelationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlantUMLParser#relationOp.
    def visitRelationOp(self, ctx:PlantUMLParser.RelationOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlantUMLParser#label.
    def visitLabel(self, ctx:PlantUMLParser.LabelContext):
        return self.visitChildren(ctx)



del PlantUMLParser