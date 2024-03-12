"""
Takes some code as a string and displays the abstract syntax tree (AST)
produced after parsing it.
"""
import ast

code = """
def greet(name):
    print("Hello " + name)
"""  # Code to execute

tree = ast.parse(code)

print(ast.dump(tree, indent=4))

