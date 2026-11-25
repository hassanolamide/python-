# total = 0.0
# history = []

# while True:
#     user_input = input("Enter operator and number or undo or quit: ")

#     if user_input == "quit":
#         break

#     if user_input == "undo":
#         if history:
#             total = history.pop()
#             print("Result:", total)
#         else:
#             print("Nothing to undo.")
#         continue

#     parts = user_input.split()

#     if len(parts) != 2:
#         print("Invalid input. Use: + 5")
#         continue

#     operator = parts[0]

#     try:
#         number = float(parts[1])
#     except ValueError:
#         print("Invalid number.")
#         continue

#     if operator == "/" and number == 0:
#         print("Cannot divide by zero.")
#         continue

#     history.append(total)

#     if operator == "+":
#         total = total + number
#     elif operator == "-":
#         total = total - number
#     elif operator == "*":
#         total = total * number
#     elif operator == "/":
#         total = total / number
#     else:
#         print("Invalid operator.")
#         history.pop()
#         continue

#     print("Result:", total)


#     # Palindrome:
#     sentence = input("Enter a sentence")
#     left = 0
#     right = len(sentence)-1

#     is_palindrome = True
#     while left < right:
#         if not sentence[left].isalnum():
#             left += 1
#             continue
#         if not sentence[right].isalnum():
#             right -= 1
#             continue
#         if sentence[left].lower() != sentence[right].lower():
#             break
#         left += 1
#         right -= 1
#         if is_palindrome:
#             print("it is palindrome")
#         else:
            # print("it is not palindrome")

# check grade
students =[
    {"Name":"sam","scores":[80,90]},
    {"Name":"Ade", "scores":[55,60]},
    {"Name":"Daniel", "scores":[75,85]}
]

highest_average = -1
lowest_average = 101

highest_student =""
lowest_student = ""

for student in students:
    name = student["Name"]
    scores = student["scores"]
    total = 0
for score in scores:
    total += score
    average = total/ len(scores)


if average >= 70:
     grade = "A"
elif average >= 60:
     grade ="B"
elif average >= 50:
     grade = "C"
elif average >= 45:
     grade = "D"
elif average >= 40:
     grade = "E"
else:
     grade = "F"




print(name,"Average: "f"{average:.2f}","Grade: ",grade)

if average> highest_average:
    highest_average = average
    highest_student = name


if average < lowest_average:
    lowest_average = average
    lowest_student = name

print()
print("Highest performing student:", highest_student,"_", f"{highest_average:.2f}")
print("Lowest performing student:", lowest_student,"_", f"{lowest_average:.2f}")

