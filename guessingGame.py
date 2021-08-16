import random

print("I'm thinking of a number 1 to 10, try to guess my number.")
mySecretNumber = random.randint(1, 10)
tries = 0

while True:
  guess = int(input("Enter guess: "))
  tries += 1

  if guess == mySecretNumber:
    print("You guessed the number in", tries, "tries!")
    break
  else:
    print("Sorry, try again")
