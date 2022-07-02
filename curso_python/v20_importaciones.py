# Primera forma
# import <módulo>
"""
import math
valor1 = math.pow(9,2)
print(int(valor1))

valor2 = math.pi
print(valor2)
"""

# Segunda forma 
#import <módulo> as <nombre_alternativo>
"""
import math as matematica
valor3 = matematica.pow(5,2)
print(int(valor3))

valor4 = matematica.pi
print(valor4)
"""

# Tercera forma
# from <módulo> import <elemento>
from math import pi, pow
valor5 = pi
print(valor5)
valor6 = pow(3,2)
print(int(valor6))