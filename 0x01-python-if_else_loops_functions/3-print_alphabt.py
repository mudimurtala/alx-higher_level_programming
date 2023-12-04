#!/usr/bin/python3
for i in range(97, 123,):
    alpha = chr(i)
    if alpha not in ['q', 'e']:
        print("{}".format(alpha), end="")
        