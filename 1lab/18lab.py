num2 = int(input("1. Введите двузначное число: "))
digit1 = num2 // 10
digit2 = num2 % 10
sum_2 = digit1 + digit2
print(f"   Сумма цифр: {digit1} + {digit2} = {sum_2}")

product_2 = digit1 * digit2
print(f"2. Произведение цифр: {digit1} × {digit2} = {product_2}")

num3 = int(input("\n3. Введите трёхзначное число: "))
digit1_3 = num3 // 100
digit2_3 = (num3 // 10) % 10
digit3_3 = num3 % 10
sum_3 = digit1_3 + digit2_3 + digit3_3
print(f"   Сумма цифр: {digit1_3} + {digit2_3} + {digit3_3} = {sum_3}")

print(f"4. Первая цифра: {digit1_3}, Последняя цифра: {digit3_3}")