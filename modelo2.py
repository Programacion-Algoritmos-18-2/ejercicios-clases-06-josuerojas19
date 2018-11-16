import abc
class Persona_Equipo(metaclass=abc.ABCMeta):

    def __init__(self, nom):
        self.nombre = nom

    def setNombre(self, n):
        self.nombre = n

    def getNombre(self):
        return self.nombre

    @abc.abstractmethod
    def entrenamiento(self):
        pass

class Entrenador(Persona_Equipo):
    def __init__(self, nom):
        super(Entrenador, self).__init__(nom)
        self.codigo_entrenador = ""
    def setCodigo(self ,c):
        self.codigo_entrenador = c
    def getCodigo(self):
        return self.codigo_entrenador
    def entrenamiento(self):
        print("Yo", self.getNombre(), ",soy el entrenador, Dirijo el etrenamiento")

class Futbolista(Persona_Equipo):
    def __init__(self, nom):
        super(Futbolista, self).__init__(nom)
        self.posicion_campo = ""

    def setPosicion(self, p):
        self.posicion_campo = p

    def getPosicion(self):
        return self.posicion_campo

    def entrenamiento(self):
        print("Yo", self.getNombre(), ",futbolista, hago Practica en el entrenamiento")

class MedicoEquipo(Persona_Equipo):
    def __init__(self, nom):
        super(MedicoEquipo, self).__init__(nom)
        self.titulo = ""
    def setTitulo(self, t):
        self.titulo = t

    def getTitulo(self):
        return self.titulo
    def entrenamiento(self):
        print("Yo", self.getNombre(), ",medico,atiendo los jugadores en el etrenamiento")

class PresidenteEquipo(Persona_Equipo):
    def __init__(self, nom):
        super(PresidenteEquipo, self).__init__(nom)
        self.numpropiedades = 0

    def setNumeroPropiedades(self, num):
        self.numpropiedades = num

    def getNumeroPropiedades(self):
        return self.numpropiedades;

    def entrenamiento(self):
        print("yo", self.getNombre(), ",presidente, pongo el dinero para el entrenamiento")


e = Entrenador("Pedro")
e2 = Futbolista("Juan")
e3 = MedicoEquipo("Luis")
e4 = PresidenteEquipo("Cristian")
Lista = [e, e2, e3, e4]

for l in Lista:
    l.entrenamiento()

