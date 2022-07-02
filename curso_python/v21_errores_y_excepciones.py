try:
	num1 = 30
	#num2 = 0
	num3 = 3
	print(num1/num3)
except ZeroDivisionError as e:
	print(e)
else:
	print("Esto se ejecuta en lugar del except")
finally:
	print("Esto se ejecuta siempre")