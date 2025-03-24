#Task 1 : Hello, World!
#Write a Python program that prints "Hello, World!" to the console.

# print("Hello world!")

#Task 2 : Variables and Data Types
#Create variables to store an integer, a float, a string, and a boolean. Print out the values and data types of these variables.

# int = int(10)
# float = float(10.3)
# string = "Task"
# boolean = True

# print(int, type(int))
# print(float, type(float))
# print(string, type(string))
# print(boolean, type(boolean))

#Task 3 : Arithmetic Operations
#First, perform basic arithmetic operations (addition, subtraction, multiplication, and division) on two predefined variables x and y.
#For example, you can set x = 3 and y = 4.
#Then, extend the program to ask the user to input two numbers and perform the same operations.

# x = 3
# y = 4

# addition = x + y
# substraction = x - y
# multiplication = x * y
# division =  x / y

# print(addition)
# print(substraction)
# print(multiplication)
# print(division)

# a = int(input("Podaj liczbe naturalna: "))
# b = int(input("Podaj liczbe naturalna: "))

# addition = a + b
# substraction = a - b
# multiplication = a * b
# division =  a / b

# print(addition)
# print(substraction)
# print(multiplication)
# print(division)

#Task 4 : User Input
#Create a program that asks the user for their name and prints a greeting using their name.

# name = input("Podaj imie: ")
# print("Cześć", name.capitalize())

#upper zwraca tekst, w którym wszystkie małe litery zostały zamienione na wielkie
#lower zwraca tekst, w którym wszystkie wielkie litery zostały zamienione na małe
#capitalize zwraca tekst, w którym pierwsza litera zostaje zamieniona na wielka
#title zwraca tekst, w którym pierwsze litery kadego słowa zostają zamienione na wielkie
#replace zwraca tekst, w którym wszystkie wystąpienie jednego słowa zostają zastąpione innym

#Task 5 : Conditional Statements
#Check if two predefined variables are even or odd.
#For example, you can set x = 3 and y = 4.
#Then, extend the program to ask the user to input a number and determine if it is even or odd.

# x = 3 
# y = 4

# if x % 2 == 0:
#     print("The number", x, "is even.")
# else:
#     print("The number", x, "is odd.")

# if y % 2 == 0:
#     print("The number", y, "is even.")
# else:
#     print("The number", y, "is odd.")

# a = int(input("Give a number: "))

# if a % 2 == 0:
#     print("The number", a, "is even.")
# else:
#     print("The number", a, "is odd.")

#Task 6 : Loops
#Use a loop to print the numbers from 1 to 10.

# for i in range(1,11):
#     print(i)

#Task 7 : Lists and Loops

# fruits =  ["blueberries", "mango", "passionfruit", "watermelon", "blackberry", "raspberry", "apple"]

# for i in fruits:
#     print(i)

#Task 8 : String Manipulation
#Ask the user for their favorite quote, then print it in uppercase and lowercase.

# quote = input("Give your favorite quote: ")

# print(quote.upper())
# print(quote.lower())

#Task 9 : Lists and Conditionals
#Create a list of numbers. Write a program that finds and prints the largest number in the list.

#listy składane - pozwalaja na utworzenie nowej listy na podstawie istniejącej listy lub zakresu, ale po dokonaniu pewnych modyfikacji
#generator - określa co powinno znajdować się na nowej liście
#przykładowy generator: x * 10 for x in numbers - chcemy x * 10 dla kazdego x z numbers, taki generator będzie zwracał kolejne elementy z numbers, pomnozone przez 10

# numbers = [ x + 1 for x in range(10)]
# print(numbers)
# print("Największa wartość w numbers: ", max(numbers))
# print("Najmniejsza wartość w numbers: ", min(numbers))

#Task 10 : Loops
#Write a program that prints "Hello" 50 times, each on a new line.

# for i in range(50):
#     print("Hello")

#Task 11 : Working with Strings
#Write a program to print "Hello" 12 times on the same line, separated by spaces.

