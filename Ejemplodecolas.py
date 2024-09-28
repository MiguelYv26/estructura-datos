class pilas:
    def __init__(self):
        self.items = []
 
    def isEmpty(self):
        return self.items == []
 
    def push(self, item):
        self.items.append(item)
 
    def pop(self):
        return self.items.pop()
 
    def top(self):
        return self.items[len(self.items)-1]
 
    def size(self):
        return len(self.items)
    
mi_pila = pilas()

mi_pila.push(10)
mi_pila.push(20)
mi_pila.push(30)
mi_pila.push(40)

print("Pila actual:", mi_pila.items)
print("Elemento en la cima:", mi_pila.top())
print("Elemento borrado:", mi_pila.pop())
print("Pila despues de pop:", mi_pila.items)
print("¿Se encuentra vacia la pila?", mi_pila.isEmpty())
print("El tamaño de la pila:", mi_pila.size)
    
   


