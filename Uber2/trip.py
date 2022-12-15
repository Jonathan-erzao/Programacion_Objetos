from car import Car
from accountDrives import Driver
from accountUser import User
from route import Route
from payment import Payment

class Trip(Car, Driver, User, Route, Payment):
    idTrip    = int
    
    def __init__(self, placa, modelo, color, año, matricula, driver, idTrip):
        super().__init__(placa, modelo, color, año, matricula, driver)
        self.idTrip = idTrip