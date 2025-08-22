# class student:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def display(self):
#         print("Name:",self.name)
#         print("Age:",self.age)
# s= student("John",22)
# s.display()








# class BankAccount:
#     def __init__(self,account_number,balance):
#         self.__account_number=account_number
#         self.__balance=balance
#     def __display_balance(self):
#         print("Balance:",self.__balance)
# b=BankAccount(123456789,5000)
# b.__display_balance()




# class person:
#     def __init__(self,name,age):
#          self._name=name
#          self._age=age
#     def _display(self):
#          print("Name:",self.name)
#          print("Age:",self.age)
# class student(person):
#      def __init__(self,name,age,roll_number):
#           super().__init__(name,age)
#           self._roll_number=roll_number

#      def _display(self):
#           self._display()
#           print("Roll Number:",self._roll_number)
# x=student("John",23,50)
# x._display()







class person:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    def _display(self):
        print("Name:", self._name)
        print("Age:", self._age)

class student(person):
    def __init__(self, name, age, roll_number):
        super().__init__(name, age)
        self._roll_number = roll_number

    def display(self):
        self._display()  
        print("Roll Number:", self._roll_number)

x = student("John", 23, 50)
x.display()
