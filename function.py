# # Default parameters
# # If no argument is passed, "World" will be used as the default value
# def hello(to="World"):
#     # to is a parameter of the hello function
#     print("Hello,",to)


# # If you call a function, it must already be defined by the time you call it. Otherwise, you'll get a NameError.
# hello() # prints "Hello, World"

# name = input("What's your name? " )

# # name is an argument to the hello function
# hello(name)


# def main(): 
#     name = input("What's your name? ")
#     hello()
    
# def hello():
#     # name is a variable defined in the main function
#     # It is not accessible here, because it is out of scope. Scope is the region of the program where a variable is accessible.
#     print(name)

# main()


# def main(): 
#     name = input("What's your name? ")
#     hello(name)
    
# def hello(to="World"):
#     print("Hello,",to)

# main()



def main(): 
    name = input("What's your name? ")
    def hello():
        # name is accessible here because it is in the same scope as the hello function
        return "Hello " + name
    print(hello())
    
main()
