# 1. Декоратор логирования

def logger(func):
    def wrapper(*args, **kwargs):
        # Перед вызовом функции
        print(f"Вызов функции {func.__name__} с аргументами {args} и {kwargs}")
        
        # Выполнение функции
        result = func(*args, **kwargs)
        
        # После выполнения функции
        print(f"Функция {func.__name__} вернула {result}")
        
        return result
    return wrapper

# Применение декоратора к функциям

@logger
def add(a, b):
    return a + b

@logger
def divide(a, b):
    if b == 0:
        return "Ошибка: деление на ноль"
    return a / b

@logger
def greet(name):
    return f"Привет, {name}!"


# 2. Декоратор доступа

def require_role(allowed_roles):
    def decorator(func):
        def wrapper(user, *args, **kwargs):
            if user.get('role') in allowed_roles:
                return func(user, *args, **kwargs)
            else:
                print(f"Доступ запрещён пользователю {user['name']}")
                return None
        return wrapper
    return decorator

# Пример использования декоратора доступа

@require_role(['admin'])
def delete_database(user):
    print(f"База данных удалена пользователем {user['name']}")

@require_role(['admin', 'manager'])
def edit_settings(user):
    print(f"Настройки изменены пользователем {user['name']}")


# Тестирование

print("=== Тестирование декоратора логирования ===")
print("add(5, 3):")
add(5, 3)

print("\ndivide(10, 2):")
divide(10, 2)

print("\ndivide(10, 0):")
divide(10, 0)

print("\ngreet('Анна'):")
greet('Анна')

print("\n=== Тестирование декоратора доступа ===")

# Создание пользователей с разными ролями
users = [
    {'name': 'Иван', 'role': 'admin'},
    {'name': 'Мария', 'role': 'manager'},
    {'name': 'Петр', 'role': 'user'},
    {'name': 'Анна', 'role': 'guest'}
]

# Тестирование функций с разными пользователями
for user in users:
    print(f"\nПользователь: {user['name']} (роль: {user['role']})")
    delete_database(user)
    edit_settings(user)