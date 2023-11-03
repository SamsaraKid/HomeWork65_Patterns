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


class Car(Functions):
    def __init__(self, rashod, volume, speed):
        self._rashod = rashod  # расход топлива, л/100км
        self._volume = volume  # объём топливного бака, л
        self._speed = speed     # скорость км/ч
        self.__fuel = 0        # количество топлива в баке, л

    def ride(self, time):
        rashod_per_km = self._rashod / 100
        distance = self._speed * time
        if self.__fuel >= rashod_per_km * distance:
            print(f'\tПроехали {distance}км, потратили {rashod_per_km * distance}л топлива')
            self.__fuel -= rashod_per_km * distance
        elif self.__fuel > 0:
            print(f'\tПроехали {self.__fuel / rashod_per_km}км, потратили {self.__fuel}л топлива. Топлива больше нет')
            self.__fuel = 0
        else:
            print('\tНет топлива')

    def fill(self):
        print(f'\tЗалили в бак {self._volume - self.__fuel}л топлива')
        self.__fuel = self._volume

    def fueldat(self):
        print(f'\tВ баке {self.__fuel}л топлива')
        return self.__fuel


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
                print('\tЗавод выпустил горолское авто')
                return Citycar()
            else:
                raise UnknownCarException
        except UnknownCarException as e:
            print(e, name)


class AbsImprover(Functions):
    def __init__(self, object):
        self.object = object

    def ride(self, distance):
        self.object.ride()

    def fill(self):
        self.object.fill()

    def fueldat(self):
        self.object.fueldat()


class Nitro(AbsImprover):
    def ride(self, time):
        rashod_per_km = self._rashod / 100
        distance = self._speed * time
        if self.__fuel >= rashod_per_km * distance:
            print(f'\tПроехали {distance}км, потратили {rashod_per_km * distance}л топлива')
            self.__fuel -= rashod_per_km * distance
        elif self.__fuel > 0:
            print(f'\tПроехали {self.__fuel / rashod_per_km}км, потратили {self.__fuel}л топлива. Топлива больше нет')
            self.__fuel = 0
        else:
            print('\tНет топлива')



carfactory = Factory()
print('Производим пикап')
car1 = carfactory.create('pickup')
print('Производим городское авто')
car2 = carfactory.create('citycar')
print('Производим мотоцикл')
car3 = carfactory.create('moto')

print('Катаемся на пикапе')
car1.ride(2)
car1.fill()
car1.fueldat()
car1.ride(2)
car1.fueldat()

print('Катаемся на городском авто')
car2.ride(2)
car2.fill()
car2.fueldat()
car2.ride(2)
car1.fueldat()

car2 = Nitro(car2)
car2.ride(2)
car1.fueldat()

