#!/usr/bin/python3
def fizzbuzz():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz", end=" ")
        elif i % 5 == 0:
            i = 'Buzz'
        elif i % 3 == 0:
            i = 'Fizz'
        print("{}".format(i), end=" ")
    print()

fizzbuzz()