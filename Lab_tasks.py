# Napisz program, który wyświetli liczby z zakresu od 1 do 1000 spełniające poniższe warunki:
# 1) są to liczby nieparzyste;
# 2) które dzielą się bez reszty przez 3;
# 3) oraz dzielą się bez reszty przez 7.

# for i in range(1, 1001):
#     if i % 2 == 1:
#         if i % 3 == 0:
#             if i % 7 == 0:
#                 print(i, end=" ")

# for i in range(21, 1001, 42):
#     print(i, end=" ")

# Z zakresu podanego przez użytkownika [a:b] sprawdź które liczby są liczbami pierwszymi.
# Liczba pierwsza = dzieli się tylko przez siebie i przez 1
# Zakładamy że a >= 2, b > a.

a = int(input("Give a number: "))
b = int(input("Give a number: "))

def is_prime(number):
    if number <= 1:
        return False    
    for j in range (2, int( number ** 0.5 + 1 )):
        if number % j == 0:
            return False
    return True

for n in range(a, b + 1):
    if is_prime(n):
        print(n)




# Policz i wyświetl wszystkie elementy ciągu Fibonacciego od 1 do N włącznie
# element0 = 0, element1 = 1, element2 = element1 + element0
# elementN = element(N-1) + element(N-2)

# punkty kratowe (wewnątrz okręgu) oraz punkty o współrzędnych całkowitych znajdujące się na okręgu

# sprawdź czy liczba jest doskonała, czyli czy jest równa sumie swoich dzielników właściwych, np. 6 = 3+2+1
# sprawdź czy liczba jest podzielna, czy dzieli się bez reszty przez sumę swoich cyfr
# sprawdź czy liczba jest liczbą pierwszą, a następnie czy jest liczbą super-pierwszą (czyli suma cyfr liczby pierwszej jest liczbą pierwszą)