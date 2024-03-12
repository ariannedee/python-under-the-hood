"""
Takes some code as a string and prints out the tokens.

To tokenize a file, run $ python3 –m tokenize <file.py>
"""
import io
import token
import tokenize

code = """
def greet(name):
    print("Hello " + name)
"""  # Code to execute

as_bytes = io.BytesIO(code.encode('utf-8'))  # Turn into encoded bytes
tokens = list(tokenize.tokenize(as_bytes.readline))  # Get tokens

# Print TokenInfo objects
for tok in tokens:
    print(tok)

print()

# Print summary of tokens
for tok in tokens:
    print(f"{token.tok_name[tok.exact_type]:<20}{tok.string}")
