'''recuerden que def se usa para crear funciones y class para crear clases,
al crear una clase con el mismo nombre de una funcion, el programa entra en conflicto
no, arroja un error, por que se ejecuta lo cual es peor, porque el error lo marca, el 
conflicto no'''


class FabricaTelefono ():
    pass

print(type(FabricaTelefono))

motorola = FabricaTelefono()
iphone = FabricaTelefono()
samsung = FabricaTelefono()
alcatel = FabricaTelefono()

print(type(motorola))

def FabricaTelefono ():
    pass

print(type(FabricaTelefono))
print(type(FabricaTelefono()))