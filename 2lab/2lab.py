import random


numbers = [random.randint(-59, 50) for _ in range(10)]
print(f"Исходный список: {numbers}")

print("\n1. Чётные элементы:")
even_numbers = [x for x in numbers if x % 2 == 0]
print(f"Чётные: {even_numbers}")


print("\n2. Максимум и минимум:")
print(f"Максимум: {max(numbers)}, Минимум: {min(numbers)}")


print("\n3. Ввод 5 чисел:")
user_numbers = []
for i in range(5):
    num = int(input(f"Введите число {i+1}: "))
    user_numbers.append(num)
user_numbers.sort()
print(f"Отсортированный список: {user_numbers}")

print("\n4. Удаление дубликатов:")
unique_list = []
for item in numbers:
    if item not in unique_list:
        unique_list.append(item)
print(f"Список без дубликатов: {unique_list}")


print("\n5. Обмен первого и последнего:")
if len(numbers) >= 2:
    numbers[0], numbers[-1] = numbers[-1], numbers[0]
print(f"После обмена: {numbers}")