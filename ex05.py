my_name   = "Nico"
my_age    = 23
my_height = 184
my_weight = 72
my_eyes   = "green"
my_hair   = "brown"

print("Let's talk about %s.")            % (my_name)
print("He's %d centimetres tall.")       % (my_height)
print("He's %d years old.")              % (my_age)
print("He weights %d kilos.")            % (my_weight)
print("His eyes are %s and his hair %s") % (my_eyes, my_hair)

# the next line is a little more tricky
print("If I add %d, %d, and %d I get %d.") % (my_age, my_height, my_weight, my_age + my_height + my_weight)
print("Bye!")
