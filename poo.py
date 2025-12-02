#no es obligatorio usar self, se puede usar cualquier otra palabra, pero
#documentación de python dice que se use self como palabra propuesta por ellos


class FabricaTelefonos():
    def __init__(this, marca, *colores, **modelos):
        this.modelos = modelos
        this.marca = marca
        this.colores = colores



telefeno = FabricaTelefonos("guawei", "negro", "verde", "amarillos", "blanco", "rojo", M2 = "IPHONE 14 PRO MAX SUPERSAYAYIN" , M1 = "IPHONE 15 PLUS PRO MAX")

print(telefeno.modelos)
print(telefeno.colores)
print(telefeno.marca)


telefeno.memoria = 512 # atributo temporal asociado al objeto creado, cuando se creé un nuevo objeto, este no aparecera

print(telefeno.memoria)
        