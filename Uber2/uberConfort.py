from car import Car

class UberConfort(Car):
    aceptado   = bool
    asientos    = int
    tapizado   = str
    
    def __init__(self, placa, modelo, color, año, matricula, driver, acpetado, asientos, tapizado):
        super().__init__(placa, modelo, color, año, matricula, driver)
        self.aceptado  = acpetado
        self.asientos  = asientos
        self.tapizado  = tapizado