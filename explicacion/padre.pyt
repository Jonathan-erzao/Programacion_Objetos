#Herencia
class Persona:
    nombre   = str
    apellido = str 
    edad     = int

    def __init__(self, nombre, apellido, edad):
        self.nombre   = nombre 
        self.apellido = apellido
        self.edad     = edad
    
    def conversar(self, otra_persona):
        return f"Hola {otra_persona.nombre}, me llamo {self.nombre} {self.apellido} , tengo {self.edad} "

class Hijo(Persona):
    ciudad = str

    def __init__(self, nombre, apellido, edad, ciudad):
        Persona.__init__(self, nombre, apellido , edad)
        self.ciudad = ciudad

padre = Persona("Victor", "Grados", 50)
print(vars(padre))

hijo = Hijo ("Elena", "Grados", 25 , "Quito")
print(vars(hijo))

print(padre.conversar(hijo))
print(hijo.conversar(padre))

#Herencia2

class Persona2:
    nombre   = str
    apellido = str 

    def __init__(self, nombre, apellido):
        self.nombre   = nombre 
        self.apellido = apellido
    
    def conversar(self, otra_persona):
        return f"Hola{otra_persona.nombre}, me llamo {self.nombre} {self.apellido}"

class Hijo2(Persona2):
    estudios       = str
    lugardeestudio = str

    def __init__(self, nombre, apellido, estudios, lugardeestudio):
        super().__init__(nombre, apellido)
        self.estudios       = estudios
        self.lugardeestudio = lugardeestudio
        
    def informar(self, otra_persona):
        return f'Buenas tardes, {otra_persona.nombre} acabo de estudiar{self.materia}, llegue hace unos 20 minutos  '
    
padre2 = Persona2("Juan", "Flores")
hijo2 = Hijo2("Jose", "Perez", "POO", "IST YAVIRAC")

print()

class Padre:
    
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
    