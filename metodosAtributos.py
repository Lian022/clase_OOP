class FabricaTelefonos():
    marca = "motorola"
    color = "rojo"
    memoriaRam = 16
    almacenamiento = 128

    def llamar(self, mensaje):
        return print(mensaje)
    
    def escucharMusica (self):
        return print ("estas escuchando Musica")


telefono = FabricaTelefonos()
telefono.marca
telefono.color
telefono.memoriaRam
telefono.almacenamiento


telefono.llamar("alo, con dorian?")
telefono.escucharMusica()