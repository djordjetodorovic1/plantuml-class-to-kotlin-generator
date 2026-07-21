from ast_generator.ast_nodes import DiagramNode, ClassNode, AttributeNode, MethodNode, RelationNode

TYPE_MAPPING = {
    "String": "String",
    "int": "Int",
    "integer": "Int",
    "double": "Double",
    "float": "Float",
    "long": "Long",
    "boolean": "Boolean",
    "bool": "Boolean",
    "char": "Char",
    "byte": "Byte",
    "short": "Short",
    "void": "Unit"
}

VISIBILITY_MAPPING = {
    "+": "",  # public
    "-": "private ",
    "#": "protected ",
    "~": "internal ",
    None: ""
}

STRUCTURAL_RELATIONS = {"ASSOCIATION", "AGGREGATION", "COMPOSITION"}


def map_type(type_name):
    is_array = type_name.endswith("[]")
    base = type_name[:-2] if is_array else type_name
    mapped_base = TYPE_MAPPING.get(base, base)
    return f"List<{mapped_base}>" if is_array else mapped_base


def map_return_type(type_name):
    if type_name is None:
        return None
    mapped = TYPE_MAPPING.get(type_name)
    if mapped == "Unit":
        return None
    return map_type(type_name)


def lower_first(name):
    return name[0].lower() + name[1:] if name else name


