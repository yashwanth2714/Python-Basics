# i = 0

# while i < 3:
#     print("hola", i, sep="-")
#     i = i + 1
    

# for i in [0,1,2]:
#     print("hello", i, sep="*")
    
    
# # range function generates a sequence of numbers
# # range(3) generates numbers from 0 to 2
# # range(start, stop) generates numbers from start to stop-1. For example, range(1,4) generates 1,2,3
# # range(start, stop, step) generates numbers from start to stop-1 with a step. For example, range(1,10,2) generates 1,3,5,7,9
# for i in range(3):
#     print("hi", i, sep="_")
    
    
# # _ is a throwaway variable
# # It is used when you don't need the variable. For example, when you just want to repeat something a certain number of times
# for _ in range(3):
#     print("hey")


# # You can multiply strings in Python
# # prints "meowmeowmeow"
# print("meow" * 3)


# # end="" prevents the extra newline that print adds by default
# print("meow\n" * 3, end="")


# # Ask user for a positive integer. Keep asking until they provide a positive integer.
# # This is a common pattern for input validation.
# while True:
#     n= int(input("What's n? "))
#     if n > 0:
#         break
    
# for _ in range(n):
#     print("meow")

def getNumber():
    while True:
        n = int(input("What's n? "))
        if n > 0:
            # return breaks out of the function and loop is also exited because return exits the function
            return n

def main():
    number= getNumber()
    meow(number)
    
def meow(n):
    for _ in range(n):
        print("meow")
    
main()
