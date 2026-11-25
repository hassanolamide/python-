# Calculator
# sum1 = int(input("Enter first number: "))
# op = input("Enter your operation: ")
# sum2 = int(input("Enter second number: "))

# if op =="+":
#     print(sum1+ sum2)
# elif op == "-":
#     print(sum1 - sum2)
# elif op == "*":
#     print(sum1 * sum2)
# elif op == "/":
#     print(sum1 - sum2)
# else :
#     print("Invalid operation" )


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


#LIST ANALYSIS
numbers =[9,3,18,6,12]
smallest = numbers[0]
largest = numbers[0]
total = 0

for number in numbers:
    if number < smallest:
        smallest = number
    if number > largest:
        largest = number
    total += number
average = total / len(numbers)


print("smallest: ", smallest)
print("largest: ", largest)
print("average: ", average)
print("Total: ", total)


