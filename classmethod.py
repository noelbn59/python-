
class Person:
    age = 25

    def printAge(cls):
        print("Age:", cls.age)

Person.printAge = classmethod(Person.printAge)
print(Person.age)











