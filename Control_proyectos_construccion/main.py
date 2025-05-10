from antlr4 import *
from antlr4.error.ErrorListener import ErrorListener
from CSVFilterLexer import CSVFilterLexer
from CSVFilterParser import CSVFilterParser
from MyCSVVisitor import MyCSVVisitor

# Definición del listener personalizado
class CustomErrorListener(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        print(f"Error en línea {line}, columna {column}: {msg}")

# Ejecutar el script
input_stream = FileStream("programa.dsl", encoding='utf-8')
lexer = CSVFilterLexer(input_stream)
stream = CommonTokenStream(lexer)
parser = CSVFilterParser(stream)

# Configurar manejo de errores antes de ejecutar el parser
parser.removeErrorListeners()
parser.addErrorListener(CustomErrorListener())

tree = parser.prog()
visitor = MyCSVVisitor()
visitor.visit(tree)
