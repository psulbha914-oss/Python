# del keyword
# used to delete object properties or object itself.

# class student:
#     def __init__(self,name):
#         self.name=name

# s1= student("sharadha") 
# print(s1.name) 
# del s1.name
# print(s1.name)



             # Private(like) attribute& methods #
# conceptual implementations in python
# private attributes & methods are meant to be used only within the class and are not accesible from outside the class.

class person:
    __name="sulbha"
    def __hello(self):
        print("hello person!")

    def welcome(self):
        self.__hello() 

p1= person()    



                         # Inheritance #

# When one class(child/derived)derives the properties & methods of another class(parent/base)

class A:
    varA="welcome to class A"

class B:
    varB="welcome to class B"

class C(A,B):
    varC="welcome to class C"    

c1=C() 
print(c1.varC)
print(c1.varB)
print(c1.varA) 


         # Property # 
class student:
    def __init__(self,phy,chem,math):
        self.phy=phy
        self.chem=chem
        self.math=math

    @property
    def percentage(self):
        return str((self.phy+self.chem+self.math)/3)+"%"


stu1=student(98,97,99)
print(stu1.percentage)

stu1.phy=84
print(stu1.percentage)


# Polymorphism # Operator Overloding
# When the same operater is allowed to the different meaning according to the context.

print(1+2)
print("sulbha"+"kachare")    # Basic
print([1,2,3]+[4,5,6])







  





