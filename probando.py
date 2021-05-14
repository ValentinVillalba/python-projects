from funciones_probando import *
b=int(input("ingrese el primer numero para el calculo: "))
c=int(input("ingrese el segundo numero para el calculo: "))
d=int(input("ingrese el tercer numero para el calculo: "))
print("se sumaron el primer y segundo numero, se restó el tercero")

a=funcion_calculo(b,c,d)
print("el resultado de la funcion de calculo es:", a)

lista=[14,21,26,2,49]
for i in lista:
	if i > a:
		print("se encontró un mayor en la lista y es:", i)
	else:
		print("saquenme de latinoamerica")