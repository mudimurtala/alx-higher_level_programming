#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div
    operator = ["+", "-", "*", "/"]

    if len(sys.argv) != 4:
        print('More than three arguments')
        sys.exit(1)
    if sys.argv[2] not in operator:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    
    a = int(sys.argv[1])
    b = int(sys.argv[3])

    if sys.argv[2] == '+':
        print("{} {} {} = {}".format(a, '+', b, add(a,b)))
    elif sys.argv[2] == '-':
        print("{} {} {} = {}".format(a, '-', b, sub(a,b)))
    elif sys.argv[2] == '*':
        print("{} {} {} = {}".format(a, '*', b, mul(a,b)))
    else:
        print("{} {} {} = {}".format(a, '/', b, div(a,b)))