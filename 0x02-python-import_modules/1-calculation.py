#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    a = 10
    b = 5
    operations = [add, sub, mul, div]
    for i in operations:
        print("{} {} {} = {}".format(a, "?", b, i(a, b)))
