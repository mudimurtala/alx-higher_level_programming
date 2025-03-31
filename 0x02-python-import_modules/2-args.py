#!/usr/bin/python3
if __name__ == "__main__":

    import sys

    argv = sys.argv
    no_of_argvs = len(argv) - 1
    for i, arg in enumerate(argv[1:], 1):
        if no_of_argvs == 0:
            print("{}: {}".format(i, arg))
        elif no_of_argvs == 1:
            print("1 argument:")
        else:
            print("{} arguments:".format(no_of_argvs))
