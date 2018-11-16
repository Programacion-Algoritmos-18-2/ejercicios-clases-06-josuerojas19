class Persona_Equipo(object):
    def __init__(self):
        self.nombre = " "

    def setNombre(self,n):
        self.nombre = n

    def getNombre(self):
        return self.nombre

    def entrenar(self):
        print("Entreno")

class Futbolista(Persona_Equipo):
    def __init__(self):
        super(Futbolista, self).__init__()
        self.posicion_campo = ""

    def setPosicion(self, p):
        self.posicion_campo = p

    def getPosicion(self):
        return self.posicion_campo

    def entrenar(self):
        print("Hago Practica en el entrenamiento")

class Entrenador(Persona_Equipo):
    def __init__(self):
        super(Entrenador, self).__init__()
        self.cargo_entrenador = ""

    def setCargo(self, c):
        self.cargo_entrenador = c

    def getCargo(self):
         return self.cargo_entrenador

