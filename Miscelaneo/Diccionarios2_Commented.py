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

#Otra manera es agregar preeventivamente un valor dummy, ejemplo con zodiac_elements

zodiac_elements["energy"] = "Not a Zodiac element"
#Donde al crear El elemento energy sin que lo usemos:

if "energy" in zodiac_elements:
  print(zodiac_elements["energy"])

#Podemos presentarle al usuario si existe o no  