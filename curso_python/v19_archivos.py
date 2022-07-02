"""
r (leer)
w (escribir)
a (añadir al final)
w+ (leer y escribir)
"""


with open("v19_archivos/texto.txt", "r") as archivo:
	for linea in archivo:
		print(linea)
archivo.close()


"""
notas = {
	"Vimer":20,
	"Nadiana":18,
	"Brenda":15,
	"Michael":15
}
with open("v19_archivos/texto.txt", "w") as archivo:
	for nombre, nota in notas.items():
		archivo.write(nombre + ":" + str(nota) + "\n")
archivo.close()
"""

"""
agregarNotas = {
	"Angel":18,
	"Bryan":13,
	"Joselim":12
}
with open("v19_archivos/texto.txt","a") as archivo:
	for nombre, nota in agregarNotas.items():
		archivo.write(nombre + ":" + str(nota) + "\n")
archivo.close()
"""