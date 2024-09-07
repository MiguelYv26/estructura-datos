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

