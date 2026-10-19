# '''
# Project 1 : Snake Water Gun Game  --- jsut like rock, paper, scissors game


# We all have played snake, water gun game in our childhood. If you haven’t,
# google the rules of this game and write a python program capable of playing
# this game with the user.

# '''


# '''
# rock = 1
# paper = 0
# scissors = -1

# '''


# import random

# computer = random.choice([0,-1,1])

# gameElements = {
#     "r":"Rock",
#     "p":"Paper",
#     "s":"Scissors"
# }

# print("\n")
# print("Chose your inputs as key from here : ", gameElements)

# userInput = (input("Enter your choice : "))

# dict = {
#     "r":1,
#     "p":0,
#     "s":-1
# }

# reverseDict = {1:"Rock", -1:"Scissors", 0:"Paper" }

# yourChoice = dict[userInput]

# a = computer
# b = yourChoice



# # game logic--
# if(a == b):
#     print("Game draw!")

# else:
#     if(a == 1  and  b == 0):
#         print("Wow! You WON.")
        
#     elif(a == 1  and  b == -1):
#         print("Oh! You LOST.")

#     elif(a == 0  and  b == -1):
#         print("Wow! You WON.")

#     elif(a == 0  and  b == 1):
#         print("Oh! You LOST.")
        

#     elif(a == -1  and  b == 0):
#         print("Oh! You LOST.")
        

#     elif(a == -1  and  b == 1):
#         print("Wow! You WON.")

#     else:
#         print("something went wrong!")
        

# print(f"Computer choice is: {reverseDict[computer]} and Your choice is: {gameElements[userInput]}")









'''

Practice Set  --- file I/O

1. Write a program to read the text from a given file ‘this.txt’ and find out whether it
contains the word ‘twinkle’.

2. The game() function in a program lets a user play a game and returns the score as an
integer. You need to read a file which is either blank or contains the previous
Hi-score. You need to write a program to update the Hi-score whenever the game()
function breaks the Hi-score.

3. Write a program to generate multiplication tables from 2 to 20 and write it to the different
files. Place these files in a folder for a 13-year-old.

4. A file contains a word “Donkey” multiple times. You need to write a program which
replaces this word with ##### by updating the same file.

5. Repeat program 4 for a list of such words to be censored.

6. Write a program to mine a log file and find out whether it contains ‘python’.

7. Write a program to find out the line number where python is present from ques 6.
8. Write a program to make a copy of a text file “this.txt”.
9. Write a program to find out whether a file is identical and matches the content of another
file.
10. Write a program to wipe out the content of a file using python.
11. Write a python program to rename a file to “renamed_by_python.txt”.

'''


# # ------------- Q1 ----------------
# with open("this.txt") as f:

#     text = f.read()
#     if("twinkle" in text):
#         print(f"Yes! the word {"twinkle"} is there in this.text file")
#     else:
#         print(f"No! the word {"twinkle"} is not there in this.text file")

# # print(text, type(text))



# # ------------- Q2 ----------------

# def game():
#     print("we are playing high number guessing game...")
#     n = int(input("Enter your number between 1-50: "))

#     # fetch the prev score-
#     with open("file.txt") as f:
#         high_score = f.read()
#         if(high_score != ""):
#             high_score = int(high_score)
#         else:
#             high_score = 0

#     if(n>high_score):
#         # write in file or update...
#         with open("file.txt", "w") as f:
#             f.write(str(n))

#         print("You WON! your guess is high...")
#     else:
#         print("ohh you LOST! your guess is low...")


# game()
            




# # ------------- Q3 ----------------

# def generate_table(n):
#     table = ""
#     for i in range(1,11):
#         table+= f"{n} * {i} = {n*i}\n"

#     with open(f"tables/table_{n}.txt", "w") as f:
#         f.write(table)



# for i in range(2,21):
#     generate_table(i)







# # ------------- Q4 ----------------
# with open("this.txt", "r") as f:
#     content = f.read()

# updated_content = content.replace("Donkey", "#####")

# with open("this.txt", "w") as f:
#     f.write(updated_content)
    





# # ------------- Q5 ----------------

# censored = ["Donkey", "monkey", "hey"]

# with open("this.txt", "r") as f:
#     content = f.read()

# for word in censored:
#     content = content.replace(word, "#"*(len(word)))



# with open("this.txt", "w") as f:
#     f.write(content)
    





# # ------------- Q6 ----------------
# with open("this.txt", "r") as f:
#     content = f.read()

# if "python" in content:
#     print("Yes! python is present in the file.")
# else:
#     print("No! python is not present in then file.")





# # ------------- Q7 ----------------
# cnt = 1

# with open("this.txt", "r") as f:

#    all_lines = f.readlines()

# for line in all_lines:
#     if "python" in line:
#         print(f"Yes, python is present at line no. - {cnt}")
#         break
#     cnt+=1


# else:     #  else tabhi chalega jab pura for loop chal gaya khatam ho gaya then......
#     print("No, python is not present in the file at any line.")
        





# # ------------- Q8 ----------------
# with open("this.txt", "r") as f:
#     content = f.read()

# with open("this2.txt", "w") as f:
#     f.write(content)





# # ------------- Q9 ----------------
# with open("this.txt", "r") as f:
#     file1 = f.read()

# with open("this2.txt", "r") as f:
#     file2 = f.read()

# if file1 == file2:
#     print("Yes! both file has same content.")
# else:
#     print("No! both files are not same.")





# # ------------- Q10 ----------------
# with open("this2.txt", "w") as f:
#     f.write("")



# ------------- Q11 ----------------

# method:1 -- firstly copy the content of the file to another and name that new like rename that new ... this is optimal way--


# # method:2 -- import os and then rename...
# import os

# current_name = "this.txt"
# new_name = "renamed_by_python.txt"

# os.rename(current_name, new_name)
# print(f"successfully renamed {current_name} to {new_name}")

