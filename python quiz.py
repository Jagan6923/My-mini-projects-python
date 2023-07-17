print("Welcome to My Quiz!!")
quiz=input("Do you want to play?(Yes/Quit)")

if quiz.lower() != 'yes':
  print("quit")
print("Okayy Let's Play :) ")

score=0

ans=input("Who developed Python Programming Language?")
if ans.lower()=='guido van rossum':
  print("Correct!!")
  score=score+1
else:
  print("Incorrect!!")

ans=input("Which type of Programming does Python support?")
if ans.lower()=='object oriented programming':
  print("Correct!!")
  score=score+1
else:
  print("Incorrect!!")

ans=input("Is Python case sensitive when dealing with identifiers?")
if ans.lower()=='yes':
  print("Correct!!")
  score=score+1
else:
  print("Incorrect!!")

ans=input("Which of the following is the correct extension of the Python file?")
if ans.lower()=='.py':
  print("Correct!!")
  score=score+1
else:
  print("Incorrect!!")

ans=input("Which keyword is used for function in Python language?")
if ans.lower()=='def':
  print("Correct!!")
  score=score+1
else:
  print("Incorrect!!")


print("You Scored " + str(score) +" in my quiz")
print("The percentage is "+ str((score/5)*100)+'%')


