name=input("Type your name: ")
print("Welcome",name,"to the jagan's adventure!!..")

answer=input("You are in a dark forest,you can go left or right. \nWhich way would you like to go??(left/right)")
if answer.lower()== "left":
  answer=input("You come to a house.(go/pass) ")
  if answer=="go":
    print("There is a dangerous dog!!!!,that kills you,you lost the game")
  elif answer=="pass":
    print("You walked for many miles,ran out of water and you lost the game")
  else:
    print("Not a valid option.you lose")

elif answer.lower()== "right":
  answer=input("There is a Hotel(go/pass)")
  if answer=="go":
    answer=input("There is a man with a weapon(meet/pass)")
    if answer=="meet":
      print("He gave the bag of money ,you won")
      print("Well Done!!")
    elif answer=="pass":
      print("you did not complete task,you lost")
    else:
      print("Not a valid option.you lose")
  elif answer=="pass":
    print("You walked for many miles,ran out of water and you lost the game")
  else:
    print("Not a valid option.you lose")

print("Thanks for playing..",name)