class KotlinCodeGenerator:
    def __init__(self, diagram):
        self.diagram = diagram
        self.extends_map: dict[str, str] = {}
        self.implements_map: dict[str, list[str]] = {}
        self.structural_relations_by_source: dict[str, list[RelationNode]] = {}
        self.superclass_names: set[str] = set()
        self.index_relations()

    def index_relations(self):
        for rel in self.diagram.relations:
            if rel.relation_type == "EXTENDS":
                self.extends_map[rel.source] = rel.target
                self.superclass_names.add(rel.target)
            elif rel.relation_type == "IMPLEMENTS":
                self.implements_map.setdefault(rel.source, []).append(rel.target)
            elif rel.relation_type in STRUCTURAL_RELATIONS:
                self.structural_relations_by_source.setdefault(rel.source, []).append(rel)
    
    # code generator
    def generate(self):
        parts = []

        for cls in self.diagram.classes:
            if cls.is_interface:
                parts.append(self.generate_interface(cls))
            else:
                parts.append(self.generate_class(cls))

        for enum in self.diagram.enums:
            parts.append(self.generate_enum(enum))

        return "\n\n".join(parts)


    def generate_interface(self, cls):
        lines = []

        parent_interfaces = self.implements_map.get(cls.name, [])
        header = f"interface {cls.name}"
        if parent_interfaces:
            header += " : " + ", ".join(parent_interfaces)
        header += " {"
        lines.append(header)

        for attr in cls.attributes:
            lines.append(f"    val {attr.name}: {map_type(attr.type_name)}")

        if cls.attributes and cls.methods:
            lines.append("")

        for method in cls.methods:
            lines.append(f"    {self.method_signature(method)}")

        lines.append("}")
        return "\n".join(lines)


    def generate_enum(self, enum):
        lines = [f"enum class {enum.name} {{"]
        constants = ",\n".join(f"    {c}" for c in enum.constants)
        lines.append(constants)
        lines.append("}")
        return "\n".join(lines)


    def generate_class(self, cls):
        parent_name = self.extends_map.get(cls.name)
        parent_args = self.get_class_constructor_args(parent_name) if parent_name else []
        forwarded_params = [f"{arg_name}: {arg_type}" for arg_name, arg_type in parent_args]

        own_params = [
            f"{VISIBILITY_MAPPING[attr.visibility]}var {attr.name}: {map_type(attr.type_name)}"
            for attr in cls.attributes
        ]
        single_relation_params, many_relation_body_lines = self.structural_relation_parts(cls.name)
        constructor_params = forwarded_params + own_params + single_relation_params
        
        if cls.is_abstract:
            header_prefix = "abstract class"
        elif cls.name in self.superclass_names:
            header_prefix = "open class"
        else:
            header_prefix = "class"
        header = f"{header_prefix} {cls.name}"

        if constructor_params:
            if len(constructor_params) == 1:
                header += f"({constructor_params[0]})"
            else:
                params_joined = ",\n".join(f"    {p}" for p in constructor_params)
                header += f"(\n{params_joined}\n)"

        supertypes = self.supertypes_for(cls.name)
        if supertypes:
            header += " : " + ", ".join(supertypes)

        contract_names = self.abstract_contract_names(cls.name)
        method_lines = [self.method_block(m, override=m.name in contract_names) for m in cls.methods]

        body_parts = []
        if many_relation_body_lines:
            body_parts.append("\n".join(many_relation_body_lines))
        if method_lines:
            body_parts.append("\n".join(method_lines))

        if not body_parts:
            return header

        return header + " {\n" + "\n".join(body_parts) + "\n\n}"

    def supertypes_for(self, class_name):
        supertypes = []
        if class_name in self.extends_map:
            parent_name = self.extends_map[class_name]
            parent_args = self.get_class_constructor_args(parent_name)
            arg_names = ", ".join(arg_name for arg_name, _ in parent_args)
            supertypes.append(f"{parent_name}({arg_names})")
        supertypes.extend(self.implements_map.get(class_name, []))
        return supertypes

    def structural_relation_parts(self, class_name):
        single_params = []
        many_body_lines = []

        for rel in self.structural_relations_by_source.get(class_name, []):
            attr_name = rel.label if rel.label else lower_first(rel.target)
            is_many = rel.target_multiplicity in ("many", "*") or (rel.target_multiplicity and ".." in rel.target_multiplicity)
            if is_many:
                many_body_lines.append(f"    var {attr_name}: List<{rel.target}> = mutableListOf()")
            else:
                single_params.append(f"var {attr_name}: {rel.target}")

        return single_params, many_body_lines
    
    def get_class_constructor_args(self, class_name):
        cls = self.diagram.find_class(class_name)
        if not cls:
            return []    
        args = []  

        parent_name = self.extends_map.get(class_name)
        if parent_name:
            args.extend(self.get_class_constructor_args(parent_name))

        for attr in cls.attributes:
            args.append((attr.name, map_type(attr.type_name)))
        for rel in self.structural_relations_by_source.get(class_name, []):
            is_many = rel.target_multiplicity in ("many", "*") or (rel.target_multiplicity and ".." in rel.target_multiplicity)
            if not is_many:
                attr_name = rel.label if rel.label else lower_first(rel.target)
                args.append((attr_name, rel.target))
        return args

    def abstract_contract_names(self, class_name):
        names: set[str] = set()

        for interface_name in self.implements_map.get(class_name, []):
            interface = self.diagram.find_class(interface_name)
            if interface:
                names |= {m.name for m in interface.methods}

        parent_name = self.extends_map.get(class_name)
        if parent_name:
            parent_cls = self.diagram.find_class(parent_name)
            if parent_cls:
                names |= {m.name for m in parent_cls.methods if m.is_abstract}
            names |= self.abstract_contract_names(parent_name)

        return names

    def method_signature(self, method):
        params = ", ".join(f"{p.name}: {map_type(p.type_name)}" for p in method.params)
        return_type = map_return_type(method.return_type)
        return_suffix = f": {return_type}" if return_type else ""
        return f"fun {method.name}({params}){return_suffix}"

    def method_block(self, method, override=False):
        visibility = VISIBILITY_MAPPING[method.visibility]
        signature = self.method_signature(method)
        override_prefix = "override " if override else ""

        if method.is_abstract:
            return f"    {visibility}{override_prefix}abstract {signature}"
        return f"    {visibility}{override_prefix}{signature} {{\n        TODO()\n    }}"
    

def generate_kotlin_code(diagram):
    return KotlinCodeGenerator(diagram).generate()