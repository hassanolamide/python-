# A function name must start with a letter or underscore
# A function name can only contain letters, numbers, and underscores
# Function names are case-sensitive (myFunction and myfunction are different)

def myfxn():
    print("hello")

myfxn()
myfxn()
myfxn()


# return valuue
# Instead of using print we return a value and call it inside a print.

def fahrenheit_to_celsius(fahrenheit):
    return(fahrenheit - 32) * 5 / 9
print(fahrenheit_to_celsius(77))
print(fahrenheit_to_celsius(95))
print(fahrenheit_to_celsius(50))

def get_gretting():
    return "Great omotan"
message = get_gretting()
print(message)

# using a retun value directly
def get_gretting():
    return "greet my babe"
print(get_gretting())

# PASS
def my_function():
    pass

# Arguement is the example belor is olamide
# Parameter in this example below is names.

def my_name(names):
    return (names + " age")
print(my_name("olamide"))

def my_names (fname, lname):
    return(fname + " " + lname)
print(my_names("abdul" ,"quayyum"))
 
# intialize a value from the parameter

def my_country(country = "england"):
    return("i am from " + country )

print(my_country("nigeria"))
print(my_country())
print(my_country("argentina"))

# Assign specific keys to the a specifc argument.

def my_animal(animal, pet):
    print( "i am an " + animal)
    print("The name of my animal is " + pet)

my_animal("mamal","cat")
 
def my_dictionary(person):
    print("Name:", person["name"])
    print("Age", person[ "age"])

my_dictionary({"name":"ola", "age": 45})

# Picking a particular argument from diffrent argument
def My_nuumber(*kids):
    print("The name of my ssecond born is ", kids)

My_nuumber("Ade", "ola", "shola")
        
# Accessing values from **kwargs:
def my_function(**myvar):
  print("Type:", type(myvar))
  print("Name:", myvar["name"])
  print("Age:", myvar["age"])
  print("All data:", myvar)

my_function(name = "Tobias", age = 30, city = "Bergen")


def my_function(a, b, c):
  return a + b + c

numbers = [1, 2, 3]
result = my_function(*numbers) # Same as: my_function(1, 2, 3)
print(result)

def my_function(fname, lname):
  print("Hello", fname, lname)

person = {"fname": "Emil", "lname": "Refsnes"}
my_function(**person) 

def max_num (num1,num2,num3):
    if num1 >= num2 and num1 >= num3:
        return (num1)
    elif num2 >= num1 and num2 >= num3:
        return(num2)
    else:
        return num3
print(max_num(30,450,66))
