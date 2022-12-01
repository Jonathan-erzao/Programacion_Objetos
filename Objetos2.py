class miClase:
    x = 5

p1 = miClase()
print(p1.x)

class persona:
    nombre = str
    edad = int
    
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return f'Su nombre es:{self.nombre}'

p2 = persona("Diego", 29)
print(p2)

class persona2:
    nombre = str
    edad = int
    cedula = str
    
    def __init__(self,nombre,edad,cedula):
        self.nombre = nombre
        self.edad = edad
        self.cedula = cedula
    
    def  miFuncion(self):
        print("hola mi nombre es " + self.nombre + "mi edad es " + self.edad + "mi cedula es" + self.cedula)
        
p3 = persona2("Alexander", 19,"1728733070")
p3.miFuncion()

class persona3:
    nombre = str
    edad = int
    estatura = int
    
    def __init__(self,nombre,edad,estatura):
        self.nombre = nombre
        self.edad = edad
        self.estatura = estatura
    def __str__(self):
        return f'Su nombre es:{self.nombre} y su estatura es de {self.estatura}'

p4 = persona("Diego", 29)
print(p2)