# try:
#     x = int(input("What's x? "))
# except ValueError:
#     print("x is not an integer")
    
# # when you enter a non-integer value, the program will not crash. Instead, it will print "x is not an integer"
# # But, the variable x will not be defined if the user enters a non-integer value because the assignment to x is inside the try block. And, if an exception occurs, the assignment is skipped.
# print(f"x is {x}")


try:
    x = int(input("What's x? "))
except ValueError:
    print("x is not an integer")
else:
    # else block is executed if no exception occurs in the try block. If an exception occurs, the else block is skipped.
    print(f"x is {x}")
finally:
    # finally block is always executed, regardless of whether an exception occurs or not. It is typically used for cleanup actions.
    print("This is the finally block. It is always executed.")