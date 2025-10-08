
number = int(input("Введите число: "))
two = number ** 2
print(f"1. {number} в квадрате = {two}")

cube = number ** 3
print(f"2. {number} в кубе = {cube}")

n = int(input("\n3. Введите степень N: "))
power = number ** n
print(f"3. {number} в степени {n} = {power}")

n2 = int(input("\n4. Введите степень N для числа 2: "))
power2 = 2 ** n2
print(f"4. 2 в степени {n2} = {power2}")