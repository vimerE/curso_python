# Ojo: Una tupla puede es inmutable, no se le puede agregar ni quitar un valor, contiene una secuencia ordenanda de elementos
numeros1 = (1,2,3,3,4)
print(numeros1)
print(numeros1[2])
print(4 in numeros1) # Devuelve True o False si existe el índice en la tupla
for i in numeros1:
	print(i)
print(numeros1.index(3)) # Devuelve el índice del elemento
print(numeros1.count(3)) # count cuenta la cantidad de veces que hay un mismo elemento en la tupla
