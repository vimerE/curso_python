for i in range(0,8,2): # inicio, hasta antes de, de 2 en 2
	print(i)

# Ciclos sobre iterables
"""
Cadenas de caracteres
Listas
Tuplas
Diccionarios
Otros
"""
miCadena = "Hola mundo"
for i in miCadena:
	print(i)

miLista = ["A","B","C","D","E"]
for i in miLista:
	print(i)

miTupla = (1,2,3,4,5)
for i in miTupla:
	print(i)

miDiccionario = {0:"V", 1:"I", 2:"M", 3:"E", 4:"R"}
for i in miDiccionario: # Forma 1
	print(miDiccionario[i])

for i in miDiccionario.values(): # Forma 2
	print(i)

for clave, valor in miDiccionario.items(): # Extrae la clave y el valor de la tupla
	print(clave,valor)