###### Diccionarios en Python
#Tipo de dato presente en python, similares a la lista pero contienen indices 
# (llamados claves) adjuntos a los valores que les demos al diccionario

#Para Crear
sensors =  {"living room": 21, "kitchen": 23, "bedroom": 20, "pantry": 22}
num_cameras = {"backyard": 6,  "garage": 2, "driveway": 1}

#asignamos usando  {"Valor":indice, } para cada item del diccionario


#Para imprimir el diccionario llamamos su nombre:
print(sensors)
print(num_cameras)
print("")

#Si deseamos crear un diccionario vacio usamos:

diccionario_vacio = dict()
diccionario_vacio2 = {}
print("Diccionario Vacio 1 :")
print(diccionario_vacio)
print("Diccionario Vacio 2 :")
print(diccionario_vacio2)
print("")


##Los diccionarios no pueden indexar listas en su interior:
# Tal que:
    # powers = {[1, 2, 4, 8, 16]: 2, [1, 3, 9, 27, 81]: 3}
    # # print(powers)
# Retornara error al no poder hashear el tipo listam, pero el diccionario:
children = {"von Trapp": ["Johannes", "Rosmarie", "Eleonore"] , "Corleone": ["Sonny", "Fredo", "Michael"]}
print(children)
print("")

#Funcionara, esto es debido a que la lista numerica puede mutar, 
# pero la lista con strings es inmutable, puesto que para crear
# un diccionario debe ser inmutable
# para poder crear un diccionario con numeros, usamos una tupla, tal que:

powers = {(1, 2, 4, 8, 16): 2, (1, 3, 9, 27, 81): 3}
print(powers)
print("")


#Los diccionarios pueden recibir nuevos items, asi como se evidencia en el siguiente ejemplo:

menu = {"oatmeal": 3, "avocado toast": 6, "carrot juice": 5, "blueberry muffin": 2}
print("Antes: ", menu)
menu["cheesecake"] = 8
print("")
print("Despues", menu)
print("")

#Al asignar un indice a un elemento no existentee podemos crear un item

#Asi mismo, se debe tener cuidado al asignar diccionarios, si se quiere añadir
# un nuevo elemento no se utiliza el igual, pue esto causara lo siguiente:

animals_in_zoo = {"dinosaurs": 0,}
print(animals_in_zoo)
animals_in_zoo = {"reptiles": 0}
print(animals_in_zoo)
animals_in_zoo = {"horses": 2}
print(animals_in_zoo)
print("")
#Solo Horses quedara, pues fue el ultimo en ser asignado al objeto "animals_in_zoo"


#Para agregar items correctamente debemos usar la funcion .update
print("Antes", sensors)

sensors.update({"guest room": 25, "patio": 34})
print("Despues", sensors)
print("")

#Donde podemos añadir correctamente varios items a la vez, otro ejemplo
user_ids = {"teraCoder": 9018293, "proProgrammer": 119238}
print(user_ids)
user_ids.update({"theLooper": 138475, "stringQueen": 85739})
print(user_ids)
print("")


#Sobreescribir valores
#Podemos agregar un item usando la sintaxis 
#  objeto["string"]=id
#Con el cual podemos sobreescribir el indice de un item, ejemplo con el menu

print("Antes: ", menu)
menu["oatmeal"]=5
print("Despues", menu)
print("")

#Evidencie como el valor de oatmeal cambio de 3 a 5
#Otro ejemplo presente

oscar_winners = {"Best Picture": "La La Land", "Best Actor": "Casey Affleck", "Best Actress": "Emma Stone", "Animated Feature": "Zootopia"}
print("Antes", oscar_winners)

oscar_winners.update({"Supporting Actress": "Viola Davis"})
print("Despues 1", oscar_winners)

oscar_winners["Best Picture"] = "Moonlight"
print("Despues 2", oscar_winners)
print("")

#En este ejemplo el item de Supporting Actress fue añadido,
#Best picture fue cambiado por Moonlight



###  Combinacion de Diccionarios
#A partir de dos tuplas o listas existentes podemos crear un diccionario
#El siguiente ejemplo presenta una lista de estudiantes y alturas

names = ['Jenny', 'Alexus', 'Sam', 'Grace']
heights = [61, 70, 67, 64]

#Para combinarlos utilizamos la siguiente sintaxis

zipEstudiantes= zip(names, heights)

#print("Combinacion Estudiantes", zipEstudiantes)
#Imprimir esto nos dara la posicion del objeto Zip dentro de la memoria, 
# para unirlos ello debemos realizar el siguiente for:

Estudiantes = {key:value for key, value in zip(names, heights)}
print(Estudiantes)
print("")
#Esto creara el diccionario Estudiantes, otro ejemplo es:

drinks = ["espresso", "chai", "decaf", "drip"]      #Creamos la primer lista 
caffeine = [64, 40, 0, 120]                         #Creamos la segunda lista (identificadores)
zipped_drinks = zip(drinks, caffeine)                   #Asignamos
drinks_to_caffeine = {key:value for key, value in zipped_drinks} #Fusionamos Listas
print(drinks_to_caffeine) 
print("")

#Un ejemplo que integra todo lo aprendido es el siguiente:

songs = ["Like a Rolling Stone", "Satisfaction", "Imagine", "What's Going On", "Respect", "Good Vibrations"]
playcounts = [78, 29, 44, 21, 89, 5]
plays = {key:value for key, value in zip(songs, playcounts)}
print(plays)
print("")
plays.update({"Purple Haze": 1})
plays.update({"Respect": 94})
print("After: ", plays)
print("")
library = {"The Best Songs": plays, "Sunday Feelings": {}}
print(library)

