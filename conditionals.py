# x = int(input("What's x? "))
# y = int(input("What's y? "))


# if x < y:
#     print("x is less than y")
# elif x > y:
#     print("x is greater than y")
# else:
#     print("x is equal to y")


# if x < y or x > y:
#     print ("x is not equal to y")
# else:
#     print("x is equal to y")


# if x != y:
#     print("x is not equal to y")
# else:
#     print("x is equal to y")


score = int(input("Score: "))

# if score >= 90 and score <=100:
#     print("Grade A")
# elif score >= 80 and score < 90:
#     print("Grade B")
# elif score >= 70 and score < 80:
#     print("Grade C")
# else:
#     print("Grade F")


# if 90 <= score <= 100:
#     print("Grade A")
# elif 80 <= score < 90:
#     print("Grade B")
# elif 70 <= score < 80:
#     print("Grade C")
# else:
#     print("Grade F")


# if score >= 90:
#     print("Grade A")
# elif score >= 80:
#     print("Grade B")
# elif score >= 70:
#     print("Grade C")
# else:
#     print("Grade F")


def main(): 
    print(is_even())

def is_even():
    return True if score % 2 == 0 else False
    
main()