# for i in range(12):
#     print("Hello", end=" ")

#Task 12 : Loops and Data Types
#Given the list ' elements = [3, 7.76, True, "Argentine"] ', print each element and its type, each pair on a new line.

# elements = [3, 7.76, True, "Argentine"]

# for x in elements:
#     print("Element: ", x, type(x))

#Task 13 : Loops and Strings
#Define a variable `name = "your_name"`, for example name = "John Doe". Write a program that prints each letter of the name on a new line.

# name = "Kamila Kędzierska"

# for x in name:
#     print(x)

#Task 14 : Spotting mistakes
#Correct the following code snippets:

# print("Welcome to class!") #SyntaxError: unterminated string literal (detected at line 151)
# print("Programming is fun") #NameError: name 'Programming' is not defined
# print('Hello world!') #SyntaxError: unterminated string literal (detected at line 153)

#Task 15 : Division and Modulus Operators
#Run `print(10 // 3)` and `print(10 % 3)` and analyze what each operator (`//` and `%`) does.

# print(10 // 3)
# print(10 % 3) #reszta z dzielenia

#Task 16: Time Conversion
#Given `time_in_min = 505`, calculate the number of hours (`num_whole_hours`) and remaining minutes (`num_remaining_minutes`). Then print:
#"Number of hours and minutes in 505 min is <hours> hours and <minutes> minutes."

# time_in_min = 505

# num_whole_hours = time_in_min // 60
# num_remaining_minutes = time_in_min % 60

# print("Numbers of hours and minutes in", time_in_min, "is", num_whole_hours, "and", num_remaining_minutes, "minutes.")

#Task 17 : Exception Handling
#Create a program that asks the user to enter a number. Handle any exceptions that may occur if the user enters something that's not a number.

# while True: #uzycie petli, aby uzytkownik był proszony o podanie prawidłowej liczby do momenty, gdy wprowadzi poprawne dane
#     number = input("Enter a number: ")
#     if number.isdigit():
#         number = int(number)
#         print("Input is correct!")
#         break
#     else:
#         print("Enter a correct input.")

#Task 18 : Basic Calculator
#Build a basic calculator (function) that can perform addition, subtraction, multiplication, and division. The function should take two numbers and an operation and return the result of the operation.

# def calculator(a, b, operation):
#     if operation == "addition":
#         print("Result of the", operation, a + b)
#     elif operation == "substraction":
#         print("Result of the", operation, a - b)
#     elif operation == "multiplication":
#         print("Result of the", operation, a * b)
#     elif operation == "division":
#         print("Result of the", operation, a / b)

# calculator(3, 4, "division")

#Task 19 : Random Number Generator
#Generate a random number between 1 and 10 and ask the user to guess it. Provide feedback on whether their guess was too high, too low, or correct.

# import random

# number = random.randint(1,10)
# amount_of_guesses = 0

# while True:
#     guess = (input("Give a number: "))
#     if guess.isdigit():
#         guess = int(guess)
#         amount_of_guesses += 1
#         if number == guess:
#             print("You guessed the number!")
#             break
#         elif guess > number:
#             print("The number is too high.")
#         else:
#             print("The number is too low.")
#     else:
#         print("Invalid input! Enter a correct input.")

# print("It took", amount_of_guesses, "guesses.")

#rozwiązanie chatgpt

# import random

# number = random.randint(1, 10)
# amount_of_guesses = 0

# while True:
#     guess = input("Give a number between 1 and 10: ")

#     if not guess.isdigit():
#         print("Invalid input! Please enter a valid number.")
#         continue  # Pomija resztę pętli i wraca do początku

#     guess = int(guess)
#     amount_of_guesses += 1

#     if guess == number:
#         print("You guessed the number!")
#         break
#     elif guess > number:
#         print("The number is too high.")
#     else:
#         print("The number is too low.")

# print(f"It took you {amount_of_guesses} guesses.")