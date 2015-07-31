#!/usr/bin/python

# <--- modules needed --->

from sys import argv


# <--- beginning of the script --->

script = argv[0]
user_name = argv[1]
prompt = '> '

print("Hi {0}, I'm the {1} script.".format(user_name, script))
print("I'd like to ask you a few questions.")
print("Do you like me {}?".format(user_name))
likes = raw_input(prompt)

print("Where do you live {}?".format(user_name))
lives = raw_input(prompt)

print("What kind of computer do you have?")
computer = raw_input(prompt)

print("""
Alright, so you said {0!r} about liking me.
You live in {1!r}. Not sure where it is.
And you have a {2!r} computer. Nice.
""".format(likes, lives, computer))
