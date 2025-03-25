#!/usr/bin/python3
for ch in range(26):
    if ch % 2 == 0:
        print("{:c}".format(122 - ch), end="")
    else:
        print("{:c}".format(90 - ch), end="")


#!/usr/bin/python3
for i in range(122, 96, -1):
    if i % 2 == 0:
        print("{}".format(chr(i)), end="")
    else:
        print("{}".format(chr(i - 32)), end="")
