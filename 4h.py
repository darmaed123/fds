
class Vehicle:
    def move(self):
        print("Транспортное средство движется")

    def fuel(self):
        return "Неизвестное топливо"

class Car(Vehicle):
    def move(self):
        print("Машина едет по дороге")

    def fuel(self):
        return "Бензин или дизельное топливо"

class Bicycle(Vehicle):
    def move(self):
        print("Велосипед едет по велосипедной дорожке")

    def fuel(self):
        return "Человеческая сила"

class Boat(Vehicle):
    def move(self):
        print("Лодка плывет по воде")

    def fuel(self):
        return "Дизельное топливо или электричество"

vehicles = [Car(), Bicycle(), Boat()]

for vehicle in vehicles:
    vehicle.move()

print("\nТипы топлива для различных транспортных средств:")
for vehicle in vehicles:
    print(f"{vehicle.__class__.__name__}: {vehicle.fuel()}")
