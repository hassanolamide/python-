# set are use to store multible item in one variable.
# They are written in {}
# to add you use .add 
# to add more than one item you use .update
# To remove you use the remove or the discard.
# interception print out the common btw both set.
# diffrence is the opposite of interception.
#  symmetric_difference keeps itam that are not on both side

thisset = {"one", "two", "three", "one"}
print(thisset)

thisset = {"apple", "banana", "cherry", True, 1, 2}

print(thisset)

thisset = {"apple", "banana", "cherry"}
for x in thisset :
    print(x)

thisset = {"apple", "banana", "cherry"}
print ("banana" not in thisset)

thisset = {"apple", "banana", "cherry"}
thisset.add("bread")
print(thisset)


thisset = {"apple", "banana", "cherry"}
getin = {"fruits", "orange", "pawpaw"}

thisset.update(getin)
print(thisset)



set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}
myset = set1 | set2 | set3 | set4

print (myset)

set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}
sets = set3.intersection(set4)

print(sets)

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.intersection(set2)
print(set3)

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.difference_update(set2)
print(set3)

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 ^ set2
print(set3)

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set2.difference_update(set1)

print(set2)