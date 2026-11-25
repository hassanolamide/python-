# sing input in py.
# name = input("Enter your name:")
# age = input("Enter your agae:")
# print("Hello " + name + " ! you are " + age )


# Building a calculator
# num1 = input("Enter a number ")
# num2 = input("Enter a  second number ")
# result = float(num1) + float(num2)

# print(result)


# Mad libs game
# color = input("Enter a color")
# plural_noun = input("Enter a plural noun")
# celebrity = input("Enter a celebrity")



# print("Roses are " + color)
# print(plural_noun + " are blue")
# print("I love " + celebrity) 


 # List using extend 
# .sort or reverse which is ascendng and desecding.

# list1 = ["ada","ade", "ola", "obatala", "giwa"]
# list2 = [ 2,34,54,65,77]

# list1.extend(list2)
# print(list1)
 
# # FUNXTION.
# def say_hi():
#     print("Hi")
# say_hi()
 

#  Dictionary

# monthcheck = {
#     "jan" : "January",
#     "feb" : "Febuary",
#     "mar" : "March",
#     "apr" : "April",
#     "may" : "may",
# }

# print(monthcheck.get("apr"))

# Loop

# i =1 

# while i <= 10:
#     print(i)
#     1 += 1
# print("Done")


# GAME GUESSSING
# itis mean to keep guessing untill 3
# secret_word ="Hameedah"
# guess = ""
# guess_count = 0
# guess_limit = 3
# out_of_guess = False

# while guess != secret_word and not(out_of_guess):
#     if guess_count < guess_limit:
#         guess = input("Enter your guess: ")
#         guess_count += 1
#     else:
#         out_of_guess = True
# if out_of_guess :
#     print ("you lose")
# else:
#     print("you won")

#FOR LOOP

for letter in "Adeola masewa":
    print(letter)


for index in range(-3,10):
    print(index)

for index in range(5):
    if index == 0:
        print ("mide mi")
    else:
        print("my love")

#2len

simple_grid =[
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [0]
]

for row in simple_grid :
    for col in row:
        print (col)


# Check if it is a vowel and after checking change it to "g"

# def translate(phrase):
#     translation = ""
#     for letter in phrase:
#         if letter.lower() in "aeiou":
#             translation = translation + "g"
#         else:
#             translation = translation + letter
#     return translation

# print(translate(input("Enter a pharse: ")))

# x = 300

# def myfunc():
#   global x
#   x = 200

# myfunc()

# print(x)

# def myfunc1():
#   x = "Jane"
#   def myfunc2():
#     nonlocal x
#     x = "hello"
#   myfunc2()
#   return x

# print(myfunc1())


#  Lammbda

# x = lambda a, b : a + b
# print(x(5,6))

'''
Using the try and except
'''

# try:
#    number = int(input("Enter your number: "))
#    print(number)
# except:
#    print("invalid input")

'''FIle Reading
"r" → READ
"w" → WRITE/REPLACE
"a" → ADD
"x" → CREATE
'''

# with open("students.txt", "r") as file:
#     print(file.read())

# with open("student.txt", "x") as file:
#    file.write("Hello")


# name = input("Enter student name: ")

# with open("student.txt", "a") as file:
#    file.write(name + "\n")

# print("Saved")

# with open("student.txt", "a") as file:
#    file.write("Lamidi - Content" + "\n")
# print("Successful") 



# TRY AND EXCEPT
'''
    Try block help test code for error.
    Except help you handle the error
    else: it help execute code when there is no error
    Finally: it execute the code regadless the result of the try and except.

    Exception: is use to catch ann exception
'''
try:
    print(x)
except:
    print("Invalid error")

txt= 95
print(f"I am {txt:.2f} years")


x = input("Enter a number: ")

print(float(x))