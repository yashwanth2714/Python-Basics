name = input("Enter name: ")

match name:
    case "Apple":
        print ("It's a fruit")
    case "Carrot":
        print("It's a vegetable")
    case "Chicken":
        print("It's a meat")
    case _:
        print("I don't know what it is")