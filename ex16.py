from sys import argv

filename = argv[1]

print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you agree, hit RETURN."
raw_input('?')

print "Opening the file..."
target = open(filename, 'w')

print "Truncating the file %r. Goodbye!" % filename
target.truncate()

print "Now I'm going to ask you for three lines."
line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."
target.write(line1 + '\n')
target.write(line2 + '\n')
target.write(line3 + '\n')

print "And finally, we close it."
target.close()
