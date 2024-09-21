class Animal:
    def __init__(self, edad, tipo):
        self.edad = edad
        self.tipo = tipo

class Node:
    def __init__(self, animal):
        self.animal = animal
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.primero = None

    def agregar(self, animal):
        if not self.primero:
            self.primero = Node(animal)
            return
        
        actual = self.primero
        while actual.siguiente:
            if actual.animal.tipo == animal.tipo and actual.animal.edad == animal.edad:
                print(f"Ya existe un {animal.tipo} de {animal.edad} años")
                return
            actual = actual.siguiente
        
        if actual.animal.tipo == animal.tipo and actual.animal.edad == animal.edad:
            print(f"Ya existe un {animal.tipo} de {animal.edad} años")
        else:
            actual.siguiente = Node(animal)

    def mostrar_recursivo(self, nodo=None):
        if nodo is None:
            nodo = self.primero
        if nodo:
            print(f"{nodo.animal.tipo} - {nodo.animal.edad} años")
            self.mostrar_recursivo(nodo.siguiente)

    def mostrar_bucle(self):
        actual = self.primero
        while actual:
            print(f"{actual.animal.tipo} - {actual.animal.edad} años")
            actual = actual.siguiente

zoologico = ListaEnlazada()

zoologico.agregar(Animal(5, "Leon"))
zoologico.agregar(Animal(10, "Elefante"))
zoologico.agregar(Animal(2, "Loro"))
zoologico.agregar(Animal(5, "Leon"))

print("Animales (modo recursivo):")
zoologico.mostrar_recursivo()

print("Animales (modo bucle):")
zoologico.mostrar_bucle()