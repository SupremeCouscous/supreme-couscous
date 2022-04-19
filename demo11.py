import ast

y1 = None
y2 = None
print(y1 == y2)

x1 = "None"
# x1 = "5+4j"
print(x1 == y1)
z1 = ast.literal_eval(x1)
print(type(z1), z1)
x2 = "None"
# x2 = 400
z2 = None if x2 == 'None' else x2
print(type(z2), z2)
# x3 = "None"
x3 = "15+13"
z3 = eval(x3)
print(type(z3), z3)
print(type(x1), x1)
~~~~~~~~~~~~~~~~~~~~~~
def twice(number: float) -> float:
    return 2 * number


print(twice(500))
print(twice(3.14))
print(twice("***"))