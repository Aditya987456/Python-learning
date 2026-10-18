


# # Question -1: print poem

# # NOTE - to print multi line we use triple double quotes("""  """) or single triple quotes('''  ''')

# print("""


# Twinkle, twinkle, little star,
# How I wonder what you are!
# Up above the world so high,
# Like a diamond in the sky.

# When the blazing sun is gone,
# When he nothing shines upon,
# Then you show your little light,
# Twinkle, twinkle, all the night.

# Then the trav'ller in the dark,
# Thanks you for your tiny spark,
# He could not see which way to go,
# If you did not twinkle so.

# In the dark blue sky you keep,
# And often thro' my curtains peep,
# For you never shut your eye,
# Till the sun is in the sky.

# 'Tis your bright and tiny spark,
# Lights the trav'ller in the dark:
# Tho' I know not what you are,
# Twinkle, twinkle, little star.



# """)





# # Ques2: use repl and print the table of 5.

# # Ques3: install external module and use it to perform an operation of you interest.
# import pyttsx3
# engine = pyttsx3.init()

# engine.say("HIIIIIIIIIIIIIIIIIII")
# engine.runAndWait()




# # Quest4: Write a python program to print the contents of a directory using the os module.
# import os

# # Get the contents of the current directory
# contents = os.listdir("/home/aditya2981")

# for item in contents:
#     print(item)







'''

--------------------------basic question practice from the handbook - var and all...-----------------------------------------

1. Write a python program to add two numbers.
2. Write a python program to find remainder when a number is divided by z.
3. Check the type of variable assigned using input() function.
4. Use comparison operator to find out whether ‘a’ given variable is greater than ‘b’ or not.
Take a = 34 and b = 80
5. Write a python program to find an average of two numbers entered by the user.
6. Write a python program to calculate the square of a number entered by the user.


'''


# # ------------Q1---------------
# a = int(input("enter first number: "))
# b = int(input("enter second number: "))
# print("sum is : ", a+b)



# # ------------Q2---------------
# a = int(input("enter your dividend : "))
# b = int(input("enter you divisor : "))

# print("Remainder is : ", a%b)



# # ------------ Q3 ---------------
# anything = input("Give me any type of value:")  # btw this is always string...
# print(" the type of your given input is : ", type(anything))




# # ------------Q4---------------
# a = int(input("enter a : "))
# b = int(input("enter b : "))

# print("a is greater than b is ", a>b)


# # ------------Q5---------------
# a = int(input("enter first number: "))
# b = int(input("enter second number: "))

# print("Average of two number is ", (a+b)/2 )



# # ------------Q6---------------
# a = int(input("enter number: "))
# # print("Square number is ", (a*a) )
# print("Square number is ", (a**2) )




'''
Practice Set - basic question practice on string and all.

1. Write a python program to display a user entered name followed by Good Afternoon using
input() function.
2. Write a program to fill in a letter template given below with name and date.

letter = '''
# Dear <|Name|>,
# You are selected!
# <|Date|>
'''

3. Write a program to detect double space in a string.
4. Replace the double space from problem 3 with single spaces.
5. Write a program to format the following letter using escape sequence characters.
letter = "Dear Sir, this python course is nice. Thanks!"

'''


# # ------------Q1---------------

# userName = input("Enter your name: ")

# print(f"Good Afternoon {userName}")



# # ------------Q2---------------

# letter = letter = ''' Dear <|Name|>,
#                     You are selected!
#                     <|Date|>
# '''


# print(letter.replace("<|Name|>", "Aditya Raj").replace("<|Date|>", "13 October, 2026"))



# # ------------Q3---------------

# str = "aditya raj  jiii  hello"
# idx = str.find("  ")
# print(idx)


# # ------------Q4---------------
# str = "aditya raj  jiii  hello"
# newStr = str.replace("  ", " ")
# print(newStr)


# # ------------Q5---------------

# letter ="Dear Sir,\n \tthis python course is nice. \nThanks!"
# print(letter)








"""
Practice Set : tuples, list...

1. Write a program to store 2 fruits in a list entered by the user.
2. Write a program to accept marks of 3 students and display them in a sorted manner.
3. Check that a tuple type cannot be changed in python.
4. Write a program to sum a list with 4 numbers.
5. Write a program to count the number of zeros in the following tuple:
a = (7, 0, 8, 0, 0, 9)

"""



# # ------------ Q1 ---------------

# fruit = []

# a = input("enter fruit name: ")
# fruit.append(a)

# b = input("enter fruit name: ")
# fruit.append(b)

