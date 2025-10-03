import pytest 
from calculator import add, sub

# Minden tesztfüggvény neve test_-tel kezdődik,
# így a pytest automatikusan felismeri őket

def test_add():
    assert add(3, 4) == 2

def test_sub():
    assert sub(3, 4) == 2