
num1 = float(input("Введите первое число: "))
num2 = float(input("Введите второе число: "))
if num1 > num2:
    print(f"Большее число: {num1}")
elif num2 > num1:
    print(f"Большее число: {num2}")
else:
    print("Числа равны")
if num1 < num2:
    print(f"Меньшее число: {num1}")
elif num2 < num1:
    print(f"Меньшее число: {num2}")
else:
    print("Числа равны")
difference = abs(num1 - num2)
print(f"Разница между числами: {difference}")
if num1 == num2:
    print("Числа равны")
else:
    print("Числа не равны")