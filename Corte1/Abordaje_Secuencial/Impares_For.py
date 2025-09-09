#9 de septiembre de 2025, +1 decima adicional en el corte completo


#ingresar por teclado un numero cualquiera para comprobar si es par o impar, fin
#todo eso en el while true para que no salga del codigo

while (True):
    num= int(input("Ingrese un numero \n"))
    residuo= num % 2
    if residuo==0:
        print(num," es par")
    else:
        print(num," es impar")    
 
