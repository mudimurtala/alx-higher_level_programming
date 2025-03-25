#!/usr/bin/python3
def fizzbuzz():
    for i in range(1, 101):
        if i % 3 == 0:
            i = 'Fizz'
            print("{}".format(i), end=" ")

fizzbuzz()