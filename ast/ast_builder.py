from parser.PlantUMLVisitor import PlantUMLVisitor
from parser.PlantUMLParser import PlantUMLParser
from ast_nodes import (
    DiagramNode, ClassNode, EnumNode, RelationNode,
    AttributeNode, MethodNode, ParamNode,
)

class ASTBuilder(PlantUMLVisitor):
    # Root
    def visitDiagram(self, ctx):
        diagram = DiagramNode()

        for element_ctx in ctx.element():
            if element_ctx.classDecl():
                diagram.classes.append(self.visitClassDecl(element_ctx.classDecl()))
            elif element_ctx.interfaceDecl():
                diagram.classes.append(self.visitInterfaceDecl(element_ctx.interfaceDecl()))
            elif element_ctx.enumDecl():
                diagram.enums.append(self.visitEnumDecl(element_ctx.enumDecl()))
            elif element_ctx.relation():
                diagram.relations.append(self.visitRelation(element_ctx.relation()))
        return diagram

    # Class/Interface
    def visitClassDecl(self, ctx):
        node = ClassNode(
            name=ctx.IDENTIFIER().getText(),
            is_abstract=ctx.ABSTRACT() is not None,
            is_interface=False,
        )
        self.fill_class_body(node, ctx.classBody())
        return node

    def visitInterfaceDecl(self, ctx):
        node = ClassNode(
            name=ctx.IDENTIFIER().getText(),
            is_abstract=False,
            is_interface=True,
        )
        self.fill_class_body(node, ctx.classBody())
        return node

    def fill_class_body(self, node, body_ctx):
        if body_ctx is None:
            return
        for member_ctx in body_ctx.classMember():
            if member_ctx.attribute():
                node.attributes.append(self.visitAttribute(member_ctx.attribute()))
            elif member_ctx.method():
                node.methods.append(self.visitMethod(member_ctx.method()))

    def visitAttribute(self, ctx):
        return AttributeNode(
            name=ctx.IDENTIFIER().getText(),
            type_name=self.type_text(ctx.type_()),
            visibility=self.visibility_symbol(ctx.visibility()),
            is_static=ctx.STATIC() is not None,
        )

    def visitMethod(self, ctx):
        params = []
        if ctx.paramList():
            for param_ctx in ctx.paramList().param():
                params.append(ParamNode(
                    name=param_ctx.IDENTIFIER().getText(),
                    type_name=self.type_text(param_ctx.type_()),
                ))

        return MethodNode(
            name=ctx.IDENTIFIER().getText(),
            params=params,
            return_type=self.type_text(ctx.type_()) if ctx.type_() else None,
            visibility=self.visibility_symbol(ctx.visibility()),
            is_static=ctx.STATIC() is not None,
            is_abstract=ctx.ABSTRACT() is not None,
        )

    def visibility_symbol(self, visibility_ctx):
        return visibility_ctx.getText() if visibility_ctx else None
    
    def type_text(self, type_ctx):
        return type_ctx.getText() if type_ctx else ""
    
    # Enum
    def visitEnumDecl(self, ctx):
        identifiers = ctx.IDENTIFIER()
        name = identifiers[0].getText()
        constants = [ident.getText() for ident in identifiers[1:]]
        return EnumNode(name, constants)

    # Relation
    def visitRelation(self, ctx):
        identifiers = ctx.IDENTIFIER()
        source_name = identifiers[0].getText()
        target_name = identifiers[1].getText()

        op_ctx = ctx.relationOp()
        relation_token = op_ctx.getChild(0).getSymbol()
        token_type_name = PlantUMLParser.symbolicNames[relation_token.type]
        relation_type = RELATION_TYPE_MAP.get(token_type_name, "UNKNOWN")

        mult_terminals = ctx.MULTIPLICITY()
        op_index = list(ctx.children).index(op_ctx)
        source_mult = None
        target_mult = None
        for term in mult_terminals:
            term_index = list(ctx.children).index(term)
            if term_index < op_index:
                source_mult = term.getText().strip('"')
            else:
                target_mult = term.getText().strip('"')

        label_text = self.label_text(ctx.label()) if ctx.label() else None

        return RelationNode(
            source=source_name,
            target=target_name,
            relation_type=relation_type,
            source_multiplicity=source_mult,
            target_multiplicity=target_mult,
            label=label_text,
        )

    def label_text(self, label_ctx):
        return " ".join(child.getText().strip('"') for child in label_ctx.children)


RELATION_TYPE_MAP = {
    "EXTENDS_ARROW": "EXTENDS",
    "IMPLEMENTS_ARROW": "IMPLEMENTS",
    "COMPOSITION_ARROW": "COMPOSITION",
    "AGGREGATION_ARROW": "AGGREGATION",
    "DEPENDENCY_ARROW": "DEPENDENCY",
    "ASSOCIATION_ARROW": "ASSOCIATION",
}