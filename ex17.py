#!/usr/bin/python

# <--- modules needed --->

from sys import argv
from os.path import exists


# <--- beginning of the script --->

source_file, target_file = argv[1], argv[2]

print("Copying from {0!r} to {1!r}.".format(source_file, target_file))

with open(source_file) as input_file:
    content = input_file.read()
    print("The input file is {:d} bytes long.".format(len(content)))

print("Does the output file exist? {!r}".format(exists(target_file)))
print("Ready. Hit RETURN to continue or CTRL-C to abort.")
raw_input('> ')

with open(target_file, 'w') as output_file:
    content = output_file.read()
    content.write(input_file)

print("Alright, all done.")
