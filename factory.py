from abc import ABC, abstractmethod


class Functions(ABC):
    @abstractmethod
    def ride(self, time):
        pass

    @abstractmethod
    def fill(self):
        pass

    @abstractmethod
    def fueldat(self):
        pass



def ridefunction(fuel, rashod_per_km, distance):
    if fuel >= rashod_per_km * distance:
        print(f'\tПроехали {distance}км, потратили {rashod_per_km * distance}л топлива')
        fuel -= rashod_per_km * distance
    elif fuel > 0:
        print(f'\tПроехали {fuel / rashod_per_km}км, потратили {fuel}л топлива. Топлива больше нет')
        fuel = 0
    else:
        print('\tНет топлива')
    return fuel


class Car(Functions):
    def __init__(self, rashod, volume, speed):
        self.rashod = rashod  # расход топлива, л/100км
        self.volume = volume  # объём топливного бака, л
        self.speed = speed     # скорость км/ч
        self.fuel = 0        # количество топлива в баке, л

    def ride(self, time):
        rashod_per_km = self.rashod / 100
        distance = self.speed * time
        self.fuel = ridefunction(self.fuel, rashod_per_km, distance)

    def fill(self):
        print(f'\tЗалили в бак {self.volume - self.fuel}л топлива')
        self.fuel = self.volume

    def fueldat(self):
        print(f'\tВ баке {self.fuel}л топлива')
        return self.fuel


class Pickup(Car):
    def __init__(self):
        super().__init__(20, 85, 90)


class Citycar(Car):
    def __init__(self):
        super().__init__(10, 45, 110)


class UnknownCarException(Exception):
    def __str__(self):
        return '\tНеизвестный тип автомобиля:'


class Factory:
    def create(self, name):
        try:
            if name == 'pickup':
                print('\tЗавод выпустил пикап')
                return Pickup()
            elif name == 'citycar':
                print('\tЗавод выпустил городское авто')
                return Citycar()
            else:
                raise UnknownCarException
        except UnknownCarException as e:
            print(e, name)


class AbsImprover(Functions):
    def __init__(self, object):
        self.object = object

    def ride(self, time):
        self.object.ride()

    def fill(self):
        self.object.fill()

    def fueldat(self):
        self.object.fueldat()


class Nitro(AbsImprover):
    def ride(self, time):
        rashod_per_km = 2 * self.object.rashod / 100
        distance = 2 * self.object.speed * time
        self.object.fuel = ridefunction(self.object.fuel, rashod_per_km, distance)


class Econom(AbsImprover):
    def ride(self, time):
        rashod_per_km = self.object.rashod / 100 / 2
        distance = self.object.speed * time / 2
        self.object.fuel = ridefunction(self.object.fuel, rashod_per_km, distance)


class NeedForSpeed():
    def __init__(self, time):
        self.riders = set()
        self.time = time

    def enter(self, rider):
        self.riders.add(rider)

    def exit(self, rider):
        self.riders.remove(rider)

    def go(self):
        print('\tГонка стартовала')
        for num, car in enumerate(self.riders, start=1):
            if isinstance(car, Car):
                print('Участник номер', num)
                car.ride(self.time)

carfactory = Factory()
print('Производим пикапы')
pick1 = carfactory.create('pickup')
pick2 = carfactory.create('pickup')
pick3 = carfactory.create('pickup')
print('Производим городские авто')
car1 = carfactory.create('citycar')
car2 = carfactory.create('citycar')
car3 = carfactory.create('citycar')
print('Производим мотоцикл')
car4 = carfactory.create('moto')

print('Катаемся на пикапе')
pick1.ride(2)
pick1.fill()
pick1.fueldat()
pick1.ride(2)
pick1.fueldat()

print('Катаемся на городском авто')
car2.ride(2)
car2.fill()
car2.fueldat()
car2.ride(2)
car2.fueldat()


print('Машина с нитро')
car2.fill()
car2 = Nitro(car2)
car2.ride(1)
car2.fueldat()

print('Машина эконом')
car3.fill()
car3 = Econom(car3)
car3.ride(1)
car3.fueldat()


