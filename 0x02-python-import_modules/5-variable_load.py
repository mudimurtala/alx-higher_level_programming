#!/usr/bin/python3
if __name__ == "__main__":
    from variable_load_5 import a
    print(a)


#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    a = 10
    b = 5
    for i in calculator_1:
        print("{} + {} = {}".format(a, b, i(a, b)))