# print(fruit)



# # ------------ Q2 ---------------

# studentMarks = []

# s1 = int(input("enter you marks: "))
# studentMarks.append(s1)
# s2 = int(input("enter you marks: "))
# studentMarks.append(s2)
# s3 = int(input("enter you marks: "))
# studentMarks.append(s3)

# studentMarks.sort()
# print(studentMarks)


# # ------------ Q3 ---------------
# a = (32, "abc0", 858585, True)
# a[1] = 33   # TypeError: 'tuple' object does not support item assignment


# # ------------ Q4 ---------------
# l1 = [1,2,3,4]
# print("sum:", sum(l1))


# # ------------ Q5 ---------------
# a = (7, 0, 8, 0, 0, 9)

# ans = a.count(0)
# print(ans)











'''

Practice Set -- Dictionary and sets...

1. Write a program to create a dictionary of Hindi words with values as their English
translation. Provide user with an option to look it up!

2. Write a program to input 4 numbers from the user and display all the unique numbers
(once).

3. Can we have a set with 18 (int) and '18' (str) as a value in it?

4. What will be the length of following set s:
s = set()
s.add(20)
s.add(20.0)
s.add('20') # length of s after these operations?

5. s = {}
What is the type of 's'?

6. Create an empty dictionary. Allow 4 friends to enter their favorite language as value and
use key as their names. Assume that the names are unique.

7. If the names of 2 friends are same; what will happen to the program in problem 6?

8. If languages of two friends are same; what will happen to the program in problem 6?

9. Can you change the values inside a list which is contained in set S?
s = {8, 7, 12, "Harry", [1,2]}

'''


# # ------------ Q1 ---------------

# words = {
#     "kitab":"book",
#     "dukhi":"sad",
#     "kela":"banana",
#     "jaldi":"fast",
#     "billi":"cat"
# }

# print(words)
# inp = input("Enter the word you want meaning : ")

# print(f"Meaning of your entered word {inp} is : ", words.get(inp))




# # ------------ Q2 ---------------
# s = set()

# a = int(input("enter your 1st number : "))
# s.add(a)
# b = int(input("enter your 2nd number : "))
# s.add(b)
# c = int(input("enter your 3rd number : "))
# s.add(c)
# d = int(input("enter your 4th number : "))
# s.add(d)



# print(s)



# #  $$$$$$ interview question -- 
# s=set()
# s.add(1)
# s.add(1.0)
# s.add("1")

# print(len(s))  # length is 2 becz 1==1.0 becz only val compare not data types...



# # ------------ Q3 ---------------
# s=set()
# s.add(8)
# s.add('8')
# print(s)



# # ------------ Q4 ---------------
# s = set()
# s.add(20)
# s.add(20.0)
# s.add('20') # length of s after these operations? - 3


# # ------------ Q5 ---------------
# s={}
# print(type(s))


# # ------------ Q6 ---------------

# friends = {}  #empty dictionary

# name = input("Enter your name: ")
# lang = input(f"Hi {name} enter your fav language: ")
# friends.update( {name:lang} )

# name = input("Enter your name: ")
# lang = input(f"Hi {name} enter your fav language: ")
# friends.update( {name:lang} )

# name = input("Enter your name: ")
# lang = input(f"Hi {name} enter your fav language: ")
# friends.update( {name:lang} )

# name = input("Enter your name: ")
# lang = input(f"Hi {name} enter your fav language: ")
# friends.update( {name:lang} )

# print(friends)



# ------------ Q7 ---------------
#$$ it will takes the latest entered key value pair becz we do update......



# ------------ Q8 ---------------
# $$$ value can be duplicate but keys should be unique becz that ids identifier... so both entries will there.



# ------------ Q9 ---------------
# s = {8, 7, 12, "Harry", [1,2]}
# $$$ since we cant do changes in values inside set and even we cannot even have a list as an element in a set becz sets in python require all their elements to be immutable and hashable.








'''
Practice Set -------- conditional statements.

1. Write a program to find the greatest of four numbers entered by the user.

2. Write a program to find out whether a student has passed or failed if it requires a total of
40% and at least 33% in each subject to pass. Assume 3 subjects and take marks as an
input from the user.

3. A spam comment is defined as a comment containing following keywords: “Make a lot of
money”, “buy now”, “subscribe this”, “click this”. Write a program to detect these spams.

4. Write a program to find whether a given username contains less than 10 characters or not.

5. Write a program which finds out whether a given name is present in a list or not.

6. Write a program to calculate the grade of a student from his marks from the following
scheme:
90 - 100 => Ex
80 - 90 => A
70 - 80 => B
60 - 70 => C
50 - 60 => D
<50 => F

7. Write a program to find out whether a given post is talking about “adi” or not.

'''




