from dataclasses import dataclass, field

@dataclass
class ParamNode:
    name: str
    type_name: str
    line: int | None = None
    column: int | None = None

@dataclass
class AttributeNode:
    name: str
    type_name: str
    visibility: str | None = None
    is_static: bool = False
    line: int | None = None
    column: int | None = None

@dataclass
class MethodNode:
    name: str
    params: list[ParamNode] = field(default_factory=list)
    return_type: str | None = None
    visibility: str | None = None
    is_static: bool = False
    is_abstract: bool = False
    line: int | None = None
    column: int | None = None

@dataclass
class ClassNode:
    # class/interface node
    name: str
    is_abstract: bool = False
    is_interface: bool = False
    attributes: list[AttributeNode] = field(default_factory=list)
    methods: list[MethodNode] = field(default_factory=list)
    line: int | None = None
    column: int | None = None

@dataclass
class EnumNode:
    name: str
    constants: list[str] = field(default_factory=list)
    line: int | None = None
    column: int | None = None

@dataclass
class RelationNode:
    source: str
    target: str
    relation_type: str
    source_multiplicity: str | None = None
    target_multiplicity: str | None = None
    label: str | None = None
    line: int | None = None
    column: int | None = None

@dataclass
class DiagramNode:
    # root node
    classes: list[ClassNode] = field(default_factory=list)
    enums: list[EnumNode] = field(default_factory=list)
    relations: list[RelationNode] = field(default_factory=list)

    def find_class(self, name):
        for c in self.classes:
            if c.name == name:
                return c
        return None