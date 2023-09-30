#!/usr/bin/env python3

def happy_new_year():
    i = 10
    while i>0:
        print(i)
        i-=1
    print("Happy New Year!")

happy_new_year()


def square_integers(int_list):
    square_integers = []
    for num in int_list:
        square_integers.append(num ** 2)
    return square_integers

#Usage Example
int_list = [1,2,3,4,5]
result = square_integers(int_list)
print(result)

def fizzbuzz():
    for i in range(1, 101):
        if i % 3 ==0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

fizzbuzz()
