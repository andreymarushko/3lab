
print("1. Словарь студентов:")
students = {"Иван": 4.5, "Мария": 4.8, "Петр": 3.9, "Анна": 5.0}
average_score = sum(students.values()) / len(students)
print(f"Средний балл: {average_score:.2f}")


print("\n2. Подсчёт букв в строке:")
text = input("Введите строку: ")
letter_count = {}
for char in text:
    if char != " ": 
        letter_count[char] = letter_count.get(char, 0) + 1
print(f"Количество букв: {letter_count}")

print("\n3. Квадраты чисел:")
squares = {x: x**2 for x in range(1, 11)}
print(f"Квадраты: {squares}")


print("\n4. Объединение списков:")
keys = ["a", "b", "c"]
values = [1, 2, 3]
combined_dict = dict(zip(keys, values))
print(f"Объединённый словарь: {combined_dict}")