'''class fabricaTelefonos():
    marca = "Motorola"

    def elaborarHuawei(self):
        self.marca = "Huawei"

telefono = fabricaTelefonos()
telefono.elaborarHuawei()
print(telefono.marca)'''

class fabricaTelefonos():
    def __init__(self, marca, color):
        self.marca = marca
        self.color = color


telefono = fabricaTelefonos("alcatel","purpura")

print(telefono.marca,",", telefono.color)
