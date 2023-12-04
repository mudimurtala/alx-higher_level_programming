#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_d = abs(number) % 10
print(f"Last digit of {number} is {last_d}", end=" ")
if last_d > 5:
    print("and is greater than 5")