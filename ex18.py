#!/usr/bin/python


def print_two_arguments(*args):
    arg1, arg2 = args   # unpacking arguments to variables
    print("arg1: %r, arg2: %r") % (arg1, arg2)


def print_two_arguments_again(arg1, arg2):   # better than the previous version
    print("arg1: %r, arg2: %r") % (arg1, arg2)


def print_one_argument(arg):
    print("arg: %r") % arg


def print_without_arguments():
    print("I got nothin'.")


print_two_arguments("Zed", "Shaw")
print_two_arguments_again("Monty", "Python")
print_one_argument("Snakes")
print_without_arguments()
