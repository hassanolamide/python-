# # VARIABLE

# # QUESTION 1
# Student_Name = "Amina"
# Age= 22
# Department= "computer science"

# print ("Student Name: " ,Student_Name)
# print("Age: ",Age)
# print("Department: ",Department)

# # QUESTION 2

# price_note = 1200
# price_pen = 300
# number_note = 3
# number_pen =2

# Total_Note = price_note * number_note 
# Total_pen = price_pen * number_pen


# Total = Total_Note + Total_pen

# print(f"₦{format(Total, ',')}")


# # QUESTION 3

# initial_balance = 25000
# food_expences = 6500
# receive = 10000

# sub = initial_balance - food_expences
# final_balance = sub + receive

# print(f"₦{format(final_balance, ",")}")


# DATATYPE

# # QUESTION 1
# Username= "abdul_dev"
# Age= 23
# Account_balance= 15000.50
# Istheaccountverified = True

# print (type(Username))
# print(type(Age))
# print(type(Account_balance))
# print(type(Istheaccountverified))

# # QUESTION 2

# quality = "5"
# price = "2500"

# new_quality = int(quality)
# new_price = int(price)
# multiplication = new_quality * new_price

# print(multiplication)
# print(type(multiplication))

# # QUESTION 3
# # and requires both conditions to be true.

# amount = "7500"
# account_balance = 12000.0
# account_active = True

# new_amount = int(amount)

# has_enough_money = account_balance >= new_amount 

# can_pay = account_active and has_enough_money


# print(can_pay)


# NUMBERS

# QUESTION 1

# workers_earn = 5000
# days =6

# total_salary = workers_earn * days

# print (total_salary)

# #   QUESTION 2
# original_price = 25000
# discount = 10

# discount_amount = original_price * 0.1

# total_price = original_price - discount_amount

# print(discount_amount)
# print(total_price)

# # QUESTION 3
# current_price = 15500.50
# deposit = 5000.75
# withdraw = 2000.25

# after_deposit= current_price + deposit
# after_withdraw = after_deposit - withdraw 

# print(after_deposit, type(after_deposit))
# print(after_withdraw, type(after_withdraw))

# TYPE CASTING

# QUESTION 1
# age = "21"

# new_age = int(age)

# print(new_age, type(new_age))

# # QUESTION 2

# price ="3500.50"
# quality = "3"

# new_price = float(price)
# new_quality = int(quality)

# total = new_price * new_quality

# print(total, type(total))

# # QUESTION 3

# customer_name = "Abdul"
# total_payment = 12500

# new_payment = str(total_payment)

# print(f"{customer_name} paid ₦{new_payment}")

# print(type(new_payment))

# STRING
# QUESTION 1
# student_name = "amina bello"

# print(student_name.upper())
# print(student_name.lower())
# print(len(student_name))

# # QUESTION 2
# email = "  ABDUL@GMAIL.COM  "
# print(email.strip().lower())
 
# # QUESTION 3
# first_name = "Abdul"
# skill  = "python Developer"

# message = first_name + " " +  skill

# print(f"Hello {first_name}, welcome to your {skill} journey!")

# print("python" in message)



# BOOLEAN
# QUESTION 1

# age = 22

# can_register = age >=18

# print(can_register)

# QUESTION 2

# account_balance = 15000
# payment_amount = 12000
# account_active = True

# balance_check = account_balance >= payment_amount

# can_pay = balance_check and account_active


# print(can_pay)

# # QUESTION 3

# correct_username = True
# correct_password = False

# login_succeful = correct_password and correct_username

# login_succefuls = correct_password or  correct_username
# print(login_succeful)
# print(login_succefuls)

# OPERATOR
# QUESTION1

# biscuits = 17
# people = 5

# people_receive = biscuits // people
# remaining_biscuits = biscuits % people

# print(people_receive)
# print(remaining_biscuits)

# # QUESTION2

# phone_a = 250000
# phone_b = 220000

# Phone_check = phone_a == phone_b
# phone_great = phone_a > phone_b
# phone_cheap = phone_b < phone_a