# # --------------- Q1 ------------------

# num1 = int(input("Enter your 1st num : "))
# num2 = int(input("Enter your 2nd num : "))
# num3 = int(input("Enter your 3rd num : "))
# num4 = int(input("Enter your 4th num : "))

# greatest = num1
# if(num2>greatest):
#     greatest = num2

# if(num3>greatest):
#     greatest=num3

# if(num4>greatest):
#     greatest=num4

# print("greatest no. : ", greatest)




# # --------------- Q2 ------------------
# # passing criteria - individual 33% in each subject + overall 40%

# SubPassing = 33
# totalPassing = (40/100)*300

# sub1 = int(input("Enter your 1st subject number : "))
# sub2 = int(input("Enter your 2nd subject number : "))
# sub3 = int(input("Enter your 3rd subject number : "))
# totalMarks = sub1+sub2+sub3
# totalpercent = (totalMarks/300) * 100

# if((sub1>=SubPassing and sub2>=SubPassing and sub3>=SubPassing) and (totalMarks>=totalPassing)):
#     print(f"You are passed and your total obtained percentage is {totalpercent}")
# else:
#     print("You failed. Try again next year!")





# # --------------- Q3 ------------------
# # in -- to check is there is sub ele is there or not... 

# p1="Make a lot of money"
# p2="buy now"
# p3="subscribe this"
# p4="click this"

# comment = input("enter your comment : ")

# if((p1 in comment) or (p2 in comment) or (p3 in comment) or (p4 in comment)):
#     print("This is a spam comment")

# else:
#     print("No spam comment")



# # --------------- Q4 ------------------
# username = input("Enter you username : ")

# if(len(username)<10):
#     print("Yes! it contain less than 10 characters.")
# else:
#     print("No! it has more than 10 characters")



# # --------------- Q5 ------------------
# list1 = ["khsu", "aditya", "hitman", "klr", "adi", "haa"]
# find = input("Enter the name you want to find : ")

# if(find in list1):
#     print(f"Yes! {find} is there in the list")

# else:
#     print(f"No! {find} is not in the list.")


# # --------------- Q6 ------------------
# marks = int(input("Enter your marks : "))

# if(marks>=90 and marks<=100):
#     print("Congratulations! Your grade is : ", "Ex")
# elif(marks>=80 and marks<90):
#     print("Congratulations! Your grade is : ", "A")
# elif(marks>=70 and marks<80):
#     print("Congratulations! Your grade is : ", "B")
# elif(marks>=60 and marks<70):
#     print("Congratulations! Your grade is : ", "C")
# elif(marks>=50 and marks<60):
#     print("Congratulations! Your grade is : ", "D")
# else:
#     print("Sorry! You are failed, try next year.", "F")



# # --------------- Q7 ------------------
# post = input("Enter your post : ")

# if("adi" in post.lower()):
#     print(f"Yes! this post have talked about {"adi"}")
# else:
#     print(f"No! this post have not talked about {"adi"}")














'''

Practice Set ------- loops

1. Write a program to print multiplication table of a given number using for loop.
2. Write a program to greet all the person names stored in a list ‘l’ and which starts with S.
l = ["Harry", "Soham", "Sachin", "Rahul"]
3. Attempt problem 1 using while loop.
4. Write a program to find whether a given number is prime or not.
5. Write a program to find the sum of first n natural numbers using while loop.
6. Write a program to calculate the factorial of a given number using for loop.

7. Write a program to print the following star pattern.
*
***
***** for n = 3

8. Write a program to print the following star pattern:
*
**
*** for n = 3

9. Write a program to print the following star pattern.
* * *
*   * for n = 3
* * *

10. Write a program to print multiplication table of n using for loops in reversed order.

'''



# # ---------------------------- Q1 --------------------------

# number = int(input("Enter the numberof which you want table : "))

# for i in range(1,11):
#     val = i*number
#     print(f"{number} * {i} = {val}")




# # ---------------------------- Q2 --------------------------
# l = ["Harry", "Soham", "Sachin", "Rahul"]
# for item in l:
#     if(item[0].lower()=="s"):
#         print(f"Hello! good morning {item}")






# # ---------------------------- Q3 --------------------------
# num=int(input("Enter the number, you want table : "))
# i=1
# while(i<11):
#     val = i*num
#     print(f"{num} * {i} = {val}")
#     i+=1





