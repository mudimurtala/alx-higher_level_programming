#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_d = abs(number) % 10
print(f"Last digit of {number} is", end=" ")
if number < 0:
    print(f"{-last_d}", end=" ")
else:
    print(f"{last_d}", end=" ")

if last_d == {-last_d}:
    print("and is less than 6 and not 0")
elif last_d > 5:
    print("and is greater than 5")
elif last_d == 0:
    print("and is 0")
else:
    print("and is less than 6 and not 0")
