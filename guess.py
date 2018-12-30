import random
import datetime


now = datetime.datetime.now()
if now.hour<6 :
    print(" Hello...!! Good Morning ")
else:
    print("Hello....!!! Good Evening ")
print("What's  your name?")
name=input()
print("Welcome "+name+" now we are going to play a guess game (between 1-100)")
secretnumber=random.randint(1,100)
print("Take Guess")
for i in range(1,7):
    print("You have "+str(7-i)+" left")
    guess=int(input())
    if guess < secretnumber:
        print("too low")
    elif guess > secretnumber:
        print("too high")
    else:
        break

if guess == secretnumber:
    print("You guessed "+str(secretnumber)+" was correct Great Job!! "+name)
else:
    print(name+" Better luck next time . The number i was thinked is "+str(secretnumber))    
