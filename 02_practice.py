'''
Project 1 : Snake Water Gun Game  --- jsut like rock, paper, scissors game


We all have played snake, water gun game in our childhood. If you haven’t,
google the rules of this game and write a python program capable of playing
this game with the user.

'''


'''
rock = 1
paper = 0
scissors = -1

'''


import random

computer = random.choice([0,-1,1])

gameElements = {
    "r":"Rock",
    "p":"Paper",
    "s":"Scissors"
}

print("\n")
print("Chose your inputs as key from here : ", gameElements)

userInput = (input("Enter your choice : "))

dict = {
    "r":1,
    "p":0,
    "s":-1
}

reverseDict = {1:"Rock", -1:"Scissors", 0:"Paper" }

yourChoice = dict[userInput]

a = computer
b = yourChoice



# game logic--
if(a == b):
    print("Game draw!")

else:
    if(a == 1  and  b == 0):
        print("Wow! You WON.")
        
    elif(a == 1  and  b == -1):
        print("Oh! You LOST.")

    elif(a == 0  and  b == -1):
        print("Wow! You WON.")

    elif(a == 0  and  b == 1):
        print("Oh! You LOST.")
        

    elif(a == -1  and  b == 0):
        print("Oh! You LOST.")
        

    elif(a == -1  and  b == 1):
        print("Wow! You WON.")

    else:
        print("something went wrong!")
        

print(f"Computer choice is: {reverseDict[computer]} and Your choice is: {gameElements[userInput]}")
