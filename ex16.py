#!/usr/bin/python

# <--- modules needed --->

from sys import argv


# <--- beginning of the script --->

filename = argv[1]

print("We're going to erase {!r}.".format(filename))
print("If you don't want that, hit CTRL-C (^C).")
print("If you agree, hit RETURN.")
raw_input('?')

print("Opening the file...")
with open(filename, 'w') as target:
    print("Truncating the file {!r}. Goodbye!".format(filename))
    target.truncate()

print("Now I'm going to ask you for three lines.")
line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print("I'm going to write these to the file.")
new_file_content = line1 + '\n' + line2 + '\n' + line3 + '\n'
target.write(new_file_content)
