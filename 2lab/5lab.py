import random
from collections import Counter


print("1. Уникальные значения:")
random_numbers = [random.randint(1, 10) for _ in range(20)]
unique_values = list(set(random_numbers))
print(f"Случайные числа: {random_numbers}")
print(f"Уникальные: {unique_values}")


print("\n2. Словарь повторений:")
count_dict = {x: random_numbers.count(x) for x in set(random_numbers)}
print(f"Количество повторений: {count_dict}")


print("\n3. Слова длиной > 5:")
words = ["doter", "cdgoer", "backender", "frontend", "golang", "mysql"]
long_words = {word for word in words if len(word) > 5}
print(f"Длинные слова: {long_words}")


print("\n4. Количество вхождений слов:")
sentence = input("Введите предложение: ").lower()
word_count = {}
for word in sentence.split():
    word_count[word] = word_count.get(word, 0) + 1
print(f"Количество вхождений: {word_count}")


print("\n5. Удаление дубликатов:")
original_list = [1, 2, 2, 3, 4, 4, 5]
unique_list = list(set(original_list))
print(f"Исходный: {original_list}")
print(f"Без дубликатов: {unique_list}")

print("\n6. Самый дорогой товар:")
products = {"mers": 51, "volvo": 320, "bugati": 750, "arkana": 1000}
most_expensive = max(products, key=products.get)
print(f"Самый дорогой товар: {most_expensive} - {products[most_expensive]} руб.")


print("\n7. Анализ имён:")
names = ["Андрюха", "Машка", "Петя", "Андрюха", "Анна", "Машка"]
name_count = Counter(names)
duplicate_names = [name for name, count in name_count.items() if count > 1]
most_common = name_count.most_common(1)[0]
print(f"Повторяющиеся имена: {duplicate_names}")
print(f"Самое частое имя: {most_common[0]} ({most_common[1]} раз)")

print("\n8. Словарь индексов:")
text = input("Введите строку: ")
char_index = {}
for index, char in enumerate(text):
    if char not in char_index:
        char_index[char] = index
print(f"Символ → первый индекс: {char_index}")