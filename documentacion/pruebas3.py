import math

def raizCuadrada(listaNumeros):

	"""
	La funcion devuelve una lista con la
	raiz cuadrada de los elementos numericos
	pasados por parametro en otra lista.

	Para anidar expresiones en las pruebas
	se hace uso de los tres puntos
	como en el siguiente caso:

	>>> lista=[]
	>>> for i in [4, 9, 16]:
	...		lista.append(i)
	>>> raizCuadrada(lista)
	[2.0, 3.0, 4.0]

	En la siguiente prueba se especifican la primera
	y la ultima linea del error, y se omite
	lo que esta en medio utilizando los tres puntos indentados.

	>>> lista=[]
	>>> for i in [4, -9, 16]:
	...		lista.append(i)
	>>> raizCuadrada(lista)
	Traceback (most recent call last):
		...
	ValueError: math domain error

	"""
	return [math.sqrt(n) for n in listaNumeros]

print (raizCuadrada([9, 16, 25, 36]))

import doctest
doctest.testmod()