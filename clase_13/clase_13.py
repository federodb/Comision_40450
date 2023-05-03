
class Perro:

    cantidad = 0

    def __init__(self, nombre, raza):
        self.__nombre = nombre
        self.raza = raza
        self.algo = None
        Perro.cantidad += 1

    def muestra_nombre(self):
        print(self.nombre)
        self.algo = "100"
    
    def imprimo_cualquier_cosa(self):
        self.__set_nombre()

    def __set_nombre(self, nombre):
        if nombre:
            self.__nombre = nombre
        return "Error"

    def __str__(self):
        return self.__nombre


perro1 = Perro("Lazy", "caniche")

perro1.__set_nombre("Yasi")

print(perro1)