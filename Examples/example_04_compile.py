from dis import disassemble

code_str = f"""
def greet(name):
    print('Hello ' + name)  

greet(world)
greet(hi)
"""

code = compile(code_str, '<string>', 'exec')

print(code)
print(code.co_code)    # Byte instructions
print(code.co_names)   # Names used in the code
print(code.co_consts)  # Constants/literals used in the code

disassemble(code)      # Display human-readable instructions
