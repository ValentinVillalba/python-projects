def areaTriangulo(base, altura):
		"""
		Calcula el área de un triangulo utilizando los parámetros
		base y altura

		CON LO SIGUIENTE SE PUEDEN HACER PRUEBAS,
		LO QUE SE ESPECIFICA ES QUE SI EN LA FUNCION SE INGRESAN 3 Y 6, DEBE DAR 9.0
		SI SE CAMBIA EL 9.0 POR OTRA COSA, SE ESPECIFICARA DONDE ESTÁ EL ERROR AL REALIZAR LA PRUEBA.

		LO CAMBIE A 8.0 PARA VER EL ERROR.

		>>> areaTriangulo(3,6)
		8.0

		LAS COMILLAS DOBLES SE DIFERENCIAN DE LAS SIMPLES

		>>> areaTriangulo(4,8)
		"El resultado es: 16.0"

		"""
		return "El resultado es: " + str((base*altura)/2)

import doctest
doctest.testmod()