from car import Car

class UberFlash(Car):
    direccionRetiro  = str
    direccionEntrega = str
    
    def __init__(self, placa, modelo, color, año, matricula, driver, direccionRetiro, direccionEntrega,):
        super().__init__(placa, modelo, color, año, matricula, driver)
        self.direccionRetiro   = direccionRetiro
        self.direccionEntrega  = direccionEntrega