# print(phone_cheap,phone_great,Phone_check )

# # QUESTION 3

# purchase_amount = 25000
# is_member = True

# purchase_check = purchase_amount >= 20000
# get_discount = purchase_check and is_member

# print(get_discount)


# LIST 
# QUESTION 1
# students = ["Abdul", "Amina", "David", "Sarah"]

# print(students)
# print(students[0])

# students.append("Micheal")
# students.remove("David")

# print(students)

# # QUESTION 2

# product = ("Laptop", 450000, "HP")

# print(product[0])
# print(product[1])
# print(product[2])
# print(len(product))

# # QUESTION 3
# emails = [
#     "abdul@gmail.com",
#     "amina@gmail.com",
#     "abdul@gmail.com",
#     "david@gmail.com",
#     "amina@gmail.com"
# ]

# new_set = set(emails)
# print(new_set)
# print(len(new_set))

# CONDITIONAL STATEMENT
# QUESTION 1

# age = 16
# if age >= 18:
#     print("Registred allowed")
# else:
#     print("Registration denied")

# # QUESTION 2
# score = 65

# if score >= 70 :
#     print("A")
# elif score >= 60:
#     print("B")
# elif score >= 50:
#     print("C")
# elif score >= 45:
#     print("D")
# else :
#     print("F")

# # QUESTION 3

# account_balance = 50000
# withdrawal_amount = 20000
# account_active = True

# if account_active != True:
#     print("Account is inactive")
# elif withdrawal_amount > account_balance:
#     print("Insufficient balance")
# else:
#     print("Withdrawl successful")


# LOOP
# FOR LOOP

# QUESTION 1
# daily_sales = [5000, 7500, 3000, 9000, 6500]

# total_sales = 0 
# for number in daily_sales:
#     print(number)
#     total_sales = total_sales + number

# print("Total sales : ",total_sales)

# # QUESTION 2

# scores = [45, 78, 32, 90, 55]

# for number in scores:
#     if number >= 50:
#         print(number," - pass")
#     else:
#         print(number," - fail")

# # QUESTION 3

# prices = [2500, 4000, 1500, 3000]

# total_cost = 0
# item_count = 0
# for number in prices:
#     total_cost = total_cost + number
#     if number >= 3000:
#         item_count = item_count + 1


# print("Total cost:", total_cost)
# print("Items costing at least 3000:", item_count)

# WHILE LOOP
# QUESTION 1
# current_balance = 5000

# while current_balance < 25000:
#     current_balance = current_balance + 5000
#     print(current_balance)

# print("Savings goal reached!")
# # QUESTION 2


# correct_password = "python123"
# attempts = 0
# passwords = ["wrong123", "hello456", "python123"]


# while attempts <= 3:
#     print("Attempt", attempts + 1)

#     entered_password = passwords[attempts]

#     if entered_password == correct_password:
#         print("Login successful")
#         break 

#     attempts = attempts + 1
#     if attempts == 3 and passwords[attempts -1]!= correct_password:
#         print("Account temporary locked.")


# correct_password = "python123"
# attempts = 0

# while attempts < 3:
#     entered_password = input("Enter your password: ")
#     attempts = attempts + 1

#     if entered_password == correct_password:
#         print("Login successful")
#         break
#     else:
#         print("incorrect password")

# if attempts == 3 and entered_password != correct_password:
#     print("Acoount banned")

# QUESTION 3
# expenses = [2000, 1500, 3000, 2500, 2000]

# total = 0
# index = 0

# while index < len(expenses) and total < 10000:
#     total = total + expenses[index]
#     print(total)
#     index = index + 1

# if total >= 10000:
#     print("BUDGET REACHED!")
 

# function
# QUESTION 
# def greet_user(name):
#     print("Welcome,",name)

# greet_user("Abdul!")
# greet_user("Sarah!")

# # QUESTION 2

# def calculate_salary(daily_salary,days_worked):
   
#     return daily_salary*days_worked

# total = calculate_salary(5000,6)

# print("Total salary:",total)

