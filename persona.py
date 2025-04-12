# Define la clase persona:

class Persona: 
    # Constructor co atributos de instancia.
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def presentarse(self):
        print ("Hola, mi nombre es", self.nombre, "y tengo", self.edad, "años")

persona1 = Persona ("Ana", 28)
persona2 = Persona ("Luis", 35)

# Uso del metodo para mostrar la información de cada una de las instancias.

persona1.presentarse()
persona2.presentarse()