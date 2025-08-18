print("Hell\"o\"","World" + "!")

# Ask user for their name
name = input("What's your name? ")

# Remove any leading or trailing whitespace
name = name.strip()

# Capitalize the first letter of the name
# name = name.capitalize()

# Convert the name to title case
# This will capitalize the first letter of each word in the name
name = name.title()

# Destructuring the name into first and last
first, last = name.split(" ")

"""
Multi-line Comment:

Say hello
to the user
"""

# separator and end parameters in print function
# sep="--" means that the separator between items will be "--" instead of a space which is the default
# end="Good " means that the end of the print statement will be "Good " instead of a newline
print("Hello,", name , "!", sep="--", end="Good ")

# f-string for formatted string literals
# f-string allows you to embed expressions inside string literals, using curly braces {}
print(f"Bye {first} {0 + 1} th")
