#!/usr/bin/python

# <--- modules needed --->

from sys import argv


# <--- beginning of the script --->

filename = argv[1]         # filename = 'ex15_sample.txt'
with open(filename) as text_file:
    content = text_file.read()
    print("Here's your file %r:") % filename
    print(content)

print("Type the filename again:")
filename_again = raw_input("> ")

with open(filename_again) as text_file_again:
    content = text_file_again.read()
    print(content)
