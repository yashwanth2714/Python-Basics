# try:
#     x = int(input("What's x? "))
# except ValueError:
#     print("x is not an integer")
    
# # when you enter a non-integer value, the program will not crash. Instead, it will print "x is not an integer"
# # But, the variable x will not be defined if the user enters a non-integer value because the assignment to x is inside the try block. And, if an exception occurs, the assignment is skipped.
# print(f"x is {x}")


# try:
#     x = int(input("What's x? "))
# except ValueError:
#     print("x is not an integer")
# else:
#     # else block is executed if no exception occurs in the try block. If an exception occurs, the else block is skipped.
#     print(f"x is {x}")
# finally:
#     # finally block is always executed, regardless of whether an exception occurs or not. It is typically used for cleanup actions.
#     print("This is the finally block. It is always executed.")


# # Keep asking the user for an integer until they provide a valid integer
# while True:
#     try:
#         x = int(input("What's x? "))
#     except ValueError:
#         # if a ValueError occurs, print the message and continue the loop to ask for input again
#         print("x is not an integer")
#     else:
#         # if no exception occurs, break out of the loop
#         break

# # prints the valid integer provided by the user
# print(f"x is {x}")


def main():
    x = get_int("What's x? ")
    print(f"x is {x}")

def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            # pass means do nothing. It is a placeholder when a statement is required syntactically but you don't want to do anything.
            # The difference between pass and continue is that continue skips the rest of the loop and goes to the next iteration, whereas pass does nothing and the loop continues normally. For example, if you had some code after the try-except block, using continue would skip that code, whereas pass would allow that code to run.
            pass
        print("after the except block")
            
main()
