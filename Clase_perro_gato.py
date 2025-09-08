class Perro:
    def __init__(self, nombre, raza):
        self.nombre = nombre
        self.raza = raza

    def ladrar(self):
        print(f"El perro {self.nombre} de raza{self.raza} esta ladrando... ¡Guauu!")
        

class Gato:
    def __init__(self, nombre, raza):
        self.nombre = nombre
        self.raza = raza

    def maullar(self):
        print(f"El gato {self.nombre} de raza{self.raza} esta maullando... ¡Miaau!")
        

datosGato = (input("Ingrese el nombre del gato, y su raza separados por coma: "))
nombreGato, razaGato = datosGato.split(",") 
miGato = Gato(nombreGato, razaGato)

 
datosPerro = (input("Ingrese el nombre del Perro, y su raza separados por coma: "))
nombrePerro, razaPerro = datosPerro.split(",") 
miPerro = Perro(nombrePerro, razaPerro)

miGato.maullar()
miPerro.ladrar()