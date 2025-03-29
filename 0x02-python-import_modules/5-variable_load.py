#!/usr/bin/python3
if __name__ == "__main__":
    from variable_load_5 import a
    print(a)


#!/usr/bin/python3
if __name__ == "__main__":
    
    import sys

    argv = sys.argv
    no_of_argvs = len(argv) - 1
    if no_of_argvs == 0:
        print("0 arguments.")
    elif no_of_argvs == 1:
        print("1 argument:")
    else:
        print("<count> arguments:")


