
print("1. Операции с множествами:")
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
print(f"Пересечение: {set1 & set2}")
print(f"Объединение: {set1 | set2}")


print("\n2. Уникальные слова:")
text = input("Введите текст: ").lower()
words = set(text.split())
print(f"Уникальные слова: {words}")


print("\n3. Общие элементы:")
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
common = set(list1) & set(list2)
print(f"Общие элементы: {common}")

print("\n4. Проверка подмножества:")
set_a = {1, 2, 3}
set_b = {1, 2, 3, 4, 5}
print(f"Является ли {set_a} подмножеством {set_b}: {set_a.issubset(set_b)}")


print("\n5. Удаление элементов:")
num_set = {1, 5, 10, 15, 20}
threshold = int(input("Введите число: "))
num_set = {x for x in num_set if x >= threshold}
print(f"Множество после удаления: {num_set}")