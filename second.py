fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newList =[]

for x in fruits:
    if "a" in x:
        newList.append(x)

print(newList)



fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if x != "apple"]
print(newlist)


fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x if x != "banana" else "orange" for x in fruits]
print(newlist)



# sort lst


newlist= ["apple", "banana", "cherry", "kiwi", "mango"]
newlist.sort(reverse = True)
print(newlist)


def myfunc(n):
    return abs(n-50)
thelist = [100, 40, 29, 33, 84]
thelist.sort(key = myfunc)
print(thelist)



newlist= ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x.upper() for x in newlist]
print(newlist)



# LIST JOINING

list1 = ["a", "b", "c"]
list2 = [ 1,2,3,4]

list3 = list1 + list2
print(list3)