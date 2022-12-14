from pprint import pprint
from UberXL import UberXL
from acountUser import User
from account import Account
from accountDrives import Driver
from account import Account
from car import Car
from payment import Payment
from paymentCard import PaymentCard
from paymentCash import PaymentCash
from paymentTransfer import PaymentTransferencia
from route import Route
from trip import Trip
from UberX import UberX
from UberConfort import UberConfort
from UberX import UberX
 
if __name__ == "__main__":
    usuario1 = User(1, "Diego Yanez", "Masculino", 9999999, 25)
    print(vars(usuario1))
    usuario2 = User(2, "Diego Yanez", "Masculino", 9999999, 35)
    print(vars(usuario2))
    
    #carro1 = Car("PCH-142", "Chevrolet Corsa", "Gris", 2015, Driver(3, "assd asda"))
    #print(vars(carro1))
    #UberX1 = UberX("XLX-5599", "Chevrolet Corsa", "Gris", 2015, "luis suquillo", 9999999, 22, "licencia1")    
    #print(vars(UberX1))
    
    uberXL1 = UberXL("PDF-123","sandoval","chevrolet", "rojo", 2023, 8,)
    print(vars(uberXL1))
    
    carro1 = Car("PBC-555555", "Chevrolet Corsa", "Gris", 2015, Driver(3, "Alexander Flores", "Masculino", 99999999))
    print(vars(carro1))
   
