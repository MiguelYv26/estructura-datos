x=int(input("Escriba el primer numero: "))
y=int(input("Escriba el segundo numero: "))
operacion=input("Escriba la operacion: ")
if operacion=="+":
    print("La suma es: ",x+y)
elif operacion=="-":
    print("La resta es: ",x-y)
elif operacion=="*":
    print("La multiplicacion es: ",x*y)
elif operacion=="/":
    print("La division es: ",x/y)
else:
    print("La operacion no es valida")


2