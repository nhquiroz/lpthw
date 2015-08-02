#!/usr/bin/python


def add(a, b):
    print("ADDING {0:d} + {1:d}".format(a, b))
    return a + b


def substract(a, b):
    print("SUBSTRACTING {0:d} - {1:d}".format(a, b))
    return a - b


def multiply(a, b):
    print("MULTIPLYING {0:d} * {1:d}".format(a, b))
    return a * b


def divide(a, b):
    print("DIVIDING {0:d} / {1:d}".format(a, b))
    return a / float(b)


print("Let's do some math with just functions!")

age = add(30, 5)
height = substract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print("Age: {0:d}, Height: {1:d}, Weight: {2:d}, IQ: {3:d}".format(age,
                                                                   height,
                                                                   weight,
                                                                   iq))

# A puzzle for the extra credit, type it in anyway.
print("Here's a puzzle.")

what = add(age, substract(height, multiply(weight, divide(iq, 2))))

print("That becomes: ", what, "Can you do it by hand?")
