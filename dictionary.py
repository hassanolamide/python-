# A dictionary in Python stores data in key-value pairs.
# to get a model you use the ".get" 
# you change a specific value by calling it key.
# ".clear" to del the dictionary
# KEYYYYYYY
# fromkeys()	Returns a dictionary with the specified keys and value
# get()	Returns the value of the specified key
# items()	Returns a list containing a tuple for each key value pair
# keys()	Returns a list containing the dictionary's keys
# pop()	Removes the element with the specified key
# popitem()	Removes the last inserted key-value pair
# setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
# update()	Updates the dictionary with the specified key-value pairs
# values()	Returns a list of all the values in the dictionary

thisdict = {
    "name" : "Ola",
    "relationship": "used",
    "age": 99

}
print(len(thisdict))

thisdict = {
    "name" : "Ola",
    "relationship": "used",
    "age": 99

}
print(thisdict["name"])

thisdict = {
    "name" : "Ola",
    "relationship": "used",
    "age": 99,
    "color":["blue", "red", "green"]

}

thisdict["man"] = "abdul"

x = thisdict.items()
print(x)

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict["model"]
print(thisdict)

# LOOP to print key

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict:
    print(x)

# Loop to print values
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict:
    print(thisdict[x])

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

for x in thisdict.values():
    print(x)

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x , y in thisdict.items():
    print(x,y)



student={
    "student1":{
        "name":"Ade",
        "age":15
    },
    "student2":{
        "name":"ola",
        "age":10
    },
    "student3":{
        "name":"bode",
        "age":22
    }
}
for x, obj in student.items():
    print(x)

for y in obj:
    print(y + ":" ,obj[y])