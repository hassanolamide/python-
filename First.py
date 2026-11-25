#if 5 > 3 :
  #  print("FIve is greater than three")

#print("Hello world"); print(5)

# print("Hameedah", end = " ")
# print("is a pretty gal")

# print(3 + 2)

# x = 5
# x = 'ola'
# print(type(x))

# x,y,z ="ola" , "wed", "her"
# print(x , y , z)

# GLOBAL VARIABLE
# x = "ola"

# def myfunc():
#   x = 'function'
#   print("phyton is " + x)

# myfunc()

# print("phyton is " + x)

# def myfunc():
#     global x
#     x = "Ade"
# myfunc()

# print ("My name is " + x)


# x = "awesome"

# def myfunc():
#   global x
#   x = "fantastic"

# myfunc()

# print("Python is " + x)

# y = 1j
# print(type(y))

# #CONVERT FROM INT TO FLOAT
# x =1

# a= complex(x)
# print(a)

# import random
# print(random.randrange(1, 10))

# w = float("4.2") 
# print(w)

# a= "my name is 'james'"
# print(a)

# b = """my namess"""
# print(b)

# a = """Lorem ipsum dolor sit amet,
# consectetur adipiscing elit,
# sed do eiusmod tempor incididunt
# ut labore et dolore magna aliqua."""
# print(a)


# b = "hello world"
# print(b.upper())

# a = "Hello, World!"
# print(a.replace("H", "J"))


# convert text to number. 
# bananas = "2"
# milk = "1.5"

# banana_count = int(bananas)
# milk_count = float(milk)
# print(banana_count+ milk_count)

# # convert number to text# milk = "1.5"
# a = 2
# print ("i need "+ str(a) + " babessss")


# user_input = "2"

# if user_input.isdigit():
#     banana_count= int(user_input)
#     print("succeful")

# else:
#     print("unsucceful") 
#     banana_count = 0


# a = "omotan"
# b =  "pretty girl"

# print(a +" is a " + b)


# selected_tea ="Blue_tea"
# target_temp = 100

# if selected_tea == "Blue_tea":
#     target_temp = 80


#     print(target_temp)


# selected_name = "ade"
# age = 15

# if selected_name == "ola":
#   age = 12

# elif selected_name =="ade":
#     age = 30


# print(age)


# selected_name = input("Enter your name: ")
# age = 40

# if selected_name == "ola":
#   age = 50
# elif selected_name == "owolabi":
#   age = 30
# else:
#   age == 0

# print(age)



#selected_player = "messi"
# rating = 98

# if selected_player == "ronaldo":
#   rating = 99 
# elif selected_player == "great":
#   rating = 29 

# else :
#   rating = 100

# print(rating)


# for count in range(3):
#     print("Grind " + str(count))

# for twist_number in range(5):
#     print("Grinding twist number " + str(twist_number + 1))

# for mubarack in range(13):
#    print("Mubarack has 5 babes " + str(mubarack + 1 ))

# weight = -1.0 #base case
# while weight < 1.5:
#     weight = weight + 0.5
#     print("Current weight: " + str(weight))

# age = 30
# while age < 50:
#     age = age + 2
#     print("current age " + str(age))

# customer_name =" aisha "

# clean_name = customer_name.strip().title()

# print("["+ clean_name +"]")

# slice
# order = "aDEOBA"
# print(order.strip().title())

# order = "omotan"
# abbrevation = order[0:3]
# print(abbrevation)

# # string formation
# name = "Olamide"
# drink ="pepsi"
# price = 4.56

# receipt = f"order from {name} with cold {drink} and your amount is {price:.2f}"

# print(receipt)

sentence = "latte or espresso or garri"
words = sentence.split(" or ")
# print(words)

# rejoined = "-".join(words)
# print(rejoined)

# def name_fix(name):
#    print("Name of person "+ name)

# name_fix("ola")

# x = "Hello"
# y = 15

# print(bool(x))
# print(bool(y))

# x = 12
# y = 5

# print(x // y)


# x = 5
# print(1 < x < 10)
# fruits = ["apple", "banana", "cherry"]

# print("pineapple" not in fruits)


# LIST
# the_List = ["boy", "girl", "man"]
# the_List[1] ="babe"
# print(the_List)

# thislist = ["apple", "banana", "cherry"]
# thislist[1:3] = ["watermelon"]
# print(thislist)

# theList = ["orange","pawpaww","banana"]
# theList.append( "grounnut")

# print(theList)

# x =["orange","pawpaww","banana"]
# if "orange" in x:
#   print (" i have yes")

# # remove (.remove(),.pop(1) del thislist, .clear)
# thislist = ["apple", "banana", "cherry"]
# thislist.clear()
# print(thislist)


# # LOOP

# # thislist = ["apple", "banana", "cherry"]
# # for x in thislist:
# #   print(x)

# # thislist = ["apple", "banana", "cherry"]
# # for i in range(len(thislist)):
# #   print(thislist[i])
# thislist = ["apple","banana", "orange"]
# i = 0
# while i < len(thislist):
#   print(thislist[i])
#   i = i + 1

x = range(3, 10, 2)
print(list(x))


# Array
# mytuple = ("apple", "banana", "cherry")
# myit = iter(mytuple)

# print(next(myit)