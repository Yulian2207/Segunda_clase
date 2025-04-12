# Definir una clase

class Vehiculo: 
    # Atributo de clase que se compartirá entre todas las instancias
    tipo = "Transporte"
    
    # Constructor
    def __init__(self, marca, modelo, year):
        self.marca = marca
        self.modelo = modelo
        self.year = year
    
    def información (self):
        print ("Vehiculo", self.marca, self.modelo, "del año", self.year)
        print ("Tipo", Vehiculo.tipo)
 
# Creación de las instancias de la clase vehiculo
vehiculo1 = Vehiculo ("Ford", "Mustang", 1967)
vehiculo2 = Vehiculo ("Chevrolet", "Camaro", 1969)

# Muestra la información de cada vehiculo
vehiculo1.información()
vehiculo2.información()