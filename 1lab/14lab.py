
sum1_10 = 0
for i in range(1, 11):
    sum1_10 += i
print(f"1. Сумма чисел от 1 до 10: {sum1_10}")

n = int(input("\n2. Введите число N: "))
sum1_n = 0
for i in range(1, n + 1):
    sum1_n += i
print(f"   Сумма чисел от 1 до {n}: {sum1_n}")

sum_ch = 0
for i in range(1, n + 1):
    if i % 2 == 0:
        sum_ch += i
print(f"3. Сумма чётных чисел от 1 до {n}: {sum_ch}")

sum_nch = 0
for i in range(1, n + 1):
    if i % 2 != 0:
        sum_nch += i
print(f"4. Сумма нечётных чисел от 1 до {n}: {sum_nch}")