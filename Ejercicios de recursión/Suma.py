def suma_arreglo(arr):
    if len(arr) == 0: 
        return 0
    else: 
        return arr[0] + suma_arreglo(arr[1:])

print(suma_arreglo([1, 2, 3, 4, 5])) 
