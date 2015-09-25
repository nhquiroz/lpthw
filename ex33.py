#!/usr/bin/python

a_number = 0
a_list_of_numbers = []

while a_number < 6:
    print("At the top i is {:d}".format(a_number))
    a_list_of_numbers.append(a_number)

    a_number += 1
    print("Numbers now: ", a_list_of_numbers)
    print("At the bottom a_number is {:d}".format(a_number))

print("The numbers: ")

for number in a_list_of_numbers:
    print(number)
