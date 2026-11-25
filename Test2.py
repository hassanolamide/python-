# Calculator
sum1 = int(input("Enter first number: "))
op = input("Enter your operation: ")
sum2 = int(input("Enter second number: "))

if op =="+":
    print(sum1+ sum2)
elif op == "-":
    print(sum1 - sum2)
elif op == "*":
    print(sum1 * sum2)
elif op == "/":
    print(sum1 - sum2)
else :
    print("Invalid operation" )


# PALINDROME

word = input("Enter a word: ")

is_palindrome = True

for i in range(len(word)//2):
    if word[i] != word[len(word)-1-i]:
        is_palindrome = False
        break
if is_palindrome:
    print(word, " is a Palindrome")
else:
    print(word, " is not a palindrome")


# Student Grade

# SECOND LARGEST

numbers = [10,5,8,20,15]

largest = float('-inf')
second_largest = float('-inf')

for num in numbers:
    if num > largest:
        second_largest = largest
        largest = num
    elif num > second_largest and num != largest:
        second_largest = num

    print("second largest", second_largest)
    