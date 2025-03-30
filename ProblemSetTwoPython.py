#Task 1: Generate a List of Even Numbers
#Create a program that generates a list of all the even numbers from 1 to 20

# even_numbers = [ x for x in range(1, 11)]
# print(even_numbers)

# even_numbers = []

# for i in range(1,21):
#     if i % 2 == 0:
#         even_numbers.append(i)

# print(even_numbers)

# even_number = [ x for x in range(1, 11) if x % 2 == 0 ]
# print(even_number)

#Task 2: : Sum of Positive Numbers
#Write a program that calculates the sum of all positive numbers in a list.

# numbers = [ x + 1 for x in range(20)]
# sum_of_positive_numbers = 0

# for i in numbers:
#     if i % 2 == 0:
#         sum_of_positive_numbers += i

# print(numbers)
# print(sum_of_positive_numbers)

#Task 3: Calculate Total Cost
#Create a function called calculate_total that takes two parameters: price and quantity. The function should calculate the total cost and return it.


# def calculate_total(price, quantity):
#     total_cost = price * quantity
#     return total_cost

# print(calculate_total(10, 5))
# print(calculate_total(6, 7))

#Task 4: Split Name Function
#Create a function called split_name that takes a full name as a parameter (e.g., 'John Smith') and returns two values: the first name and the last name.

# def split_name(full_name):
#     split_full_name = full_name.split()
#     first_name = split_full_name[0]
#     last_name = split_full_name[1]
#     print(f"The first name is {first_name} and the last name is {last_name}")

# split_name("Kamila Kędzierska")

#Task 5: Apply Operation Function
#Define a function called apply_operation that takes an operation function as an argument and applies it to two other values.

# def apply_operation( a, b, operation): 
#     operations = {
#     "addition": a + b,
#     "substraction": a - b,
#     "multiplication": a * b,
#     "division": a / b if b != 0 else "Error: Division by zero!"
#     }

#     result = operations.get(operation, "Error: Unkonw operation!")
#     return result 

# print(apply_operation(3, 4, "addition"))
# print(apply_operation(10, 2, "substraction"))
# print(apply_operation(5, 0, "division"))  
# print(apply_operation(6, 2, "unknown"))

#Task 6: Create Person Dictionary
#Create a function called create_person that takes arguments like first_name, last_name, age, and city and returns a dictionary representing a person's information.

# def create_person(first_name, last_name, age, city):
#     dict_create_person = {  
#     "first_name": first_name,
#     "last_name": last_name,
#     "age": age,
#     "city": city
#     }

#     return dict_create_person

# print(create_person("Kamila", "Kedz", 28, "Wrocław"))

#Task 7: Multiplication Table
#Write a program that prints the multiplication table for a number entered by the user. For example, if the user enters 7, the program should print the 7 times table from 1 to 10.



#Task 8: FizzBuzz
#Write a program that prints numbers from 1 to 100. For multiples of 3, print 'Fizz' instead of the number, and for multiples of 5, print 'Buzz.' For numbers that are multiples of both 3 and 5, print 'FizzBuzz.'

# for n in range(1, 101):
#     if n % 3 == 0 and n % 5 == 0:
#         print("FizzBuzz")
#     elif n % 3 == 0:
#         print("Fizz")
#     elif n % 5 == 0:
#         print("Buzz")
#     else:
#         print(n)

#Task 9: Palindrome Checker
#Write a program that checks if a given word or phrase is a palindrome (reads the same backward as forward). Ignore spaces and punctuation.

# word = input("Give a word: ").lower()

# if word == word[::-1]:
#     print("It's a palidrome word!")
# else:
#     print("It's not a palidrome word!")


#Task 10: List Comprehension for Even Numbers
#Create a program that generates a list of all the even numbers from 1 to 20 using list comprehension.

# even_numbers = [ x for x in range(1,21) if x % 2 == 0 ]
# print(even_numbers)

#Task 11: Prime Number Checker
#Create a program that generates a list of numbers from 1 to 100 using list comprehension. Then create a function check_if_prime_number(x) which checks whether x is a prime number (returns True or False). Finally, write another list comprehension, where you apply check_if_prime_number to every number in the previously created list and store the result to the new list if it is a prime number.

# list_of_numbers = [ x for x in range(1,101) ]
# print(list_of_numbers)

# def check_if_prime_number(x): 
#     for i in range(x):
#         if x <= 1:
#             return False
#         for j in range(2, int(x ** 0.5 + 1)):
#             if x % j == 0:
#                 return False
#                 break
#         else:
#             return True
        
# primers = [num for num in list_of_numbers if check_if_prime_number(num)]
        
# print(primers)

