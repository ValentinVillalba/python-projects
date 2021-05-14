import math

def calculaRaiz(num1):
	if num1<0:
		raise ValueError ("El numero no puede ser negativo.")
	else:
		return math.sqrt(num1)
op1=(int(input("Ingresar número: ")))


try:
	print("El resultado es: ",calculaRaiz(op1))
except ValueError as NumeroNegativoError:
	print(NumeroNegativoError)

print("Programa terminado.")