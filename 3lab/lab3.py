
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

