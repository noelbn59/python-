# class person:
#     def __init__(self,fname,lname):
#         self.firstname=fname
#         self.lastname=lname
#     def printname(self):
#          print(self.firstname,self.lastname)
# x=person("Noel","Binu")
# x.printname()




# class person:
#     def __init__(self,fname,lname):
#         self.firstname = fname
#         self.lastname = lname
#     def printname(self):
#         print(self.firstname,self.lastname)
# class student(person):
#     pass
# x=student("Noel","Binu")
# x.printname()



# class Person:
#     def __init__(self, fname, lname): 
#         self.firstname = fname
#         self.lastname = lname

# class Student(Person):
#     def __init__(self, fname, lname, year):  
#         super().__init__(fname, lname)       
#         self.graduationyear = year

#     def welcome(self):
#         print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

# s1 = Student("Mike", "Olsen", 2025)
# s1.welcome()





class shape:
    def __init__(self,rectangle,circle):
        self.rectangle = rectangle
        self.circle = circle
class rectangle(shape):
    def __init__(self,length,width):
          self.length = length
          self.width = width

    def area(self):
         return   self.length * self.width
    
class circle(shape):
     def __init__(self, radius):
         self.radius = radius
    
     def area(self):
          return 3.14 * self.radius * self.radius
     
x = rectangle(7,5)
y =  circle(4)

print("Area of rectangle:",x.area())
print("Area of circle:",y.area())
         
         

