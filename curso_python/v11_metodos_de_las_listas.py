numeros1 = [1,2,3,3,3,4,5]
numeros2 = [6,7,7,7,7,8,9,10]
print(numeros1.count(3)) # Cuenta cuantas veces hay un mismo valor en la lista
numeros1.extend(numeros2) # Extiende la lista uno con la lista 2
print(numeros1)
numeros1.pop(5) # Elimina el valor del índice indicado, por defecto borra el último elemento
print(numeros1)
numeros1.reverse() # Invierte los elementos de una lista de atrás para adelante
print(numeros1)
numeros1.sort() # Ordena los elementos de la lista de menos a mayor
print(numeros1)