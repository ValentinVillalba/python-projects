def funcion_decoradora(funcion_parametro):
	def funcion_interior(*args, **kwargs):
		#Acciones adicionales que decoran
		print("Vamos a realizar un cálculo: ")

		funcion_parametro(*args, **kwargs) #el *args perminte usar los argumentos que sean necesarios MUY UTIL

		#Acciones adicionales que decoran
		print("Hemos terminado el cálculo.\n")

	return funcion_interior

@funcion_decoradora #Con esto se le dice al programa que cuando se use la funcion suma, ademas debe tener acciones adicionales.
def suma(num1, num2, num3):
	print(num1+num2+num3)

@funcion_decoradora #RECORDAR LA NOMENCLATURA, USAR @
def resta(num1, num2):
	print(num1-num2)
	
@funcion_decoradora
def potencia(base, exponente):
	print(pow(base, exponente))

suma(7,5,8)
resta(12,10)
potencia(base=5, exponente=3)