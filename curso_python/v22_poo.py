class CuentaBancaria:
	# Atributos
	numCuenta = ""
	nombreTirular = ""
	balance = 0.0
	# Método constructor
	def __init__(self, numCuenta, nombreTirular, balance):
		self.numCuenta = numCuenta
		self.nombreTirular = nombreTirular
		self.balance = balance

	# Métodos normales
	def generarBalance(self):
		 return self.balance

	def depositar(self, monto):
		if monto > 0:
			self.balance += monto
		else:
			return self.balance

miCuenta = CuentaBancaria("138-598-333", "Vimer Edem,", 15600)
print(miCuenta.numCuenta)
print(miCuenta.nombreTirular)
print(miCuenta.balance)
print(miCuenta.generarBalance())
miCuenta.depositar(500)
print(miCuenta.generarBalance())

