# from student import Student

# student1=Student("john",20,"python")
# student2 = Student("Mary",22,"javascript")

# student1.introduce()
# student2.introduce()

# student1.change_course = "Web Development"

# student1.introduce()

from Bankaccount import BankAccount

user1 = BankAccount("john", 50000)

print(f"My name is {user1.owner} and i have ₦ {user1.balance:,} naira.")

user1.deposit(10000)
print(f"My name is {user1.owner} and i have ₦ {user1.balance:,} naira.")

user1.subtract(900000)
print(f"My name is {user1.owner} and i have ₦ {user1.balance:,} naira.")

user1.check_balance()