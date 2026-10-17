# import pyjokes 

# joke = pyjokes.get_joke()


# # this prints random joke.

# """
# this is multi line comments 
# saar.
# """


# print(joke)


# # print("hello world")










# ---------------------- variables and datatypes-------------------------

# a = 1
# b = 2

# print(a+b)



# # ----- intput----------and type conversion and ll

# a = int(input("enter number-1: "))

# b = int(input("enter number-2: "))

# # print(type(a))

# print("sum is - ", a+b)



# # -----------------------  slice  ----------------------

# a = "aditya"
# b = 'raj'
# c = '''  Hello '''
# d = """" gm bro.  """

# print("type is------------ ", type(a), type(b), type(c), type(d) )




# # slice = a[-3: -1]
# # slice = a[:4]
# # slice = a[1:5]    # here last exclude val is 5
# slice = a[1:]    # here it takes last exclude val is 6.

# print(slice)


# # slicing with skip values....

# slice = a[0:6:4]   # first will definitely come then from next element count the skips...

# print(slice)




# ------------some string functions........


# str = "abcdefghijklmnopqrstuvwxyz"

# print(len(str))
# print(str.count("a"))

# print(str.capitalize())

# # index = str.find("a")

# index = str.replace("a", "111")

# # -------------------escape sequence char in python...
'''
To insert characters that are illegal in a string, use an escape character.

An escape character is a backslash '\' followed by the character you want to insert.
'''

# print(index)

# print("The process by which green \"plant\" make \\ their food is called photosynthesis")






# # ------------------------------------------  lists and tuples   ------------------------------------
# # NOTE - list is mutable but string immutable...

# l1 = [7,9, "adi", 12.12, "yoo"]

# l1[2] = "aditya"   #unlilke string list are mutable means we can change here.

# # $$$ unlike string if we use methods of list then that changes will happened in the list not return a new like string methods do.......

# l1.append("buttan")

# l1.reverse()

# l1.insert(3, 353535535)
# a = l1.pop(3)

# l1.remove("yoo")

# print(a)

# print("\n")
# print(l1)
# print(l1[0])
# print(l1[1])
# print(l1[2])


# # tuple - immutable data types but it is same like list - collection of data types.
# print("\n")

# a = (1,)
# print(type(a))

# b = (1,5656, "jjj0", False, "Aditya")

# print(a.count(1))

# tuple1 = (1,2,3)
# tuple2 = (4,5,6)
# concate = tuple1+tuple2
# print(concate)

# # repeat tuple-
# tuple3 = ("1", "b", True)
# mytriple = tuple3*3
# print(mytriple)

# print("a" in tuple3)








# ----------------------------------------------------- Dictionary and Sets ----------------------------------------

# Dictionary: list of key value pairs...

# d={}  # empty dictionary

# a = {
#     "aditya":100,
#     "adi":12,
#     1:"klRahul"
# }

# print(a.items())
# print(a.keys())
# a.update({"aditya":99, "khu":78} )
# print(a.items())



# print(a.get("khu1"))  # return none - becz khu1 is not there
# print(a["khu1"]) # gives error


# sets: - 
# - no element repeat.

# # for empty set --
# s = set()  # becz if we use like s={} then it will becomes empty dictionary not set.


# s = {1,2,2,2,3,5,6,9,8,8,9}
# print(s)  # since it is set so it will take distinct element not repeat elements 

# s= {1,2,"adi",False}
# print(s, type(s))
# print("\n")

# print(len(s))

# s1 = {1,2,3,4,5}
# s2 = {9,8,7,6,5}

# print(s1.union(s2))
# print(s1.intersection(s2))




# fruits = {"fruits", "grapes"}   
# fruits.add("mango")

# fruits.update(["buttan", "fruits"])   #we can add multiple elements by using list.
# fruits.discard("fruits")

# print(fruits)












# # ----------------------------------------------------- Conditional Expression  ---------------------------------------------

# a = int(input("Enter your age : "))

# if(a>=18):
#     print("you can vote")

# else:
#     print("You can't vote.")







# ---------------------------------------- loops ---------------------------------------

# i=1
# while(i<10):
#     print(i)
#     i+=1


# # for i in range(0,4): #here in range -- 4 is exclude...
# #     print(i)

# # step...
# for i in range(0,100,5):   
#     print(i)

# str = "aditya"

# for char in str:
#     print(char)




# # $$ -----------for loop with else---

# list = [1,2,3,4,5,"aditya", "raj", "jii"]
# for items in list:
#     print(items)

# else:       
#     print("Done! All items is printed from the list")  # this is printed when the loop exhausts!



# for i in range(100):

    # if(i==45):
    #     break

    # if(i==50):
    #     continue

#     print(i)




# for i in range(456):
#     pass


# i=0
# while(i<67):
#     print("hello")
#     i+=1












# -------------------------------------------- functions and recursions ----------------------------------------------




