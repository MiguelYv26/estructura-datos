class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class ListaEnlazada:

    def __init__(self):
        self.cabeza = None

    def es_vacio(self):
        return self.cabeza is None

    def agregar_nodo(self, dato):
      nodo = Node(dato)
      if self.es_vacio():
          self.cabeza = nodo
      else:
          nodo_actual = self.cabeza
          while nodo_actual.next is not None:
              nodo_actual = nodo_actual.next
          nodo_actual.next = nodo

    def imprimir(self):
      nodo_actual = self.cabeza
      while nodo_actual is not None:
          print(nodo_actual.data)
          nodo_actual = nodo_actual.next

    def eliminar(self, dato):
      nodo_actual = self.cabeza
      if nodo_actual.data == dato:
          self.cabeza = nodo_actual.next
          return
      while nodo_actual.next is not None:
          if nodo_actual.next.data == dato:
              nodo_actual.next = nodo_actual.next.next
              return
          nodo_actual = nodo_actual.next

    def buscar(self, dato):
        nodo_actual = self.cabeza
        indice = 0
        while nodo_actual is not None:
            if nodo_actual.data ==dato:
                return indice
            nodo_actual = nodo_actual.next
            indice +=1
        return f"El dato {dato} no se encuentra en la lista."

lista = ListaEnlazada()
print("Agregamos datos al nodo")
lista.agregar_nodo(1)
lista.agregar_nodo(2)
lista.agregar_nodo(3)

print("Imprimimos los datos")
lista.imprimir()

print("Buscamos el dato 2")
print(lista.buscar(2))
print("Buscamos el dato 4")
print(lista.buscar(4))
