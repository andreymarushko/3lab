
factorial_3 = 1
for i in range(1, 4):
    factorial_3 *= i
print(f"1. Факториал 3! = {factorial_3}")

factorial_5 = 1
for i in range(1, 6):
    factorial_5 *= i
print(f"2. Факториал 5! = {factorial_5}")

n = int(input("\n3. Введите число N: "))
factorial_n = 1
for i in range(1, n + 1):
    factorial_n *= i
print(f"3. Факториал {n}! = {factorial_n}")

print("\n4. Вычисление факториалов (для выхода введите 0)")
while True:
    number = int(input("Введите число: "))
    if number == 0:
        print("Выход из программы")
        break
    if number < 0:
        print("Ошибка: факториал отрицательного числа не определен")
        continue
    
    factorial = 1
    for i in range(1, number + 1):
        factorial *= i
    print(f"Факториал {number}! = {factorial}")