from car import Car

class UberConfort(Car):
    aceptado   = bool
    asietos    = int
    tapizado   = str
    
    def __init__(self, placa, modelo, color, año, Driver, aceptado, asientos, tapizado):
        super().__init__(placa, modelo, color, año, Driver)
        
        self.aceptado = aceptado
        self.asietos  = asientos
        self.tapizado = tapizado
       
          
       