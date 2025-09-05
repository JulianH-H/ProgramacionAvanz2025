import math
print("Ingrese sus grados (sexagesimales)")

grad=float(input())
rad=grad/180.0*math.pi
seno= math.sin(rad)
print("El seno de: ", grad, " radianes (En grados cel es: " ,seno )

// math.radians es una funcion que se encarga de modificar el valor sexagesimal directo a radianes, tal que

result= math.sin(math.radians(grad))
result
