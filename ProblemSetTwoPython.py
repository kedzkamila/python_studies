#Task 1: Generate a List of Even Numbers
#Create a program that generates a list of all the even numbers from 1 to 20

# even_numbers = [ x for x in range(1, 11)]
# print(even_numbers)

# even_numbers = []

# for i in range(1,21):
#     if i % 2 == 0:
#         even_numbers.append(i)

# print(even_numbers)

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
    
#     return(f"The first name is {first_name} and the last name is {last_name}")

# split_name("Kamila Kędzierska")

#Task 8: FizzBuzz
#Write a program that prints numbers from 1 to 100. For multiples of 3, print 'Fizz' instead of the number, and for multiples of 5, print 'Buzz.' For numbers that are multiples of both 3 and 5, print 'FizzBuzz.'

def FizzBuzz(n):
    for n in range (1, n+1):
        if n % 3 == 0:
            n == "Fizz"
            



#Task 9: Palindrome Checker
#Write a program that checks if a given word or phrase is a palindrome (reads the same backward as forward). Ignore spaces and punctuation.


#Task 10: List Comprehension for Even Numbers
#Create a program that generates a list of all the even numbers from 1 to 20 using list comprehension.

# even_numbers = [ x for x in range(1,21) if x % 2 == 0 ]
# print(even_numbers)

#Task 11: Prime Number Checker
#Create a program that generates a list of numbers from 1 to 100 using list comprehension. Then create a function check_if_prime_number(x) which checks whether x is a prime number (returns True or False). Finally, write another list comprehension, where you apply check_if_prime_number to every number in the previously created list and store the result to the new list if it is a prime number.

# list_of_numbers = [ x for x in range(1,101)]
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