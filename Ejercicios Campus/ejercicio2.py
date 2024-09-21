import datetime

class Tarea:
    def __init__(self, descripcion, prioridad, fecha_vencimiento):
        self.descripcion = descripcion
        self.prioridad = prioridad
        self.fecha_vencimiento = fecha_vencimiento

class Nodo:
    def __init__(self, tarea):
        self.tarea = tarea
        self.siguiente = None

class ListaTareas:
    def __init__(self):
        self.primero = None

    def agregar_tarea(self, tarea):
        nuevo_nodo = Nodo(tarea)
        if not self.primero:
            self.primero = nuevo_nodo
        else:
            actual = self.primero
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo

    def eliminar_tarea(self, descripcion):
        if not self.primero:
            return
        if self.primero.tarea.descripcion == descripcion:
            self.primero = self.primero.siguiente
            return
        actual = self.primero
        while actual.siguiente:
            if actual.siguiente.tarea.descripcion == descripcion:
                actual.siguiente = actual.siguiente.siguiente
                return
            actual = actual.siguiente

    def mostrar_tareas(self):
        tareas = []
        actual = self.primero
        while actual:
            tareas.append(actual.tarea)
            actual = actual.siguiente
        tareas.sort(key=lambda x: (x.prioridad, x.fecha_vencimiento))
        for tarea in tareas:
            print(f"Descripción: {tarea.descripcion}, Prioridad: {tarea.prioridad}, Fecha: {tarea.fecha_vencimiento}")

    def buscar_tarea(self, descripcion):
        actual = self.primero
        while actual:
            if actual.tarea.descripcion == descripcion:
                return actual.tarea
            actual = actual.siguiente
        return None

    def marcar_completada(self, descripcion):
        self.eliminar_tarea(descripcion)

# Ejemplo de uso
lista_tareas = ListaTareas()

while True:
    print("\n1. Agregar tarea")
    print("2. Eliminar tarea")
    print("3. Mostrar tareas")
    print("4. Buscar tarea")
    print("5. Marcar tarea como completada")
    print("6. Salir")
    opcion = input("Elige una opción: ")

    if opcion == "1":
        descripcion = input("Descripción de la tarea: ")
        prioridad = int(input("Prioridad (1-3): "))
        fecha = input("Fecha de vencimiento (YYYY-MM-DD): ")
        fecha_vencimiento = datetime.datetime.strptime(fecha, "%Y-%m-%d").date()
        tarea = Tarea(descripcion, prioridad, fecha_vencimiento)
        lista_tareas.agregar_tarea(tarea)
    elif opcion == "2":
        descripcion = input("Descripción de la tarea a eliminar: ")
        lista_tareas.eliminar_tarea(descripcion)
    elif opcion == "3":
        lista_tareas.mostrar_tareas()
    elif opcion == "4":
        descripcion = input("Descripción de la tarea a buscar: ")
        tarea = lista_tareas.buscar_tarea(descripcion)
        if tarea:
            print(f"Tarea encontrada: {tarea.descripcion}, Prioridad: {tarea.prioridad}, Fecha: {tarea.fecha_vencimiento}")
        else:
            print("Tarea no encontrada")
    elif opcion == "5":
        descripcion = input("Descripción de la tarea completada: ")
        lista_tareas.marcar_completada(descripcion)
    elif opcion == "6":
        break
    else:
        print("Opción no válida")