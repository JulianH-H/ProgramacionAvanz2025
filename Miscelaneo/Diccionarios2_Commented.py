## Obtencion de items, Diccionarios parte 2
# Accesos

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

#Dara error en "Landmark 81", para solucionarlo se puede revisando si 
# la llave existe dentro del diccionario

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


#Para evitar devolver none en un contexto donde estemos 
# usando ids de cuentas podemos usar un if, tal que

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

##  Eliminar llaves

