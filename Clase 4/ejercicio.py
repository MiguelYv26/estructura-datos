def calculo_factorial (numero:int) -> str:
    resultado: int
    if numero < 0:
        return "No se puede valores negativos"
    elif numero ==0:
        return 1
    for n in range(1, numero):
        resultado = resultado * n
        return resultado
    OP1
    print