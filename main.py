import random as r 
import pswd

tries=1
mainPass="admin"
userPass=input("enter your password: ")

while mainPass!=userPass:
    tries+=1
    userPass=input("wrong password, try again: ")
    if tries > 4:
        break

if tries > 4:    
    print("you are temporarily blocked from the system.")
else:
    a=str(pswd.password())
    print(a)
    auth=input("phase 1 successful, now please enter the code: ")
    if a==auth:
        print("1. Welcome back!")
            

while a!=auth:
    a=pswd.password()
    print(a)
    auth=input("wrong password, try again: ")
    if a==auth:
        print("2. Welcome back!")
        break

