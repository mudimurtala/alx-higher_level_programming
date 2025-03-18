#!/usr/bin/python3
for i in range(0, 10):
    for j in range(i + 1, 10):  # Start j from i + 1 to ensure unique pairs
        if i == 8 and j == 9:  # Ensuring no trailing comma for last pair
            print("{}{}".format(i, j))
        else:
            print("{}{}".format(i, j), end=", ")
