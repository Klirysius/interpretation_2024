from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed

    @abstractmethod
    def move(self):
        pass

    @abstractmethod
    def stop(self):
        pass

    def get_speed(self):
        return self.speed


class Train(Vehicle):
    def __init__(self, name, speed, num_carriages):
        super().__init__(name, speed)
        self.num_carriages = num_carriages

    def move(self):
        print(f"{self.name} едет по рельсам")

    def stop(self):
        print(f"{self.name} остановился")

    def add_carriage(self):
        self.num_carriages += 1
        print(f"{self.name} имеет {self.num_carriages} вагонов")


class Airplane(Vehicle):
    def __init__(self, name, speed, max_altitude):
        super().__init__(name, speed)
        self.max_altitude = max_altitude

    def move(self):
        print(f"{self.name} летит по воздуху")

    def stop(self):
        print(f"{self.name} приземлился")

    def ascend(self, altitude):
        print(f"{self.name} взлетел на высоту {altitude}")
        self.max_altitude = altitude

    def descend(self, altitude):
        print(f"{self.name} снизился до {altitude}")
        self.max_altitude = altitude


V = Vehicle("Б", 123)
train = Train("Экспресс", 100, 10)
airplane = Airplane("Боенг 747", 500, 35000)

print(train.name)
print(train.get_speed())
train.move()
train.add_carriage()
train.stop()

print(airplane.name)
print(airplane.get_speed())
airplane.move()
airplane.ascend(40000)
airplane.descend(20000)
airplane.stop()
