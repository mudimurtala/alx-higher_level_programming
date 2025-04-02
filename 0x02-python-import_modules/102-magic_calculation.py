#!/usr/bin/python3
from magic_calculation_102 import add, sub


def magic_calculation(a, b):
    if a < b:
        c = add(a, b)
        for i in range(4, 6):
            c = add(c, i)
        return c
    else:
        return sub(a, b)


print(magic_calculation(2, 3))  # Should add 2 + 3, then add 4 and 5
print(magic_calculation(5, 3))  # Should return 5 - 3 (subtraction)
print(magic_calculation(10, 20))  # Should add 10 + 20, then add 4 and 5