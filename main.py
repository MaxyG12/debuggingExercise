import random

def game():
  attempts = 0
  number = random.randint(1,100)
  while True:
    guess = int(input("Pick a number between 1 and 100: "))
    if guess > number:
      print("Too high")
      attempts+=1
    elif guess < number:
      print("Too low")
      attempts+=1
    elif guess == number:
      print("\nYou got it!")
      attempts+=1
      print("It took you", attempts, "attempts.")
      break

while True:
  menu = input("\n1: Guess the random number game \n2: Exit\n> ")
  if menu == "1":
    game()
  else:
    break