#!/usr/bin/python

# <--- modules needed --->

from sys import argv


# <--- beginning of the script --->

input_file = argv[1]


def print_all(file):
    print file.read()


def rewind(file):
    file.seek(0)


def print_a_line(line_count, file):
    print line_count, file.readline()


current_file = open(input_file)

print("Fist let's print the whole file:\n")
print_all(current_file)

print("Now let's rewind, kind of like a tape.")
rewind(current_file)

print("Let's print three lines:")

current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)
