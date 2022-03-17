from abc import *

class Myclass(ABC):
    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def disconnect(self):
        pass

class Oracle(Myclass):
    def connect(self):
        print("Connecting to oracle database...")

    def disconnect(self):
        print("Disconnecting from Oracle database...")

class Sybase(Myclass):
    def connect(self):
        print("Connecting to Sybase database...")

    def disconnect(self):
        print("Disconnecting from Sybase database...")

class Database:
    # accept database name as a string
    str = input('Enter database Name : ')

    # convert string into class name
    classname = globals()[str]

    # create an object to that class
    x = classname()

    x.connect()
    x.disconnect()