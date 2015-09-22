#!/usr/bin/python

the_count = [1, 2, 3, 4, 5]
fruits = ["apples", "oranges", "pears", "apricots"]
change = [1, "pennies", 2, "dimes", 3, "quarters"]

# this first kind of for-loop goes through a list
for number in the_count:
    print("This is count {:d}".format(number))

# same as above
for fruit in fruits:
    print("A fruit of type: {:s}".format(fruit))

# also we can go through mixed lists too
# notice we have to use %r since we don't know what's in it
for element in change:
    print("I got {!r}".format(element))

# we can also build lists, first start with an empty one
elements = []

# thay use the range function to do 0 to 5 counts
for number in range(0, 6):
    print("Adding {:d} to the list.".format(number))
    # append is a function that list understand
    elements.append(number)

# now we can print them out too
for element in elements:
    print("Element was: {:d}".format(element))
