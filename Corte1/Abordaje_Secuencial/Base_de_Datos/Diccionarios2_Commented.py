#Obtencion de items, Diccionarios parte 2
#Accesos

#Puedes obtener los valores de un item en el diccionario conociendo su llave

building_heights = {"Burj Khalifa": 828, "Shanghai Tower": 632, "Abraj Al Bait": 601, "Ping An": 599, "Lotte World Tower": 554.5, "One World Trade": 541.3}
print(building_heights)
print("")
print(building_heights["Burj Khalifa"]) #Prints 828
print("")
print(building_heights["Ping An"]) #Prints 599
print("")
print("")

#Asi mismo podemos ver el valor conociendo su llave, tal que

zodiac_elements = {"water": ["Cancer", "Scorpio", "Pisces"], "fire": ["Aries", "Leo", "Sagittarius"], "earth": ["Taurus", "Virgo", "Capricorn"], "air":["Gemini", "Libra", "Aquarius"]}
print(zodiac_elements)
print("")
print(zodiac_elements["earth"]) #Imprimira ['Taurus', 'Virgo', 'Capricorn']
print("")
print(zodiac_elements["fire"]) #Imprimira ['Aries', 'Leo', 'Sagittarius']
print("")
print("")

#Si la llave es invalida dara error al no encontrarlo en la lista, ejemplo
    #print(building_heights["Landmark 81"])

# #Dara error en "Landmark 81", para solucionarlo se puede revisando si 
#la llave existe dentro del diccionario

key_to_check = "Landmark 81" #Primero asignamos la llave de busqueda a otro objeto

if key_to_check in building_heights:
  print(building_heights["Landmark 81"])
  #Y al usar este if nos presentara con un valor booleano si esta o no
print("")
#Otra manera es agregar preeventivamente un valor dummy, ejemplo con zodiac_elements

zodiac_elements["energy"] = "Not a Zodiac element"
#Donde al crear El elemento energy sin que lo usemos:

if "energy" in zodiac_elements:
  print(zodiac_elements["energy"])
print("")
#Podemos presentarle al usuario si existe o no  
#Asi mismo podemos llamar con la llave usando .get


building_heights.get("Shanghai Tower") #Esta linea retornara: 632:
building_heights.get("My House") #Esta linea retornara: None
print("")


# #Para evitar devolver none en un contexto donde estemos 
# #usando ids de cuentas podemos usar un if, tal que

user_ids = {"teraCoder": 100019, "pythonGuy": 182921, "samTheJavaMaam": 123112, "lyleLoop": 102931, "keysmithKeith": 129384}
user_ids.get("teraCoder")
#En este caso verificamos que teraCoder Exista

if user_ids.get("teraCoder") == None:
   tc_id = 1000
   #De no estarlo, imprimiriamos 1000 en vez de none
else: 
   tc_id = user_ids.get("teraCoder")
    #De lo contrario, imprimimos su user
print(tc_id)

if user_ids.get("superStackSmash") == None:
     stack_id = 100000
    #Lo mismo para este caso, donde imprimiremos 100000
print(stack_id)

#  ##Eliminar llaves
##Al igual que con las listas, podemos usar la funcion .pop para eliminar items 
##de un diccionario sabiendo el valor de la llave a eliminar
 

raffle = {223842: "Teddy Bear", 872921: "Concert Tickets", 320291: "Gift Basket", 412123: "Necklace", 298787: "Pasta Maker"}
print(raffle.pop(320291, "No Prize"))
#Imprime "Gift Basket"
print(raffle)
#Imprime {223842: "Teddy Bear", 872921: "Concert Tickets", 412123: "Necklace", 298787: "Pasta Maker"}
print(raffle.pop(100000, "No Prize"))
#Imprime "No Prize"
print(raffle)
#Imprime {223842: "Teddy Bear", 872921: "Concert Tickets", 412123: "Necklace", 298787: "Pasta Maker"}
print(raffle.pop(872921, "No Prize"))
#Imprime "Concert Tickets"
print(raffle)
#Imprime {223842: "Teddy Bear", 412123: "Necklace", 298787: "Pasta Maker"}

#Este ejemplo nos muestra una lista de objetos (posiblemente de un juego)
available_items = {"health potion": 10, "cake of the cure": 5, "green elixir": 20, "strength sandwich": 25, "stamina grains": 15, "power stew": 30}
health_points = 20

health_points += available_items.pop("stamina grains", 0)
health_points += available_items.pop("power stew", 0)
health_points += available_items.pop("mystic bread", 0)
#Al usar estos comandos eliminamos la llave, agregando el valor a health_points
print(available_items)
print(health_points)


##Obtener todas las llaves

#Si usamos el comando print(list()) podemos imprimir toda una lista facilmente
test_scores = {"Grace":[80, 72, 90], "Jeffrey":[88, 68, 81], "Sylvia":[80, 82, 84], "Pedro":[98, 96, 95], "Martin":[78, 80, 78], "Dina":[64, 60, 75]}
print(list(test_scores))
#Esto imprime la lista: ["Grace", "Jeffrey", "Sylvia", "Pedro", "Martin", "Dina"]

for student in test_scores.keys():
 print(student)
#Otra manera es usando el for, esto imprime la misma lista anteriormente

user_ids = {"teraCoder": 100019, "pythonGuy": 182921, "samTheJavaMaam": 123112, "lyleLoop": 102931, "keysmithKeith": 129384}
num_exercises = {"functions": 10, "syntax": 13, "control flow": 15, "loops": 22, "lists": 19, "classes": 18, "dictionaries": 18}
users = user_ids.keys()
lessons = num_exercises.keys()
print(users)
print(lessons)
#Este ejemplo crea las dos, Guardando las llaves (los username y las lessons) e imprimiendolas
#.keys() crea un objeto tipo dict_keys el cual funciona como lista


##Obtener valores
test_scores = {"Grace":[80, 72, 90], "Jeffrey":[88, 68, 81], "Sylvia":[80, 82, 84], "Pedro":[98, 96, 95], "Martin":[78, 80, 78], "Dina":[64, 60, 75]}
for score_list in test_scores.values():
 print(score_list)
#Este ejemplo imprime los valores (Inscritos entre [])
#Y los devuelve

num_exercises = {"functions": 10, "syntax": 13, "control flow": 15, "loops": 22, "lists": 19, "classes": 18, "dictionaries": 18}
total_exercises = 0

for exercises in num_exercises.values():
  total_exercises += exercises
print(total_exercises)

#En cambio en este for se agregan todos los valores en el diccionario para 
#Imprimir un solo valor de los valores totales


##Obtener todos los items
#Con el comando .items() podemos obtener el valor y llave de cada item del diccionario
biggest_brands = {"Apple": 184, "Google": 141.7, "Microsoft": 80, "Coca-Cola": 69.7, "Amazon": 64.8}
for company, value in biggest_brands.items():
 print(company + " has a value of " + str(value) + " billion dollars. ")
#En este ejemplo el for toma los valores en cada item (llave y valor)
#imprimiendo la llave y su valor individualmente al desempaquetarlos
#Asi mismo, el valor de value es convertido a string


pct_women_in_occupation = {"CEO": 28, "Engineering Manager": 9, "Pharmacist": 58, "Physician": 40, "Lawyer": 37, "Aerospace Engineer": 9}
for occupation, percentage in pct_women_in_occupation.items():
  print("Women make up " + str(percentage) + " percent of " + occupation + "s.") 
  #Este ejemplo estadistico realiza lo mismo, desempaquetando la llave en occupation y su valor en percentage, imprimiendolas