#!/usr/bin/python

# <--- modules needed --->

from sys import argv
from os.path import exists


# <--- beginning of the script --->

source_file, target_file = argv[1], argv[2]

print("Copying from %r to %r.") % (source_file, target_file)

input_file = open(source_file).read()

print("The input file is %d bytes long.") % len(input_file)

print("Does the output file exist? %r") % exists(target_file)
print("Ready. Hit RETURN to continue or CTRL-C to abort.")
raw_input('> ')

output_file = open(target_file, 'w')
output_file.write(input_file)

print("Alright, all done.")
output_file.close()
