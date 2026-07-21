from dataclasses import dataclass

@dataclass
class SemanticIssue:
    message: str
    line: int | None = None
    column: int | None = None

    def __str__(self):
        if self.line is not None and self.column is not None:
            return f"[SemanticError]: Linija {self.line}, kolona {self.column}: {self.message}"
        return f"[SemanticError]: {self.message}"


class SemanticChecker:
    def __init__(self, diagram):
        self.diagram = diagram
        self.issues: list[SemanticIssue] = []

    def check(self):
        self.issues = []

        self.check_duplicate_names()
        self.check_relation_targets_exist()
        self.check_relation_type_compatibility()
        self.check_circular_inheritance()
        self.check_interface_implementation()

        return self.issues

    def check_duplicate_names(self):
        seen_class_names = {}
 
        for cls in self.diagram.classes:
            if cls.name in seen_class_names:
                self.issues.append(SemanticIssue(
                    message=f"Duplirano ime klase/interfejsa: '{cls.name}' je definisano vise puta.",
                    line=getattr(cls, "line", None),
                    column=getattr(cls, "column", None)
                ))
            seen_class_names[cls.name] = cls
 
            seen_attrs = set()
            for attr in cls.attributes:
                if attr.name in seen_attrs:
                    self.issues.append(SemanticIssue(
                        message=f"Klasa '{cls.name}': duplirani atribut '{attr.name}'.",
                        line=getattr(attr, "line", None),
                        column=getattr(attr, "column", None)
                    ))
                seen_attrs.add(attr.name)
 
            seen_methods = set()
            for method in cls.methods:
                param_types = tuple(param.type_name for param in method.params)
                signature = (method.name, param_types)
                if signature in seen_methods:
                    self.issues.append(SemanticIssue(
                        message=f"Klasa '{cls.name}': duplirana metoda '{method.name}' sa istim tipovima parametara ({', '.join(param_types) or 'bez parametara'}).",
                        line=getattr(method, "line", None),
                        column=getattr(method, "column", None)
                    ))
                seen_methods.add(signature)

        for enum in self.diagram.enums:
            if enum.name in seen_class_names:
                self.issues.append(SemanticIssue(
                    message=f"Ime '{enum.name}' je vec definisano.",
                    line=getattr(enum, "line", None),
                    column=getattr(enum, "column", None)
                ))
            seen_class_names[enum.name] = enum

    def all_type_names(self):
        names = {cls.name for cls in self.diagram.classes}
        names |= {enum.name for enum in self.diagram.enums}
        return names

    def check_relation_targets_exist(self):
        known = self.all_type_names()
        for rel in self.diagram.relations:
            if rel.source not in known:
                self.issues.append(SemanticIssue(
                    message=f"Relacija referencira nepostojecu klasu '{rel.source}' (u relaciji {rel.source} -> {rel.target}).",
                    line=getattr(rel, "line", None),
                    column=getattr(rel, "column", None)
                ))
            if rel.target not in known:
                self.issues.append(SemanticIssue(
                    message=f"Relacija referencira nepostojecu klasu '{rel.target}' (u relaciji {rel.source} -> {rel.target}).",
                    line=getattr(rel, "line", None),
                    column=getattr(rel, "column", None)
                ))

    def classify(self, name):
        cls = self.diagram.find_class(name)
        if cls is not None:
            return "interface" if cls.is_interface else "class"
        if any(enum.name == name for enum in self.diagram.enums):
            return "enum"
        return None
 
    def check_relation_type_compatibility(self):
        for rel in self.diagram.relations:
            source_kind = self.classify(rel.source)
            target_kind = self.classify(rel.target)
 
            if source_kind is None or target_kind is None:
                continue
 
            if rel.relation_type == "EXTENDS":
                if source_kind in ("interface", "enum"):
                    self.issues.append(SemanticIssue(
                        message=f"Relacija '{rel.source} --|> {rel.target}': izvor '{rel.source}' je {source_kind}, "
                                f"a EXTENDS (--|>) relacija je dozvoljena samo kada je izvor klasa.",
                        line=getattr(rel, "line", None),
                        column=getattr(rel, "column", None)
                    ))
                if target_kind in ("interface", "enum"):
                    self.issues.append(SemanticIssue(
                        message=f"Relacija '{rel.source} --|> {rel.target}': cilj '{rel.target}' je {target_kind}, "
                                f"a EXTENDS (--|>) relacija zahtijeva da cilj bude klasa.",
                        line=getattr(rel, "line", None),
                        column=getattr(rel, "column", None)
                    ))
 
            elif rel.relation_type == "IMPLEMENTS":
                if target_kind != "interface":
                    self.issues.append(SemanticIssue(
                        message=f"Relacija '{rel.source} ..|> {rel.target}': cilj '{rel.target}' je {target_kind}, "
                                f"a IMPLEMENTS (..|>) relacija zahtijeva da cilj bude interfejs.",
                        line=getattr(rel, "line", None),
                        column=getattr(rel, "column", None)
                    ))

    def check_circular_inheritance(self):
        parents: dict[str, list[str]] = {}
        for rel in self.diagram.relations:
            if rel.relation_type in ("EXTENDS", "IMPLEMENTS"):
                parents.setdefault(rel.source, []).append(rel.target)

        classes_by_name = {cls.name: cls for cls in self.diagram.classes}

        reported = set()
        for cls_name in parents:
            if cls_name in reported:
                continue

            chain = set()
            stack = list(parents.get(cls_name, []))
            cyclic = False
            while stack:
                current = stack.pop()
                if current == cls_name:
                    cyclic = True
                    break
                if current in chain:
                    continue
                chain.add(current)
                stack.extend(parents.get(current, []))

            if cyclic:
                cls = classes_by_name.get(cls_name)
                self.issues.append(SemanticIssue(
                    message=f"Ciklicno nasljedjivanje/implementacija ukljucuje klasu '{cls_name}'.",
                    line=getattr(cls, "line", None) if cls else None,
                    column=getattr(cls, "column", None) if cls else None
                ))
                reported.add(cls_name)

    def check_interface_implementation(self):
        interfaces_by_name = {cls.name: cls for cls in self.diagram.classes if cls.is_interface}

        parents: dict[str, list[str]] = {}
        for rel in self.diagram.relations:
            if rel.relation_type in ("EXTENDS", "IMPLEMENTS"):
                parents.setdefault(rel.source, []).append(rel.target)

        classes_by_name = {cls.name: cls for cls in self.diagram.classes}

        def collect_method_names(cls_name, visited=None):
            if visited is None:
                visited = set()
            if cls_name in visited or cls_name not in classes_by_name:
                return set()
            visited.add(cls_name)

            cls = classes_by_name[cls_name]
            names = set() if cls.is_interface else {m.name for m in cls.methods}

            for parent_name in parents.get(cls_name, []):
                names |= collect_method_names(parent_name, visited)
            return names

        for rel in self.diagram.relations:
            if rel.relation_type != "IMPLEMENTS":
                continue
            if rel.target not in interfaces_by_name:
                continue

            interface = interfaces_by_name[rel.target]
            required_methods = {m.name for m in interface.methods}
            implemented_methods = collect_method_names(rel.source)

            missing = required_methods - implemented_methods
            if missing:
                self.issues.append(SemanticIssue(
                    message=f"Klasa '{rel.source}' implementira interfejs '{rel.target}' ali nedostaju metode: {', '.join(sorted(missing))}.",
                    line=getattr(rel, "line", None),
                    column=getattr(rel, "column", None)
                ))