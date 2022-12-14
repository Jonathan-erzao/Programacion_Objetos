from padre import Persona
from padre import Persona2
from madre import Madre

class Hijo3(Persona):
    vivienda = str
    
    def __init__(self, nombre, apellido, edad, vivienda):
        super().__init__(nombre, apellido, edad)
        self.vivienda
    
hijo3 = Hijo3



class Hijo4(Persona2):
    edad     = int
    semestre = str
    
    def __init__(self, nombre , apellido, edad, semestre):
        super().__init__(nombre, apellido)
        self.edad     = edad
        self.semestre = semestre
        
    def felicitar(self, padre):
        return f'Felicidades {self.nombre} acabas de terminar tu {self.semestre} semestra a tus {self.edad}'
    
padre4 = Persona2("Carlos", "Borja")
hijo4  = Hijo4("Ivan", "Borja", 18, "Quinto")

print(vars(padre4))
print(vars(hijo4))
print(hijo4.felicitar(padre4))

class Hijofinal(Madre):
    nombre           = str
    apellidoPaterno  = str 
    apellidoMaterno  = str
    #padre = Padre ("", "", "", "")
    madre            = Madre ("", "", "", "")
    
    def __init__(self, nombre, apellidoPaterno, apellidoMaterno, edad, ciudad, madre):
        super().__init__(nombre, edad, ciudad)
        self.apellidoMaterno = apellidoMaterno
        self.apellidoPaterno = apellidoPaterno
       #self.padre           = padre
        self.madre           = madre
        
#padrefinal = Padre("German", "Yanez", 55, "Quito")
#madrefinal = Madre("Veronica", "Flores", 55, "Quito")
hijofinal  = Hijofinal("Diego", "Yanez", "Florez", 29 , "QUito", Madre("Veronica", "Flores", 55, "Quito"))

#print(vars(padrefinal))
#print(vars(madrefinal))
print(vars(hijofinal))
