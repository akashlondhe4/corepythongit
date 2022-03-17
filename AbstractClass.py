from abc import ABC, abstractmethod

class Car(ABC):
    def __init__(self, regno):
        self.regno = regno

    def open_tank(self):
        print("Fill the fuel in to the tank")
        print("For the car with registration Number, ",self.regno)

    @abstractmethod
    def steering(self):
        pass

    @abstractmethod
    def braking(self):
        pass

class Maruti(Car):
    def steering(self):
        print('Maruti use manual steering')
        print('Drive the car')

    def braking(self):
        print("Maruti use hydraulic break")
        print("apply break and stop it")

class Sentro(Car):
    def steering(self):
        print('Sentro use Power steering')
        print('Drive the car')

    def braking(self):
        print("Sentro use Gas break")
        print("apply break and stop it")


m = Maruti(1000)
m.open_tank()
m.steering()
m.braking()

m1 = Sentro(1001)
m1.open_tank()
m1.steering()
m1.braking()