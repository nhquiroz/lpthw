#!/usr/bin/python

my_name = "Nico"
my_age = 23
my_height = 184
my_weight = 72
my_eyes = "green"
my_hair = "brown"

print("Let's talk about {}.".format(my_name))
print("He's {:d} centimetres tall.".format(my_height))
print("He's {:d} years old.".format(my_age))
print("He weights {:d} kilos.".format(my_weight))
print("His eyes are {0} and his hair {1}".format(my_eyes, my_hair))

print("If I add {0:d}, {1:d}, and {2:d} I get {3:d}.".format(my_age, my_height,
                                                             my_weight,
                                                             my_age +
                                                             my_height +
                                                             my_weight))
print("Bye!")
