#!/usr/bin/python


def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates


start_point = 10000
beans, jars, crates = secret_formula(start_point)

print("With a starting point of: {:d}".format(start_point))
print("We'd have {0:d} beans, {1:d} jars, and {2:d} crates.".format(beans,
                                                                    jars,
                                                                    crates))

start_point = start_point / 10

print("We can also do that this way:")
print("We'd have {0:d} beans, {1:d} jars, and {2:d} crates.".format(
      *secret_formula(start_point)))
