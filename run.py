from modelo import *
persona = Persona_Equipo()
persona.setNombre("Luis")
persona.entrenar()
f = Futbolista()
f.setNombre("Enner")
f.entrenar()
e = Entrenador()
e.entrenar()

Lista = [persona, f, e]

for l in Lista:
    l.entrenar()
