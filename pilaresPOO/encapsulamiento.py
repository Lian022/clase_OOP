class A():
    def __init__(self):
        self.contador = 0
    
    def incrementar(self):
        self.contador += 1

    def cuenta (self):
        return self.contador
    
class B():
    def __init__(self):
        self.__contador = 0
    
    def incrementar(self):
        self.__contador += 1

    def cuenta (self):
        return self.__contador

    
    
print("objeto 1")
a = A()
print(a.cuenta())

for i in range (1,10,1):
    a.incrementar()

print(a.cuenta())
print(a.contador)

#-------------------------

print("objeto 2")
b = B()
print(b.cuenta())

for i in range (1,10,1):
    b.incrementar()

print(b.cuenta())
print(b._B__contador)
