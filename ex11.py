#!/usr/bin/python

print("How old are you? (years):"),
age = raw_input()
print("How tall are you? (centimetres):"),
height = raw_input()
print("How much do you weigh? (kilograms):"),
weight = raw_input()

print("So, you're %r old, %r tall and %r heavy.") % (age, height, weight)
