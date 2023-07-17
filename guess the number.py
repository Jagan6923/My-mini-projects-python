import random

user=input("Type a Number: ")
if user.isdigit():
  user=int(user)
  if user <=0:
    print("Please enter number larger than 0")
  else:
    quit()
else:
  print("Type a number next time")
  quit()

random=random.randint(1,user)
guesses=0

while True:
  guesses=guesses+1
  guess=input("Guess the Number: ")

  if guess.isdigit():
    guess=int(guess)
  else:
    print("Type a number next time")
    continue

  if guess==random:
    print("You got it :) ")
    break
  elif guess>random:
      print("your guess is high")
  else:
      print("your guess is small")

print("You  got is in",guesses,"guesses")