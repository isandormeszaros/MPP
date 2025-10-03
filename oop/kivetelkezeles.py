"""Írj egy osztás függvény, amely két egész paramétert 
vár (a és b) és visszatérési értéke pedig az a/b hányados
Ha nem egész típusú paraméterkeet kapunk vagy 
ha nullával szeretnénk osztani, dobjuk kivételt"""

def osztas(a, b):
    if isinstance(a, int) and isinstance(b, int):
        if b == 0:
            raise ZeroDivisionError("Nullával nem osztunk")
        else:
            return a / b
    raise TypeError("Egész paramétert adj meg")

# Több exception ág esetén a legelső, a dobott kivétel típusára illeszkedő

try: 
    print(osztas(a = 1, b = 2))
    print(osztas(a = 5, b = 0))
    print(osztas(a = 1, b = 2.2))
except ZeroDivisionError as e:
    print(e)
except TypeError as e:
    print(e)
except Exception as e:
    print(e)