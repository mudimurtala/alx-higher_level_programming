#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div

    operators = ["+", "-", "*", "/"]
    functions = [add, sub, mul, div]

    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    op = sys.argv[2]
    if sys.argv[2] not in operators:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    a = int(sys.argv[1])
    b = int(sys.argv[3])

    for i in range(len(operators)):
        if op == operators[i]:
            result = functions[i](a, b)
            print("{} {} {} = {}".format(a, op, b, result))
            break
