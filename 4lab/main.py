class Transport:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed
    
    def move(self):
        print(f"Transport is moving at {self.speed} km/h")
    
    def __str__(self):
        return f"Transport: {self.brand}, Speed: {self.speed}"


class Car(Transport):
    def __init__(self, brand, speed, seats):
        super().__init__(brand, speed)
        self.seats = seats
    
    def honk(self):
        print("Beep beep!")
    
    def move(self):
        print(f"Car {self.brand} is driving at {self.speed} km/h")
    
    def __str__(self):
        return f"Car: {self.brand}, Speed: {self.speed}, Seats: {self.seats}"
    
    def __len__(self):
        return self.seats
    
    def __eq__(self, other):
        if isinstance(other, Car):
            return self.speed == other.speed
        return False
    
    def __add__(self, other):
        if isinstance(other, Car):
            return self.speed + other.speed
        return NotImplemented


class Bike(Transport):
    def __init__(self, brand, speed, bike_type):
        super().__init__(brand, speed)
        self.type = bike_type
    
    def move(self):
        print(f"Bike {self.brand} is cycling at {self.speed} km/h")
    
    def __str__(self):
        return f"Bike: {self.brand}, Speed: {self.speed}, Type: {self.type}"


# 4. Практика использования
print("Создание объектов")
transport1 = Transport("Autobas", 60)
car1 = Car("Toyota", 120, 5)
car2 = Car("Honda", 100, 4)
bike1 = Bike("Mers", 25, "mountain")

print("\nВывод объектов (__str__)")
print(transport1)
print(car1)
print(car2)
print(bike1)

print("\nПроверка методов move() и honk()")
transport1.move()
car1.move()
car1.honk()
bike1.move()

print("\nИспользование len(car)")
print(f"Количество мест в {car1.brand}: {len(car1)}")

print("\nСравнение двух машин (car1 == car2)")
print(f"{car1.brand} == {car2.brand}: {car1 == car2}")

print("\nСложение скоростей двух машин (car1 + car2)")
print(f"Суммарная скорость {car1.brand} и {car2.brand}: {car1 + car2}")

print("\nПопытка сложить машину и велосипед")
try:
    result = car1 + bike1
    print(f"Результат: {result}")
except TypeError as e:
    print(f"Ошибка: {e}")
    print("Объяснение: Метод __add__ в классе Car проверяет, является ли второй объект экземпляром Car.")
    print("Если нет - возвращает NotImplemented, что вызывает TypeError.")


print("\nДополнительное задание")
vehicles = [
    Transport("Generic", 50),
    Car("BMW", 150, 5),
    Car("Ford", 110, 4),
    Bike("Trek", 30, "road"),
    Bike("Specialized", 20, "mountain")
]

print("Список транспортных средств:")
for vehicle in vehicles:
    print(f"  - {vehicle}")

print("\nВызов метода move() для всех транспортных средств:")
for vehicle in vehicles:
    vehicle.move()

print("\nПринцип ООП, который демонстрируется: ПОЛИМОРФИЗМ")
print("Разные типы объектов (Transport, Car, Bike) могут отвечать на один и тот же метод (move()) по-разному,")
print("но интерфейс вызова остается одинаковым.")