# prices = [2500, 4000, 1500, 3000]
# def calculate_total(prices):
#     total_cost = 0
   
#     for number in prices:
#         total_cost = total_cost + number
#     return total_cost
# result = calculate_total(prices)

# print("Total cost:",result)

# def calculated_discount(price,discount_percentage):
#     discount= price*discount_percentage 
#     return discount
# result = calculated_discount(25000,0.1)

# print("Discount amount: ",result)


# def  calculate_final_price(price,discount_percentage):
#     discount = price * discount_percentage / 100
#     discount_sub = price - discount
#     return discount_sub
# result = calculate_final_price(25000,10)

# print("Final price:",result)

# DICTIONARIES
# QUESTION 1

# student ={
#     "Name": "Abdul",
#     "Age": 22,
# "Course": "Computer Science"
# }
# print(student["Name"])
# print(student["Age"])
# print(student["Course"])

# # QUESTION 2
# product = {
#     "name": "laptop",
#     "price": 250000,
#     "quantity": 5
# }

# print(product["name"])
# print(product["price"])

# product["quantity"]= 8
# product["brand"] = "HP"

# print(product)


# # QUESTION 3
# student = {
#     "name": "Abdul",
#     "score": 75
# }

# print(student["name"])

# student["score"]= 90
# student["grade"]= "A"

# del student["score"]

# print(student)

# # QUESTION 4
# students = {
#     "Abdul": 85,
#     "Sarah": 45,
#     "John": 70,
#     "Mary": 35
# }

# passed = 0

# for name, score in students.items():
#     if score >= 50 :
#         print(name, "Pass")
#         passed = passed + 1
#     else:
#         print(name, "fail")


# # new exe

# products = {
#     "Rice": 5000,
#     "Beans": 3500,
#     "Milk": 2500,
#     "Bread": 2000,
#     "Oil": 4500
# }

# stock = 0

# for name, price in products.items():
#     print (name , "-", price)
#     stock = stock + 1
# # ques2
# products = {
#     "Rice": 5000,
#     "Beans": 3500,
#     "Milk": 2500,
#     "Bread": 2000,
#     "Oil": 4500
# }

# stock = 0

# for name, price in products.items():
#     if price >= 3000:
#         stock = stock + 1

# print("Products costing ₦3000 or more:", stock)

# # ques 3

# products = {
#     "Rice": 5000,
#     "Beans": 3500,
#     "Milk": 2500,
#     "Bread": 2000,
#     "Oil": 4500
# }

# stock = 0

# for name, price in products.items():
#     stock = stock + price

# print("Total inventory value:", stock)



# students = {
#     "Abdul" : 5000,
# "Sarah ": 7000,
# "John ":4000,
# "Mary ":8000,
# "David": 6000
# }


#                         SECTION 2 LESSON (TECHNICALLITY)
# i will be using the number variable, 2 condition : for the number to not be greater than 10, 3) i will use while loop < 10

# number = 1
# while number <= 10:
#     print("student",number)
   
#     number += 1
# print("Attendance comppleted!")


# # 1) The customer variable  2) total will be named as the variable 3) using the for oop to get each num and add the total together

# customer = 1
# total = 0
# while customer <= 5:
#     amount = int(input("Enter amount: "))
#     total = total + amount
#     customer +=  1

# print("Total sales",total)


# while password is == correct password, 2) display "wrong password" 3) break when the password is correct 
# correct_password = "python123"
# password = ""

# while password != correct_password:
#     password = input("Enter password: ")
#     if password == correct_password:
#         break
#     else:
#         print("wrong password! try again.")
# print("Acess grant")


# FOR LOOP

# prices = [2000, 3500, 1500, 5000, 2500]

# count = 0

# for price in prices :
#     if price >= 3000:
#         count = count + 1

# print(count)
# s
# prices = [2000, 3500, 1500, 5000, 2500]

# count = 0

# for price in prices:
#     if price >= 3000:
#         print(price)
#     count += 1

# print("Count:", count) 


# FOR LOOOPPPPP
# count = 0
# total = 0

# numbers = [10, 15, 20, 25, 30, 35, 40]

