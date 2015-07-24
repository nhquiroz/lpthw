from sys import argv

filename  = argv[1]         # script = ex15_sample.txt
text_file = open(filename)

print "Here's your file %r:" % filename
print text_file.read()

print "Type the filename again:"
filename_again = raw_input("> ")

text_file_again = open(filename_again)
print text_file_again.read()