# # ---------------------------- Q4 --------------------------
# num = int(input("Enter your no. to check prime or not : "))


# isprime = True

# if num<=1:
#     isprime = False
# else:
#     for i in range(2, num):
#         if num%i ==0:
#             isprime = False
#             break
# if isprime:
#     print(f"{num} is Prime no.")
# else:
#     print(f"{num} is not Prime no.")





# # ---------------------------- Q5 --------------------------
# num = int(input("Enter a natural no. : "))
# i=1
# sum = 0
# while(i<=num):
#     sum+=i
#     i+=1

# print(f"Sum upto {num} natural numbers is : {sum}")






# # ---------------------------- Q6 --------------------------

# num = int(input("Enter the no. to find its factorial : "))

# ans = 1

# for i in range(1,num+1):
#     ans = ans * i
#     i+=1

# print(f"Factorial of {num} ({num}!) is : ", ans)





# # ---------------------------- Q7 --------------------------
# n=4
# for i in range(1,n+1):
#     print(" " * (n-i), end="")
#     print("*" * (2*i -1), end="")

#     print("\n")





# # ---------------------------- Q8 --------------------------
# n=3

# for i in range(1,n+1):
#     print("*" * (i), end="")
#     print("\n")





# # ---------------------------- Q9 --------------------------
# n = 3
# for i in range(1,n+1):

#     if(i==1 or i==n):
#         print("*" * n, end="")
#     else:
#         print("*", end="")
#         print(" "* (n-2), end="")
#         print("*", end="")
#     print("")



# # ---------------------------- Q10 --------------------------
# num = int(input("Enter number for reverse table : "))

# for i in range(1, 11):
#     val = (11-i) * num
#     print(f"{num} * {11-i} = {val}")













'''
Practice Set  --- functions and recursion

1. Write a program using functions to find greatest of three numbers.

2. Write a python program using function to convert Celsius to Fahrenheit.

3. How do you prevent a python print() function to print a new line at the end.

4. Write a recursive function to calculate the sum of first n natural numbers.

5. Write a python function to print first n lines of the following pattern.
***
**
*
- for n = 3

6. Write a python function which converts inches to cms.

7. Write a python function to remove a given word from a list and strip it at the same time.

8. Write a python function to print multiplication table of a given number.

'''


# # --------------------------- Q1 -------------------------------
# def greatest(a,b,c):
#     if(a>=b and a>=c):
#         return a
#     elif(a<=b and b>=c):
#         return b
#     else:
#         return c

# a,b,c = map(int, input("enter your all three numbers separated by space: ").split())
# ans = greatest(a,b,c)

# print(f"Greatest number among {a}, {b}, {c} is : {ans}")




# # --------------------------- Q2 -------------------------------
# def ConverTemperature(value):
#     ans = (value * (9/5)) + 32
#     return ans

# input = float(input("Enter your celsius temperature : "))
# print(f"Converted {input} Celsius(C) = {ConverTemperature(input)} Fahrenheit(F)")





# # --------------------------- Q3 -------------------------------
# print("Hellooooooooooooooooooooo")

# print("Hello oooooooooooooooooooooooo", end="")
# print("Hellooooooooooooooooooooo")




# # --------------------------- Q4 -------------------------------
# n = int(input("Enter your natural number : "))
# def Sum(n):
#     if(n==0): return 0
#     return n+Sum(n-1)

# print(f"Sum of {n} natural numbers is : {Sum(n)}")



# # --------------------------- Q5 -------------------------------
# def pattern(n):
#     if(n==0): return
#     print("*" * n)
#     pattern(n-1)

# n = int(input("Enter the value of n : "))

# pattern(n)




# # --------------------------- Q6 -------------------------------
# def ConverInches(n):
#     return 2.54*n

# n = float(input("Enter the value of inches : "))

# print(f"Converted {n} inches = {ConverInches(n)} cm")





# # --------------------------- Q7 -------------------------------
# def remove_and_strip(wordList, word_to_remove):
#     target = word_to_remove.strip()

#     result = []  #empty list to store final words...
#     for item in wordList:
#         cleaned_items = item.strip()

#         if(cleaned_items!=target):
#             result.append(cleaned_items)

#     return result


# fruits = ["  apple ", " banana ", "apple"]
# print(remove_and_strip(fruits, "apple"))




# # --------------------------- Q8 -------------------------------
# def Tableprint(n):
#     for i in range(1,11):
#         val = n*i
#         print(f"{n} * {i} = {val}")


# n = int(input("Enter the no. for its table : "))
# Tableprint(n)
