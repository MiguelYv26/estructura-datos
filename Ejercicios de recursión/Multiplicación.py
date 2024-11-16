def multiplicar(a, b):
    if b == 0:  
        return 0
    elif b > 0: 
        return a + multiplicar(a, b - 1)
    elif b < 0: 
        return -multiplicar(a, -b)

print(multiplicar(3, 4)) 
