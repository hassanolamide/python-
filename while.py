# while loop executue a set of statement for as long as it is true.

# i = 1
# while i < 6:
#     print(i)
#     i += 1
# increment of i is stopping it from printing forever.


# using the break function.
# i = 1
# while i < 6:
#     print(i)
#     if i == 3:
#         break
#     i += 1

# continous :we can stop the current iteration, and continue with the next.

# i = 0
# while i < 6:
#     i += 1
#     if i == 2:
#         continue
#     print(i)

# else : With the else statement we can run a block of code once when the condition no longer is true.
i = 1
while i < 6:
    print(i)
    i += 1
else:
    print("i is no longer less than 6")



# FOR LOOP

# When we are talking about for , it iterate with lists and while does not.

fruits = ["orange", "banana","apple"]
for x in fruits:
    print(x)

# loop through the letters in banana
fruits = ["orange", "banana","apple"]
for x in "banana":
    print(x)

# break
fruits = ["orange", "banana","apple"]
for x in fruits:
    if x =="banana":
        break
    print(x)

# Range fxn.
fruits = ["orange", "banana","apple", "pawpaw","grape"]
for x in range(2,4):
    print(x)


# The "inner loop" will be executed one time for each iteration of the "outer loop":

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)

