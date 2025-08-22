# class Calculator():
#     def add(self,a=0,b=0,c=0):
#         return a+b+c
    
# c=Calculator()
# print(c.add(7,5))
# print(c.add(1,4,6))
# print(c.add(1))





# class Calculator():
#     def add(self,*args):
#         return sum(args)
    
# c=Calculator()
# print(c.add(3,3))
# print(c.add(3,3,3))
# print(c.add(4))



# class Animal:
#     def sound(self): 
#         print("Animal makes sound")
# class Dog(Animal):
#     def sound(self):
#         print("Dog barks")
# a = Animal()
# a.sound()

# d = Dog()
# d.sound()

# animal = Dog()
# animal.sound()




class Person:
    def __init__(self, fname, lname):  # Corrected __init__
        self.firstname = fname
        self.lastname = lname

class Student(Person):
    def __init__(self, fname, lname, year):  # Corrected __init__
        super().__init__(fname, lname)       # Corrected super().__init__()
        self.graduationyear = year

    def welcome(self):
        print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

s1 = Student("Mike", "Olsen", 2025)
s1.welcome()
