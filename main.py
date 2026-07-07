import os
from antlr4 import *
from parser.PlantUMLLexer import PlantUMLLexer
from parser.PlantUMLParser import PlantUMLParser
from parser.PlantUMLVisitor import PlantUMLVisitor


def print_tokens(filepath):
    input_stream = FileStream(filepath, encoding='utf-8')
    lexer = PlantUMLLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    token_stream.fill()

    print(f"\n--- Tokeni za: {filepath} ---")
    for token in token_stream.tokens:
        token_type_name = PlantUMLLexer.symbolicNames[token.type] if token.type != -1 else "EOF"
        print(f"Tekst: {token.text} Tip: {token_type_name}")


def main():
    examples_folder = "examples"

    if not os.path.isdir(examples_folder):
        print(f"Folder '{examples_folder}' ne postoji.")
        return

    for filename in sorted(os.listdir(examples_folder)):
        filepath = os.path.join(examples_folder, filename)

        if os.path.isfile(filepath):
            try:
                print_tokens(filepath)
            except Exception as e:
                print(f"Greska prilikom obrade fajla '{filepath}': {e}")


if __name__ == "__main__":
    main()