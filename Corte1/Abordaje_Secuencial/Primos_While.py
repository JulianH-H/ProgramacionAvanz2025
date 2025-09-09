#9 de septiembre de 2025, +1 decima adicional en el corte completo

continuar=1

while continuar==1:
    valor= int(input("Ingrese un valor: \n"))
    for i in range(1,valor+1):
        contador = 0
        for n in range(1, i+1):
            residuo = i%n
            if residuo == 0:
                contador = contador + 1


    if contador==2:
        print( i, "Es un primo\n")
    else:
        print(i, "no es un primo\n")

    print("Deseas continuar? Ingresa 1 de ser asi")

    try:
        continuar= int(input())
        if continuar != 1:
            break
    except ValueError:
        print("Por favor ingrese un número válido.")

print("Final del programa")