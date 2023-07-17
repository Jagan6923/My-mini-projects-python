pwd=input("What is the Master password? ")

def view():
  with open('passwords12.txt','r') as f:
     for l in f.readlines():
       data=l.rstrip()
       user,passw=data.split('|')
       print("User Name:",user," Password:",passw)


def add():
  Name=input("Account Name: ")
  password=input("Password: ")

  with open('passwords12.txt','a') as f:
    f.write(Name + '|' + password +'\n')



while True:
  mode=input("Would you like to add new password or view the existing password? or press q to quit (add/view/q)").lower()
  if mode=="q":
    break
  elif mode=="view":
    view()
  elif mode=="add":
    add()
  else:
    print("Invalid mode")
    continue
