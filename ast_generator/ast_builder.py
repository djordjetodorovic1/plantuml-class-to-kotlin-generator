from parser.PlantUMLVisitor import PlantUMLVisitor
from parser.PlantUMLParser import PlantUMLParser
from ast_generator.ast_nodes import (
    DiagramNode, ClassNode, EnumNode, RelationNode,
    AttributeNode, MethodNode, ParamNode
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
            line=ctx.start.line,
            column=ctx.start.column + 1
        )
        self.fill_class_body(node, ctx.classBody())
        return node

    def visitInterfaceDecl(self, ctx):
        node = ClassNode(
            name=ctx.IDENTIFIER().getText(),
            is_abstract=False,
            is_interface=True,
            line=ctx.start.line,
            column=ctx.start.column + 1
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
            line=ctx.start.line,
            column=ctx.start.column + 1
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
            line=ctx.start.line,
            column=ctx.start.column + 1
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
        return EnumNode(name, constants, line=ctx.start.line, column=ctx.start.column + 1)

    # Relation
    def visitRelation(self, ctx):
        identifiers = ctx.IDENTIFIER()
        source_name = identifiers[0].getText()
        target_name = identifiers[1].getText()

        op_ctx = ctx.relationOp()
        op_token = op_ctx.getChild(0).getSymbol()
        op_text = op_ctx.getChild(0).getText()
        token_type_name = PlantUMLParser.symbolicNames[op_token.type]
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

        if op_text in REVERSED_ARROW_MAP.get(token_type_name, ()):
            source_name, target_name = target_name, source_name
            source_mult, target_mult = target_mult, source_mult

        label_text = self.label_text(ctx.label()) if ctx.label() else None

        return RelationNode(
            source=source_name,
            target=target_name,
            relation_type=relation_type,
            source_multiplicity=source_mult,
            target_multiplicity=target_mult,
            label=label_text,
            line=ctx.start.line,
            column=ctx.start.column + 1
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

REVERSED_ARROW_MAP = {
    "EXTENDS_ARROW": ("<|--",),
    "IMPLEMENTS_ARROW": ("<|..",),
    "COMPOSITION_ARROW": ("--*",),
    "AGGREGATION_ARROW": ("--o",),
    "DEPENDENCY_ARROW": ("<..",),
    "ASSOCIATION_ARROW": ("<--",),
}