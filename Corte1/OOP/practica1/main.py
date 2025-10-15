#Adicional 2 decimas 30/09/2025
import Clase

c = float(input("Ingrese un número para obtener el cuadrado: "))
cuadr=Clase.Cuadrado(c)
sum_res=Clase.Sum_Rest()

print("El cuadrado de ",c, "Es: ", cuadr.getVal())

a = int(input("Ingrese el primer número a sumar: "))
b = int(input("Ingrese el segundo número a sumar: "))
print("La suma de" ,a, "y" ,b, "Es: ", sum_res.sum(a,b))

print("Ingrese numero a Restar")
a = int(input("Ingrese el primer número a sumar: "))
b = int(input("Ingrese el segundo número a sumar: "))
print("La resta de" ,a, "y" ,b, "Es: ", sum_res.rest(a,b))