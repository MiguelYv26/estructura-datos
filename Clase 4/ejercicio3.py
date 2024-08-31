def celcius_fahrenheit(temperaturaC):
    return (temperaturaC * 9/5 + 32)

temperaturaC = float(input("Ingrese la Temperatura en celcius: " ))
resultado = celcius_fahrenheit(temperaturaC)
print("Su resultado es: ", resultado)

