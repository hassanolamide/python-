# __init__is called an initalize fxn.self.name 
#  self.name  is an atttribute of student, it means the acrtual object name is equal to the name that was input. 
# class Student:

#      def __init__(self, name, major, gpa, is_on_probation  ):
#           self.name = name
#           self.major = major
#           self.gpa = gpa
#           self.is_on_probation = is_on_probation

class Student:
     def __init__(self,name,age, course):
        self.name = name
        self.age =age
        self.course = course
        
     def introduce(self):
         print(f"My name is {self.name}, I am {self.age} years old, and I study {self.course}.")

     def change_course(self,new_course):
            self.course = new_course
            

   

        