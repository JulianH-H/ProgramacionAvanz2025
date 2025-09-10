#
#    #Listas en Python#
#    ╩Funciones propias del lenguaje y no necesitan librerias externas 
#

mi_lista= ['Rojo', 'Azul', 'Amarillo', 'Verde', 'Violeta', 'Naranja']

#  
#    Contrario a los arreglos, las listas dentro de python se asignan 
#    como una variable mas, agregando los elementos desde 0 hasta n-1
#    entre comillas simples '' y separados por coma
#

print(mi_lista)
    #Podemos imprimir sus elementos encerrados en llaves

print(type(mi_lista))    
    #El tipo de esta variable es definido por python como lista
    # <class 'list'>

print(mi_lista[2])
    #Asi mismo podemos imprimir directamente los elementos de manera individual

print("Tamaño Lista", len(mi_lista))
    #Con la funcion len() podemos ver el tamaño de una lista definida

print(mi_lista[1:3])
    #Con la funcion : podemos visualizar los elementos por trozos
    #En este caso, tomara el elemento 1 y 3 de la lista
print(mi_lista[:3])
    #Si solo hay un digito esta funcionara desde el inicio 
    # hasta la posicion despues de los dos puntos
    # puede invertirse para ver desde la posicion hasta el final


###    Funciones propias de las listas    ###

mi_lista.append('Blanco')    
print(mi_lista)
    #Append agregara el elemento al final de la lista

mi_lista.insert(4,'Negro')
print(mi_lista)
    #Insert agregara dependiendo del indice administrado
    # permitiendo agregar el elemento, causa desplazamiento de indices

mi_lista.extend(['Marron','Gris'])
print(mi_lista)
    # Extend anexa el contenido presente en la lista 
    # administrada en la funcion directamente a la lista original


print(mi_lista.index('Azul'))
    #Index indica la posicion (desde 0 a n-1) del elemento entre parentesis
     
mi_lista.remove('Marron')
print(mi_lista)
    #Remove retira el elemento del elemento indicado

print(mi_lista.pop(8))
    #Pop elimina el elemento del indice indicado
    # Asi mismo, retorna que elemento fue eliminado


print("Orden")
mi_lista_ord = mi_lista.sort()
print(mi_lista_ord)
    #Sort ordena de menor a mayor la lista administrada
    #Asi mismo, ordena en orden alfabetico Verificar asignacion


mi_listaNum= [10,9,8,7,6,5,4,3,2,1]
print(mi_listaNum)
print("Ordenando Mi lista Numerica")

mi_listaNum.sort()
print(mi_listaNum)
    #Ejemplo con una lista numerica

mi_listaNum.sort(reverse=True)
print(mi_listaNum)
    #Si se le agrega la funcion reverse=true
    # la lista se ordenara de mayor a menor    


#    Operadores    #

mi_lista3 = mi_lista*3
print("Mi lista 3 veces: ",mi_lista3)

# ' * ' repite n veces los elementos de una lista dada

mi_listamas = mi_lista+mi_lista
print("Mi lista + mi lista: ",mi_listamas)
# ' + ' Concatena entre listas


    #Tuplas en Python#
    #Listas que no pueden ser modificadas una vez sean inicializadas


mi_tupla= tuple(mi_lista)
print("Mi tupla: " ,mi_tupla)
    # Le damos datos a forma de lista o directamente una lista
    # usando el comando tuple, se imprime como lista

print(mi_tupla[0])
print(mi_tupla[2])
    #Para imprimir un valor en especifico usamos [] al igual que en listas

print('Rojo' in mi_tupla)
    # Usando el comando in  podemos verificar si un elemento esta
    #presente en la tupla, devuelve booleano
print(mi_tupla.count('Rojo'))
    #Usando count podemos saber cuantas veces el elemento esta
    #presente en la lista de manera repetida

mi_tupla_unitaria = ('Fucsia')
print(mi_tupla_unitaria)
    #Asi se puede crear una tupla unitaria, despues de esto
    # no se puede incluir mas elementos    

mi_tupla = 'Gaspar' , 5, 8, 1999
print(mi_tupla)
    #Las tuplas se pueden empaquetar sin usar parentesis

nombre, dia, mes, año = mi_tupla
print(nombre)
print(dia)
print(mes)
print(año)
print("Nombre: ", nombre, " - Dia:", dia, " - Mes: ", mes, "- Año: ", año)
    #Al desempaquetarse se guardan los valores en orden de las variables

milista_Final =list(mi_tupla)
print(milista_Final)
    #Las tuplas asi mismo se pueden convertir en listas



#    Informacion obtenida de ThinkPython segunda edicion
#    https://www.w3schools.com/python/ref_list_index.asp
#    https://www.freecodecamp.org/espanol/news/funcion-pop-en-python/

    
