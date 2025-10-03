def add(a,b):
    return a + b
def sub(a, b):
    return a - b
def mul(a, b):
    return a * b
def div(a, b):
    if b == 0:
        raise ZeroDivisionError("Division by zero")
    return a/b

assert (add(1, 2) == 3)
assert (sub(2, 3)) == -1

try:
    div(5, 0)
    assert False # Ide soha nem kellene eljutnia a programnak
except ZeroDivisionError:
    pass