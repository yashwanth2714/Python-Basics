try:
    x = int(input("What's x? "))
except ValueError:
    print("x is not an integer")
    
# when you enter a non-integer value, the program will not crash. Instead, it will print "x is not an integer"
# But, the variable x will not be defined if the user enters a non-integer value because the assignment to x is inside the try block. And, if an exception occurs, the assignment is skipped.
print(f"x is {x}")
