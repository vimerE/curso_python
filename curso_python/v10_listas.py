# Ojo: Una lista puede ser mutable, se le puede agregar y quitar un valor
nombres = ["Vimer", "Brenda", "Nadia"]
print(nombres)
print(nombres[0])
for i in nombres:
	print(i)

nombres.append("Jorge") # Agrega un valor al final de la lista
for i in nombres:
	print(i)

nombres.insert(1,"Edem") # Inserta Edem en el índice 1
for i in nombres:
	print(i)

nombres.remove("Nadia") # Remueve Nadia de la lista
for i in nombres:
	print(i)

print("Vimer" in nombres) # Devuelve Tru o False si el elemeno está en la lista

print(nombres.index("Brenda")) # Devuelve el índice del elemento

nombres[2] = "Angell" # Modifica el valor de de Brenda por Angell
for i in nombres:
	print(i)

