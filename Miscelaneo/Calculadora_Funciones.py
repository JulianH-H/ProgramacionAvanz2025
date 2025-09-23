def suma(a,b):
    return (a+b)

def resta(a,b):
    return (a-b)

print("Calculadora")
opcion=-1
while opcion!=0:
    print("Ingrese sus numeros")
    a=int(input())
    b=int(input())
    print("Ingrese 1 si quiere sumar, 2 si quiere restar, 0 para salir")
    opcion=int(input())

    if opcion==1:
        print("La suma es igual a",suma(a,b))

    if opcion==2:
        print("La resta es igual a", resta(a,b))   




