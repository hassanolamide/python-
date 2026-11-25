# LIST ANALYSIS 

numbers = [12,5,27,8,14]
smallest = numbers[0]
largest = numbers[0]
total = 0


for number in numbers:
    if number < smallest:
        smallest = number
    if number > largest:
        largest = number

    total += number

average  = total / len(numbers)


print("smallest: ", smallest)
print("largest: ", largest)
print("average: ", average)
print("Total: ", total)


# LINEAR SEARCH
values =[14,7,22,9,7,31]

target = 77
found = False

for i in range(len(values)):
    if values[i] == target:
        print("Found at index", i)
        found = True
        break

if not found:
    print("Target not found")


# MATRIX ROW SUMS

matrix = [[2,4,6],[1,3,5],[10,20,30]]

row_number = 1

for row in matrix:
    total =0 
    for number in row:
        total += number
    print("Row",row_number, "total: ", total)
    row_number += 1