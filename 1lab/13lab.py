
print("Таблица умножения на 2:")
for i in range(1, 11):
    print(f"2 × {i} = {2 * i}")
print("Таблица умножения на 5:")
for i in range(1, 11):
    print(f"5 × {i} = {5 * i}")
user_number = int(input("Введите число "))
print(f"\nТаблица умножения на {user_number}:")
for i in range(1, 11):
    print(f"{user_number} × {i} = {user_number * i}")
print("Таблица умножения на 10:")
for i in range(1, 11):
    print(f"10 × {i} = {10 * i}")