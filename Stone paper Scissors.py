import random

user_wins=0
computer_wins=0
options=["stone","paper","scissors"]

while True:
  user_input=input("Type Stone/Paper/Scissors or Q to quit: " )
  if user_input.lower()=="q":
    break
  if user_input.lower() not in options:
    continue


  random_number=random.randint(0,2)
  #rock=0,paper=1.,scissors=2

  computer_pick=options[random_number]
  print("Computer poicked",computer_pick + ".")

  if user_input =="stone" and computer_pick=="scissors":
    print("You won!!")
    user_wins+=1

  elif user_input =="paper" and computer_pick=="stone":
    print("You won!!")
    user_wins+=1

  elif user_input =="scissors" and computer_pick=="paper":
    print("You won!!")
    user_wins+=1

  elif user_input == computer_pick:
    print("You won!!")
    user_wins+=1

  else:
    print("You lost")
    computer_wins+=1

print("You won",user_wins,"times")
print("Computer won",computer_wins,"times")
print("Goodbye..")
