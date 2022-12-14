class Madre:
    nombre   = str 
    apellido = str
    edad     = int
    ciudad   = str
    
    def __init__(self,nombre, apellido, edad, ciudad):
        self.nombre   = nombre 
        self.apellido = apellido
        self.edad     = edad
        self.ciudad   = ciudad
        
    def Bienvenida(self, hijo):
        return f'Bunas noches {hijo.nombre} Bienvenido a casa, la cena esta en el microondas yo me encunetro de viaje {self.ciudad} att. {self.nombre} {self.apellido}'
