class Persona:
    nombre   = str
    apellido = str
    edad     = int
    
    def __init__(self, nombre, apellido, edad):
        self.nombre   = nombre
        self.apellido = apellido
        self.edad     = edad
        
if __name__ == "__main__":
    persona1 = Persona("Alison", "Cumbajin", 19)
    persona2 = Persona("Lenin", "Montalvo", 21)
    
    print(vars(persona1))
    print(vars(persona2))

#La funcion __str__

class Persona2:
    nombre   = str
    apellido = str
    edad     = int
    carrera  = str
    
    def __init__(self, nombre, apellido, edad, carrera):
        self.nombre   = nombre
        self.apellido = apellido
        self.edad     = edad
        self.carrera  = carrera
    
    def __init__(self, nombre, apellido, edad, carrera):
        self.nombre   = nombre
        self.apellido = apellido
        self.edad     = edad
        self.carrera  = carrera
        
class Persona3:
    nombre   = str
    apellido = str
    edad     = int
    carrera  = str
    
    def __init__(self, nombre, apellido, edad, carrera):
        self.nombre   = nombre
        self.apellido = apellido
        self.edad     = edad
        self.carrera  = carrera
    

class persona:
    nombre   = str
    apellido = str
    edad     = int
    
    def __init__(self, nombre, apellido, edad,):
        self.nombre   = nombre
        self.apellido = apellido
        self.edad     = edad
    
    def conversar(self,otra_persona):
        return f'hola {otra_persona.nombre} me llamo {self.nombre} {self.apellido}, {self.centroEstudios}'
