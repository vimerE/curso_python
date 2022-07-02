# Ojo: Un diccionario puede ser mutable, se le puede agregar y quitar un valor
# Los diccionarios tienen clave y valor
# Las claves deben ser únicas e inmutables
diccionario = {"A":1, "B":2, "C":3, "D":4}
print(diccionario["C"])
print(diccionario.get("B"))

diccionario["E"] = 5 # Agrega el valor al final del diccionario
print(diccionario)

diccionario["B"] = 33 # Actualiza el valor del índice B
print(diccionario)

del diccionario["D"] # Elimina la clave y el valor del índice asignado
print(diccionario)

print("B" in diccionario) # Devuelve True o False si existe el índice en el diccionario


