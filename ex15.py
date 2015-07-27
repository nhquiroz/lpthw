#!/usr/bin/python

# <--- modules needed --->

from sys import argv


# <--- beginning of the script --->

filename = argv[1]         # filename = 'ex15_sample.txt'
text_file = open(filename)

print("Here's your file %r:") % filename
print(text_file.read())
text_file.close()

print("Type the filename again:")
filename_again = raw_input("> ")

text_file_again = open(filename_again)
print(text_file_again.read())
text_file_again.close()
