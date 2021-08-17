import random

myArr = ["rock", "paper", "scissors"]

randomInt = random.randint(0, 2)
computer = myArr[randomInt]

person = input("write rock, paper or scissors: ")
print("computer:", computer)

if person == computer:
  print("Tie!")
elif person == "rock":
  if computer == "scissors":
    # person wins
    print("You Win!")
  else:
    # computer wins
    print("You Lose!")
elif person == "paper":
  if computer == "rock":
    # person wins
    print("You Win!")
  else:
    # computer wins
    print("You Lose!")
else:
  if computer == "paper":
    # person wins
    print("You Win!")
  else:
    # computer wins
    print("You Lose!")