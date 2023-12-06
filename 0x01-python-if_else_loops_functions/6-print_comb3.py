#!/usr/bin/python3
#for i in range(0, 100):
#    if i != 99:
#        print("{:02d}, ".format(i), end="")
#    else:
#        print("{}".format(99), end="\n")

#for i in range(0, 10):
#    print("{:02d}, ".format(''.join(map(str, i + 1))), end="")

for i in range(10):
    for j in range(i + 1, 10):  # Start j from i+1 to avoid duplicates and self-pairs
        combination = f"{i}{j}"
        if i < 9 or j < 9:  # Check if it's not the last combination
            print(combination, end=", ")
        else:
            print(combination, end="\n")
        print("\n")