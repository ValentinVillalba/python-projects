from modulos import funciones_matematicas

class Areas:
	"""Esta clase calcula las áreas de diferentes
	figuras geométricas"""

	def areaCuadrado (lado):
		"""Calcula el área de un cuadrado
		elevando al cuadrado el lado pasado por parámetro"""

		return "El área del cuadrado es: " + str(lado*lado)

	def areaTriangulo(base, altura):
		"""Calcula el área de un triangulo utilizando los parámetros
		base y altura"""

		#USANDO LAS TRES COMILLAS SE PUEDE MANDAR INFORMACION PARA LA FUNCION HELP, DE ESTA FORMA
		#SE DOCUMENTA FACILMENTE EL USO DE CADA FUNCION

		return "El área del triángulo es: " + str((base*altura)/2)

help(Areas) #DA TODA LA INFORMACION DE LA CLASE Y LAS FUNCIONES
print("A continuación la información del modulo:\n")
help(funciones_matematicas)