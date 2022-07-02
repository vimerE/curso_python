def mayorEdad(edad):
	if edad < 18:
		return "Menor de edad"
	else:
		return "Mayor de edad"

print(mayorEdad(12))

# En Python las variables externas si se pueden acceder desde una función
x = 7
def multiplicacion(y):
	return x * y

print(multiplicacion(7))