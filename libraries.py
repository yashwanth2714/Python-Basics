from random import choice, randint, shuffle

# choice is 
coin = choice(["heads", "tails"])
print(coin)


# randint returns a random integer between the two numbers (inclusive)
print(randint(1, 6))


cards = ["Jack", "Queen", "King", "Ace"]
# shuffle is an in-place shuffle, it modifies the original list
shuffle(cards)
print(cards)