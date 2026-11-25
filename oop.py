# class is use to create another datatype. you can esentially define your own datatype 

# from student import Student

# student1 = Student("Ade","agric",4.09, False)
# student2 = Student("Bola","elect",3.09, True)

# print(student1.name)
# from question import question

# # setting the question
# question_prompts = [
#     "What color are apples?\n(a) Red/Green\n(b)purple\n (C)Orange\n\n",
#     "What color are Banana?\n(a) Teal\n(b)Magenta\n (C)Yellow\n\n",
#     "What color are strawberries?\n(a) yellow\n(b)Red\n (C)Blue\n\n"
# ]

# # Setting the answer.
# questions=[
#     question(question_prompts[0],"a"),
#     question(question_prompts[1],"c"),
#     question(question_prompts[2],"b")
# ]


# def run_test (questions):
#     score = 0
#     for question in questions:
#         answer = input(question.prompt)
#         if answer ==  question.answer:
#             score += 1

#     print( "You got"+ str(score) + "/ "+ str(len(questions))+ "correct")


# run_test(questions)


# class Student:
#     def __init__(self, name,age,course):
#         self.name = name
#         self.age = age
#         self.course = course


# student1 = Student(name="john",age =20,course= "python")
# student2 = Student(name= "Mary", age = 22, course = "python")

# print(student1.name)
# print(student2.name)


# class Phone:
#     def __init__(self, brand, model, price):
#         self.brand = brand
#         self.model = model
#         self.price = price


# phone1= Phone("Samsung", "S25", "₦850,000")
# phone2= Phone("Apple", "iPhone 16", "₦1,500,000")


# print(phone1.brand, phone1.model, phone1.price)
    

# class BankAccount:
#     def __init__(self, owner,balance):
#         self.owner = owner
#         self.balance = balance

# owner1 = BankAccount("john",50000)
# owner2 = BankAccount("Mary", 100000)

# print(owner1.owner, "with a balance of " ,"₦", format(owner1.balance, ",") )
# print(owner2.owner, "with a balance of ","₦",format(owner2.balance, ","))

# owner1.append(balance = 75000)

# class BankAccount:
#     def __init__(self, owner, balance):
#         self.owner = owner
#         self.balance = balance

    
#     def deposit(self, amount):

#         self.balance = self.balance + amount

# owner1 = BankAccount("john", 50000)

# owner1.deposit(10000)

# print(owner1.balance)

# class Student:
#     def __init__(self, name, age, course):
#         self.name = name
#         self.age = age
#         self.course = course

#     def __str__(self):
#         return(f"My name is {self.name}, and i an {self.age} years old , studying {self.course}")
        

# student1 = Student("John", 20, "Python")
# print(student1)

class Gamecharacter:
    def __init__(self,name, weapon, health):
        self.name = name
        self.weapon = weapon
        self.health = health

    def attack(self):
        print(f"{self.name} attack using {self.weapon}")
    def __str__(self):
        return(f"Name: {self.name}| Weapon: {self.weapon}| Health: {self.health}")

    def take_damage(self,damage):
        if damage < self.health:
            self.health = self.health - damage
        else:
            self.health = 0
owner1 =Gamecharacter("Shadow ","Sword" , 100 )  
owner2 =Gamecharacter("Blaze","Fireball",80 )

print(owner1)
print(owner2)


owner1.attack()
owner1.take_damage(30)
print(owner1)

owner1.take_damage(90)
print(owner1)

class Compare:
    def __init__(self, name ,year):
        self.name = name
        self.year = year
    def __eq__(self, value):
        return self.name == value.name and self.year == value.year 


acct1 = Compare("ade",45)
acc2 = Compare("ade", 45)

print(acct1 == acc2)

class Add:
    def __init__(self, num):
        self.num = num

    def __add__(self, other):
        return self.num + other.num

num1 = 34
num2 = 44


print (num1+num2)


# INERITANCE

class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating")

class Dog(Animal):
    pass

dog1 = Dog("Bingo")

print(dog1.name)
dog1.eat()




class Vehicle:
    def __init__(self, brand):
        self.brand = brand
    def start(self):
        print(f"{self.brand} is starting")

class car(Vehicle):
    def drive(self):
        print(f"{self.brand} is driving")

car1= car("Toyota")

print(car1.brand)

car1.start()
car1.drive()


# Polymorphism

class Drive:
    def move(self):
        print("Driving on the road")

class Ride:
    def move(self):
        print("Riding on the road")

