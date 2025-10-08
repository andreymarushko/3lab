
print("1. Вводите числа (0 для завершения):")
sum1 = 0
while True:
    num = float(input("Введите число: "))
    if num == 0:
        break
    sum1 += num
print(f"   Сумма введённых чисел: {sum1}\n")

print("2. Вводите числа (отрицательное для завершения):")
count2 = 0
while True:
    num = float(input("Введите число: "))
    if num < 0:
        break
    count2 += 1
print(f"   Количество введённых чисел: {count2}\n")

print("3. Вводите числа (чётное для завершения):")
sum_odd = 0
while True:
    num = int(input("Введите целое число: "))
    if num % 2 == 0:  # Чётное число
        break
    sum_odd += num
print(f"   Сумма нечётных чисел: {sum_odd}\n")

print("4. Вводите числа (число > 100 для завершения):")
total = 0
count4 = 0
while True:
    num = float(input("Введите число: "))
    if num > 100:
        break
    total += num
    count4 += 1

if count4 > 0:
    average = total / count4
    print(f"   Среднее арифметическое: {average:.2f}")
else:
    print("   Не было введено чисел")