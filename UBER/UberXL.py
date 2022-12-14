from car import Car

class UberXL():
    asientos = int
    
    def __init__(self, placa, nombre, modelo, color, año, asientos):
        super().__init__(placa, nombre, modelo, color, año, asientos)
        self.asientos = asientos
