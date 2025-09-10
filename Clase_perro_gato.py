class Perro:
    def __init__(self, nombre, raza):
        self.nombre = nombre
        self.raza = raza

    def ladrar(self):
        print(f"El perro {self.nombre} de raza{self.raza} esta ladrando... ¡Guauu! \n")
    def felicidadperro(self):
        print(f"{self.nombre} ya comio ")
        print(f"{self.nombre} salio al parque ")
        print(f"{self.nombre} descanso y es feliz... ")

class Gato:
    def __init__(self, nombre, raza):
        self.nombre = nombre
        self.raza = raza

    def maullar(self):
        print(f"El gato {self.nombre} de raza{self.raza} esta maullando... ¡Miaau! \n ")

    def felicidadgato(self):
        print(f"{self.nombre} ya comio ")
        print(f"{self.nombre} jugo con su pelota ")
        print(f"{self.nombre} descanso y es feliz... ")

        

datosGato = (input("Ingrese el nombre del gato, y su raza separados por coma: "))
nombreGato, razaGato = datosGato.split(",") 
miGato = Gato(nombreGato, razaGato)

 
datosPerro = (input("Ingrese el nombre del Perro, y su raza separados por coma: "))
nombrePerro, razaPerro = datosPerro.split(",") 
miPerro = Perro(nombrePerro, razaPerro)

miGato.maullar()
miGato.felicidadgato()
miPerro.ladrar()
miPerro.felicidadperro()