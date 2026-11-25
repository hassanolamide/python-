# if is a statment written by if.
# equal to a==b
# not equal to a!= b
# less than a<=b
# greater than a>=b
# The elif condition state that if the first statement is not ture try the scond condition.
# The else statement is executed when the if condition (and any elif conditions) evaluate to False
# and - Returns True if both statements are true
# or -  Returns True if one of the statements is true
# not - Reverses the result, returns False if the result is true
# nested if : when you have an if statement inside another if statement.
# The pass statement is a null operation - nothing happens when it executes. It serves as a placeholder


a = 45
b = 84

if a < b :
    print("yes")

age = 20
if age >= 18:
  print("You are an adult")
  print("You can vote")
  print("You have full legal rights")


x = 15
y = 20

if x > y :
   print ("maximum value", x)
else :
   print("maximum value", y)


x = 15
y = 20
max_value = x if x > y else y
print("Maximum value:", max_value)

username = ""
if username :
   print("welcome", username)
else:
   print("guest")

username = ""
display_name = username if username else "Guest"
print("Welcome,", display_name)\


a = 33
b = 200

if not a < b :
   print ("falt")
else:
   print("true")

username = "Tobias"
password = "secret123"
is_verified = True

if username and password and  is_verified:
  print("Login successful")
else:
  print("Login failed")

x = 11

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")


score = 4
extra_credit = 5

if score >= 90:
   if extra_credit > 0:
      print("A+")
   else:
      print("A")
elif score >= 80:
   print("B")
else:
   print("C")

