
print("1. Таблица умножения:")
for i in range(1, 10):
    for j in range(1, 10):
        print(f"{i} * {j} = {i * j}\t", end="")
    print()


print("\n2. Сумма нечётных чисел от 1 до 100:")
sum_odd = sum(i for i in range(1, 101) if i % 2 != 0)
print(f"Сумма: {sum_odd}")


print("\n3. Поиск делителей числа:")
num = int(input("Введите число: "))
dividers = [i for i in range(1, num + 1) if num % i == 0]
print(f"Делители числа {num}: {dividers}")


print("\n4. Вычисление факториала:")
n = int(input("Введите число: "))
factorial = 1
for i in range(1, n + 1):
    factorial *= i
print(f"Факториал {n}! = {factorial}")

print("\n5. Последовательность Фибоначчи:")
n = int(input("Введите длину последовательности: "))
fib = [0, 1]
for i in range(2, n):
    fib.append(fib[i-1] + fib[i-2])
print(f"Первые {n} чисел Фибоначчи: {fib[:n]}")