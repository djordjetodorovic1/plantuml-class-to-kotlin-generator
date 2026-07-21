import sys
import os
import glob
from antlr4 import FileStream, CommonTokenStream
from antlr4.error.ErrorListener import ErrorListener
from parser.PlantUMLLexer import PlantUMLLexer
from parser.PlantUMLParser import PlantUMLParser
from ast_generator.ast_builder import ASTBuilder
from semantic_check.semantic_checker import SemanticChecker
from code_generator.code_generator import generate_kotlin_code


EXAMPLES_DIR = "examples"
DEFAULT_OUTPUT_DIR = "output"


class CollectingErrorListener(ErrorListener):
    def __init__(self):
        super().__init__()
        self.errors: list[str] = []

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        self.errors.append(f"[SyntaxError]: Linija {line}, kolona {column}: {msg}")


def parse_file(path: str):
    input_stream = FileStream(path, encoding="utf-8")
    lexer = PlantUMLLexer(input_stream)
    lexer.removeErrorListeners()
    lexer_errors = CollectingErrorListener()
    lexer.addErrorListener(lexer_errors)

    tokens = CommonTokenStream(lexer)
    parser = PlantUMLParser(tokens)
    parser.removeErrorListeners()
    parser_errors = CollectingErrorListener()
    parser.addErrorListener(parser_errors)

    tree = parser.diagram()

    all_errors = lexer_errors.errors + parser_errors.errors
    if all_errors:
        return None, all_errors
    return tree, None


def process_file(input_path, output_path):
    print(f"Obrada: {input_path}")

    tree, syntax_errors = parse_file(input_path)
    if syntax_errors:
        print("Sintaksne greske:")
        for err in syntax_errors:
            print(f"    {err}")
        return False

    builder = ASTBuilder()
    diagram = builder.visit(tree)
    checker = SemanticChecker(diagram)
    errors = checker.check()

    if errors:
        print("Semanticke greske:")
        for error in errors:
            print(f"    {error}")
        print("Generisanje koda zaustavljeno!")
        return False

    kotlin_code = generate_kotlin_code(diagram)

    os.makedirs(os.path.dirname(output_path) or ".", exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(kotlin_code)

    print(f"Uspjesno generisano -> {output_path}")
    return True


def resolve_output_path(input_path, output_dir):
    base_name = os.path.splitext(os.path.basename(input_path))[0]
    return os.path.join(output_dir, f"{base_name}.kt")


if __name__ == "__main__":
    input_files = sorted(glob.glob(os.path.join(EXAMPLES_DIR, "*.uml")))

    if not input_files:
        print(f"Nema .uml fajlova u '{EXAMPLES_DIR}/' folderu.", sys.stderr)
        sys.exit(1)

    success_count = 0
    failure_count = 0

    for input_path in input_files:
        print("-" * 100)
        output_path = resolve_output_path(input_path, DEFAULT_OUTPUT_DIR)

        if process_file(input_path, output_path):
            success_count += 1
        else:
            failure_count += 1

    print("-" * 100)
    print(f"Prevodjenje zavrseno: {success_count} uspjesno, {failure_count} neuspjesno.")
    print("-" * 100)