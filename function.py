# Default parameters
# If no argument is passed, "World" will be used as the default value
def hello(to="World"):
    # to is a parameter of the hello function
    print("Hello,",to)


hello() # prints "Hello, World"

name = input("What's your name? " )

# name is an argument to the hello function
hello(name)
