#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = number % 10 if number >= 0 else -(-number % 10)  # Keeps correct sign

if last_digit > 5:
    print(f"Last digit of {number} is {last_digit} and is greater than 5\n")
elif last_digit == 0:
    print(f"Last digit of {number} is {last_digit} and is zero\n")
else:
    print(f"Last digit of {number} is {last_digit} and is less than 6 and not zero\n")
