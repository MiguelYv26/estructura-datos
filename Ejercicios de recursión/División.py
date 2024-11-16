def dividir(a, b):
    if b == 0:
        raise ValueError("La división por cero no está definida")
    if abs(a) < abs(b):  
        return 0
    else:  
        if (a > 0 and b > 0) or (a < 0 and b < 0):
            return 1 + dividir(a - b, b)
        else:
            return -1 + dividir(a + b, b) 

print(dividir(10, 2))
print(dividir(7, -3))  
