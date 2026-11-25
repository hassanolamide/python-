# Tuple are use to store multiple data in a variable.(that cannot be change)
# tuple is also like list but  list is "[]" and tuple is "()", where tuple cannot be changed.
# To create tuple with one item you hav to add comma to the end for it to knoe it is s tuple.

thistuple =("ade", "ola", "seun")
print(thistuple)


oneitem = ("one",)
print(type(oneitem))

diffrent = ("ade", 69, "yes", True, False)
print(diffrent)

# Acess tuple

thistuple =("ade", "ola", "seun")
print(thistuple[2])


# UPDATE OR CHANGE.

x =("ade", "ola", "seun")
y = list (x)
y[1] = "ganny"
x = tuple(y)
print(x)

x = ("ade", "ola", "seun")
y = ("quayyum",)
x += y
print (x)

fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)

# LOOP
fruits = ("apple", "banana", "cherry")
for x in fruits :
    print(x)

thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
  print(thistuple[i])

fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

print(mytuple)