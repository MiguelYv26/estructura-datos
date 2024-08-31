def operaciones_matematicas(numero1, numero2, operaciones):
    if operaciones == 'suma':
        return numero1 + numero2
    elif operaciones == 'resta':
        return numero1 - numero2
    elif operaciones == 'division':
        if numero2 == 0:
            return "no se puede operar"
        else:
            return numero1/numero2
    elif operaciones == 'multiplicacion':
        return numero1 * numero2

numero1 = float(input("Ingrese un numero: "))
numero2 = float(input("Ingrese un numero: "))
operaciones = input("Que operación desea realizar: ")


resultado = operaciones_matematicas(numero1, numero2, operaciones)
print("Su resultado es: " , resultado)

