class Vehiculo:
    def __init__ (self, marca:str, combustible:str):
         self.marca = marca
         self.combustibe = combustible
    def encender (self):
         pass
    def arrancar (self):
         pass 
    def __str__(self):
         return f"el vehiculo es de marca {self.marca} utiliza como combustible {self.combustibe}"

carro = Vehiculo ("Toyota", "corriente")
print(carro)    
print(type(carro))

class Moto (Vehiculo):
     def __init__(self, marca: str, combustible: str):
          super().__init__(marca, combustible)
class Carro (Vehiculo):
     pass
motociclista = Moto ("Honda", "corriente")
mi_carro = Carro ("Mazda", "extra")
print(motociclista)
print(carro)