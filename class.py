class myNumber:
    def __iter__(self):
        self.a = 1
        return self
    
    def __next__(self):
        x = self.a 
        self.a += 1
        return x
myclass = myNumber()
myiter = iter(myclass)


print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))

'''
What a Modules?
It is a file containing set of functions you want include an application
NOTE: When using a function from a module, use the syntax: module_name.function_name.


the syntax to use 

def greeting(name):
  print("Hello, " + name)
-------------------------
import mymodule

mymodule.greeting("Jonathan")


ANOTHER EXAMPLE 

person1 = {
  "name": "John",
  "age": 36,
  "country": "Norway"
}
-----------------------------

import mymodule

a = mymodule.person1["age"]
print(a) 


Create an alias for mymodule called mx:

import mymouldes as mk
'''

import datetime

# x = datetime.datetime.now()
# print(x)

x = datetime.datetime(2020, 5, 17)

print(x)

'''
JSON:  convert from json to phthon.(json.loads())
'''
import json
x = '{"name":"Mubarak", "age":"12", "sex":"disvirgin"}'

y = json.loads(x)
print(y["age"])

'''
Convert from python to json we will be using the (json.dumps())
'''
# x = {
#     "name": "John",
#   "age": 30,
#   "city": "New York"
# }

# y =json.dumps(x)
# print(y)


x = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

y = json.dumps(x, indent=4)

print(y)

'''Regular expression

^ → start of the text
The → must have the word "The"
.* → any characters, any number of them
Spain → must have "Spain"
$ → end of the text
'''


