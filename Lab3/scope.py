'''
The LEGB Rule
Python follows the LEGB rule for variable resolution:

Local: The innermost scope (local variables).
Enclosing: Any enclosing function scopes (for nested functions).
Global: The module-level scope (global variables).
Built-in: The built-in scope (functions and names).
'''


x = 2

def scope1(x):
    x = x + 1
    return x

print(x, scope1(2), x)  


def scope2():
    global x
    x = x + 1

print(x, scope2(), x)

def scope3(x):
    global y
    y = x + 1

print(x, scope3(2), y)