# for number in numbers:
#     if number % 2 == 0:
#        total = total + number
#        count += 1 

# print(count, total)

# count = 0
# total = 0
# scores = [45, 80, 67, 90, 32, 75, 55, 88]
# for score in scores:
#     if score >= 60:
#         count += 1
#         total = total + score
# average = total/count

# print(average)

# RANGE 
'''
range(start, stop, step) THE 3 STEP THAT RANGE FOLLOWS.
And for normal range it start from 1 to the end.
'''

# count = 0 

# for number in range(1, 20,2):
#     if number % 2 != 0:
#         count += 1
#         print(number)
# print(count)


# numbers = [12, 7, 25, 40, 18, 33, 50, 9]
# count = 0
# total =0
# for number in range(len(numbers)):
#     if numbers[number] > 20:
#         count += 1
#         total = total + numbers[number]
# print("Total:",total)
# print("Count:", count)


# PHYTHON ARRAY

'''Python array can store diffrent data typess.'''
# import array

# scores = array.array('i',[45, 60, 75, 80, 90])

# scores.append(95)
# scores.insert(0,50)
# scores.remove(75)

# total = 0
# for score in scores:
#     total = total + score
# print(total)



# import array

# scores = array.array('i', [45, 60, 75, 80, 90, 55, 95])

# highest = scores[0]
# lowest = scores[0]
# for score in scores:
#     if score > highest:
#         highest = score

#     if score < lowest:
#         lowest = score
# print(highest)
# print(lowest)


# import array

# scores = array.array('i', [45, 60, 75, 80, 90, 55, 95])
# total = 0
# count = 0
# for score in scores:
#     total = total + score
# average = total / len(scores)
# for score in scores:
#     if score > average:
#         count +=1

        
# print(average, "count: :", count)

# '''ITERATION
# iter to convert
# next to review the iteration.
# '''
# numbers = [10, 20, 30]
# my_iterator = iter(numbers)
# print(next(my_iterator))


# numbers = [100, 200, 300, 400]

# my_iterator = iter(numbers)

# print(next(my_iterator))
# print(next(my_iterator))

# for number in my_iterator:
#     print(number)


'''MODULES
math: mathematical operations.
random: generating random values.
datetime: working with dates and times.
array: working with typed arrays.
'''
# import random

# number = random.randint(1,100)

# print(number)20


# QUESTION 2
# import random 

# number = random.randint(1,20)

# guess = int(input("Enter your number: "))
# while guess != number:
   
#     if guess > number:
#         print("Too high")
#     elif guess < number:
#         print("Too low")
#     guess = int(input("Try again: "))

# print("Congratulations! You got it.")


# DATETIME
'''
Code	Meaning	Example
%d	Day	11
%m	Month	11
%Y	Full year	2026
%H	Hour (24-hour)	14
%M	Minute	30
%S	Second	45
%A	Full weekday	Wednesday
%B	Full month	November
'''
# import datetime

# today = datetime.datetime.now()

# print("year:",today.year)
# print("Month:",today.month)
# print("Day:",today.day)


# import datetime

# today = datetime.datetime.now()

# arranged_date = today.strftime("%A, %d %B %Y")

# print(arranged_date)

# import datetime

# today = datetime.date.today()
# formated_date = today.strftime("%m/%d/%Y")

# print(formated_date)
# print(today.year)

# import datetime

# today = datetime.date.today()
# examdate = datetime.date(2026,12,25)

# diffrence = examdate - today

# print(diffrence)

import datetime

today = datetime.date.today()
student_input = input("Enter an exam Date in YYYY-MM-DD:")

convert_input = datetime.datetime.strptime(student_input, "%Y-%m-%d").date()

result = convert_input - today


print(result.days)


import datetime

today = datetime.date .today()
student_input = input("Enter an exam Date in YYYY-MM-DD:")
convert = datetime.datetime.strptime(student_input,  "%Y-%m-%d").date()
result = convert - today
if student_input < today:
    print(result)
elif student_input == today:
    print("Your examination is today")
elif student_input > today:
    print("exam has passed")
