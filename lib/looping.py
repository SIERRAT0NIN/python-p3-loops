#!/usr/bin/env python3


def happy_new_year():
    # code goes here!
    i = 10
    while i > 0:
        print(i)
        i -= 1
    print("Happy New Year!")


happy_new_year()


def square_integers(int_list):
    # code goes here!
    return [num**2 for num in int_list]
    return [num]


def fizzbuzz():
    for i in range(1, 101):
        if not i % 15:
            print("FizzBuzz")
        elif not i % 5:
            print("Buzz")
        elif not i % 3:
            print("Fizz")
        else:
            print(i)


def fizzbuzz():
    for i in range(1,101):
        if not i % 15