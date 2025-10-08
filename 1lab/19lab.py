char = input("Введите символ: ")

if len(char) == 1:
    if char.isdigit():
        print("1.Это цифра")
    else:
        print("1.Это не цифра")

    if char.isalpha():
        print("2.Это буква")
    else:
        print("2.Это не буква")

    vowels = "aeiouаеёиоуыэюяAEIOUАЕЁИОУЫЭЮЙЯ"
    if char in vowels:
        print("3.Это гласная буква")
    else:
        print("3.Это не гласная буква")

    if char.islower():
        print("4.Это прописная (строчная) буква")
    else:
        print("4.Это не прописная буква")
else:
    print("Ошибка: введите ровно один символ")