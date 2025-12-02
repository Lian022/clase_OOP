class fabricaTelefonos ():
    def __init__(self, marca, color):
        self.marca = marca
        self.color = color
        print(f"los objetos fueron creados {self.marca}, {self.color}")

    def __del__(self):
        print(f"los objetos fueron destruidos {self.marca}, {self.color}")

    def __str__(self):
        return "los objetos son: {} y {}".format(self.marca, self.color)


telefono = fabricaTelefonos("manzanita mordida", "blanco 3 camaras")

print(telefono.marca)
print(telefono)