
numbers = [12, 5, 27, 8, 14, 27, 3]

smallest = numbers[0]
largest = numbers[0]
small_index = 0
large_index = 0
total = 0

for i in range(len(numbers)):
    number = numbers[i]

    if number < smallest:
        smallest = number
        small_index = i

    if number > largest:
        largest = number
        large_index = i

    total += number

average = total / len(numbers)


count = 0

for number in numbers:
    if number > average:
        count += 1


print("Smallest:", smallest, "(at index", small_index, ")")
print("Largest:", largest, "(at index", large_index, ")")
print("Total:", total)
print("Average:", round(average, 2))
print("Numbers above average:", count)


