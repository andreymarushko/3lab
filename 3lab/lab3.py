
def task1():
    squares = [x**2 for x in range(1, 11)]
    print("Квадраты чисел от 1 до 10:", squares)
    return squares
task1()

def task2():
    even_numbers = [x for x in range(1, 20) if x % 2 == 0]
    print("Четные числа от 1 до 19:", even_numbers)
    return even_numbers
task2()

def task3():
    words = ["python", "Java", "c++", "Rust", "go"]
    filtered_words = [word.upper() for word in words if len(word) > 3]
    print("Исходный список:", words)
    print("Слова в верхнем регистре длиннее 3 символов:", filtered_words)
    return filtered_words
task3()

class Countdown:
    def __init__(self, n):
        self.n = n
        self.current = n
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current < 1:
            raise StopIteration
        value = self.current
        self.current -= 1
        return value

def task4():
    print("Обратный отсчет от 5:")
    for x in Countdown(6):
        print(x, end=" ")
    print()  
task4()

def fibonacci(n):
    a, b = 0, 1
    count = 0
    while count < n:
        yield a
        a, b = b, a + b
        count += 1
def task5():
    print("Первые 5 чисел Фибоначчи:")
    for num in fibonacci(5):
        print(num, end=" ")
task5()

from decimal import Decimal, getcontext
def deposit_calculator():
    print("\n=== Задание 6 ===")
    # Устанавливаем точность вычислений
    getcontext().prec = 10
    
    # Ввод данных
    print("Введите параметры вклада:")
    initial_amount = Decimal(input("Начальная сумма вклада (руб.): "))
    interest_rate = Decimal(input("Годовая процентная ставка (%): "))
    years = Decimal(input("Срок вклада (лет): "))
    
    # Расчет по формуле: S = P × (1 + r/(12×100))^(12×t)
    monthly_rate = interest_rate / (12 * 100)
    months = years * 12
    final_amount = initial_amount * (1 + monthly_rate) ** months
    
    # Округляем до копеек (2 знака после запятой)
    final_amount = final_amount.quantize(Decimal('0.01'))
    profit = final_amount - initial_amount
    
    # Вывод результатов
    print("\nРезультаты расчета:")
    print(f"Начальная сумма: {initial_amount} руб.")
    print(f"Процентная ставка: {interest_rate}% годовых")
    print(f"Срок вклада: {years} лет")
    print(f"Итоговая сумма: {final_amount} руб.")
    print(f"Общая прибыль: {profit} руб.")
    
    return final_amount, profit

def task6():
    print("Пример расчета вклада:")

    initial_amount = Decimal('100000.50')  
    interest_rate = Decimal('7.5')         
    years = Decimal('3')                   
    
    getcontext().prec = 10
    monthly_rate = interest_rate / (12 * 100)
    months = years * 12
    final_amount = initial_amount * (1 + monthly_rate) ** months
    final_amount = final_amount.quantize(Decimal('0.01'))
    profit = final_amount - initial_amount
    
    print(f"Начальная сумма: {initial_amount} руб.")
    print(f"Процентная ставка: {interest_rate}% годовых")
    print(f"Срок вклада: {years} лет")
    print(f"Итоговая сумма: {final_amount} руб.")
    print(f"Общая прибыль: {profit} руб.")
    
    return final_amount, profit
task6()

from fractions import Fraction
def task7():
    frac1 = Fraction(3, 4)
    frac2 = Fraction(5, 6)
    
    print(f"Дробь 1: {frac1}")
    print(f"Дробь 2: {frac2}")
    
    addition = frac1 + frac2
    subtraction = frac1 - frac2
    multiplication = frac1 * frac2
    division = frac1 / frac2
    
    print("\nРезультаты операций:")
    print(f"Сложение: {frac1} + {frac2} = {addition}")
    print(f"Вычитание: {frac1} - {frac2} = {subtraction}")
    print(f"Умножение: {frac1} * {frac2} = {multiplication}")
    print(f"Деление: {frac1} / {frac2} = {division}")
task7()

from datetime import datetime
def task8():
    t = datetime.now()
    
    print("Текущая дата и время:")
    print(f"Полная дата и время: {t}")
    print(f"Только дата: {t.date()}")
    print(f"Только время: {t.time()}")
    
    print("\nАльтернативные форматы:")
    print(f"Дата (ISO формат): {t.date().isoformat()}")
    print(f"Время (ISO формат): {t.time().isoformat('seconds')}")
    
    return t
task8()