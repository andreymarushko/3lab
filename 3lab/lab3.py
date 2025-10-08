
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