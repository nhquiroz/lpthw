#!/usr/bin/python

print("How old are you? (years):"),
age = raw_input()
print("How tall are you? (centimetres):"),
height = raw_input()
print("How much do you weigh? (kilograms):"),
weight = raw_input()

print("So, you're {0!r} old, {1!r} tall and {2!r} heavy.".format(age,
                                                                 height,
                                                                 weight))
