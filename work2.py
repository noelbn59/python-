# year=int(input("Enter a Year:"))
# if(year % 4 ==0 and (year % 100!= 0 or year % 400==0)):
#     print(year, "is leap year ")
# else:
#     print(year,"Year is not a leap year")





# marks = int(input("Enter your marks: "))

# if marks >= 90:
#     print("Grade: A")
# elif marks >= 80:
#     print("Grade: B")
# elif marks >= 70:
#     print("Grade: C")
# else:
#     print("Failed")




# char=input("Enter a character:").lower()
# if char.isalpha():
#     if char in 'aeiou':
#         print(f"'{char}' is a vowel.")
#     else:
#         print(f"'{char}' is a consonant.")
# else:
#     print("'{char}' is not a letter.")






# num1=int(input("Enter first number:"))
# num2=int(input("Enter second number:"))
# num3=int(input("Enter third number:"))
# if num1 >= num2 and num1 >= num3:
#     print(f"'{num1}' is the largest number.")
# elif num2 >= num1 and num2 >= num3:
#     print(f"'{num2}' is the largest number.")
# else:
#   print(f"'{num3}' is the largest number.")






# a=int(input("Enter a number:"))
# i = 0
# for i in range(1,11):
#     b = i * a
#     print(b)






# i = 0
# for i in range(1,11):
#     print(i)





# Print only even numbers from 1 to 20 using a loop.

# i = 1
# while i<= 20:
#     if i % 2==0:
#         print(i)
#     i += 1




# Write a Python program to find the sum and average of all elements in a list.

# def sum_average(lst):
#     total = sum(lst)
#     average = total /len(lst)
#     return total, average

# num = [5,10]
# total,average = sum_average(num)

# print(f"sum={total}")
# print(f"average={average:.2f}")




# Given a list of numbers, print only the even numbers.

# a =[1,2,3,4,5,6,7,8,9,10]
# even_num = [num for num in a if num%2==0]
# print("EvenNumbers:", even_num)




# Write a program to get the second largest number in a list.

# a =[23,45,32,65,13,75]
# second_largest = sorted(set(a))[-2]
# print("Second largest num:", second_largest)





# Find the maximum and minimum element in a list.

# a =[23,45,32,65,13,75]
# minimum=min(a)
# print("Minimum valus is:", minimum)
# maximum=max(a)
# print("Maximum value is:",maximum)





# Create a tuple with numbers and print only the odd numbers.

# a =(1,2,3,4,5,6,7,8,9,10)
# odd_numbers = [num for num in a if num % 2!=0]
# print("Odd numbers:",odd_numbers)





# Find the index of an element in a tuple.

# my_tuple = (20,30,40,50,60)
# index = my_tuple.index(40)
# print("index of 40:",index)





# Write a program to convert a tuple of characters to a string.

# a = ("N","O","E","L")
# result = ''.join(a)
# print("String:",result)




# Create a set of numbers and remove all even numbers.

# a = {1,2,3,4,5,6,7,8,9,10}
# for num in list(a):
#     if num % 2 == 0:
#         a.remove(num)
# print("After removing even numbers:",a)





# Write a program to update one set with items from another.

# set1 = {1,2,3,4}
# set2 = {5,6,7,8}
# set1.update(set2)
# print("Updated set 1:")
# print(set1)





# Add, update, and delete a key-value pair in a dictionary.

# person = {
#     "name" : "Noel",
#     "age" : 22,
#     "city" : "Thiruvalla"
# }

# person["country"] = "India"
# print("\n after adding 'country' key.")
# print(person)

# person["age"] = 21
# print("\n after updating 'age' key.")
# print(person)

# del person["city"] 
# print("\n after deleting 'city' key.")
# print(person)




# Write a program to count the frequency of characters in a string using a dictionary.

# string = input("Enter a string: ")
# frequency = {}
# count = 0
# for char in string:
#     if char in frequency:
#         frequency[char] += 1
#     else:
#         frequency[char] = 1
# print("Character frequency:", frequency)





# Convert two lists into a dictionary (one for keys, one for values).

# list1= ['a', 'b', 'c']
# list2 = [1, 2, 3]
# my_dict = dict(zip(list1,list2))
# print("Dictionary:",my_dict)




# Sort a dictionary by values.

my_dict = {'a': 3, 'b': 1, 'c': 2}
sorted_dict = dict(sorted(my_dict.items(), key=lambda item: item[1]))
print("Sorted Dictionary:", sorted_dict)