# To map with real world scenarios. we started using objects in code.
# This is called object oriented programming.

# class & object
# class is a blueprint for creating objects.

# creating class
class Student:
    name="sulbha"

s1=Student()
print(s1.name)   

s2=Student()
print(s2.name)

# 2 example

class Car:
    color="blue"
    brand="mercedes"

car1=Car()  
print(car1.color) 
print(car1.brand) 



# __init__ function.

# constructor
# All classes have a function called__init__(),which is always exwcuted when the class is being iniatiated.

# default contructors
# def __init__(self):
#     pass

# # parameterized contrructors
# class Student:
#     def __init__(self,fullname):
#         self.name=fullname
#         print("adding new student in database.")
        
# s1=Student("karan")
# print(s1.name)
# s2=Student("arjun")
# print(s2.name)
 
#  # "The self parameter is a reference to the current instance of the class,and is used to access variables that belongs to the class."


# # Class & Instance Attributes (ex. name, marks attribute value)

# # obj.attr > Class.attr
# # 1.Class.attr
# # 2.obj.attr


# # Methods
# # # Methods are functiontat belong to objects.( Functions=Methods )
# class students:
#     collage_name="ABC collage"
#     def __init__(self,name,marks):
#      self.name=name
#      self.marks=marks

#     def welcome(self):
#        print("welcome student",self.name)

#     def get_marks(self):
#        return self.marks    

# s1= students("karan",97)   
# s1.welcome() 
# print(s1.get_marks())




# # Let's practice

# # Create student class that takes name & marks of 3 subjects as arguments in contructor.Then create a method to print the average.

# class Student:
#    def __def__(self,name,marks):
#       self.name=name
#       self.marks=marks
#    def get_avg(self):
#       sum=0
#       for val in self.marks:
#          sum+=val
#       print("hi",self.name,"your avg score is:",sum/3)     
# s1 = Student("tony stark", [99, 98, 97])      
# s1.get_avg()

# s1.name="ironman"
# s1.get_avg()


# Static Methods(class level method)
 # methods that don't use the self parameter (work at class level)
 # @staticmethod   (decorater)

@staticmethod
def hello():
   print("hello")


# Important
# Abstraction --> Hiding the impletation details of a class and only showing the essential features to the user.

# Encapsulation --> Wrapping data and functions into a single unit(object).

# Let's practice

# Create account class with 2 attributes-balance&account no.
# Create methods for debit,credit&printing the balance.

class Account:
   def __def__(self,bal,acc):
      self.balance=bal
      self.account_no=acc

   def debit(self,amount):
      self.balance-=amount
      print("Rs.",amount,"was debited") 
      print("total balance=",self.get_balance()) 

   def credit(self,amount):
      self.balance+=amount
      print("Rs",amount,"was credited")   
      print("total balance=",self.get_balance()) 

   def get_balance(self):
      return self.balance 


acc1=Account(10000,12345) 
acc1.debit(1000)   
acc1.credit(500)













  


