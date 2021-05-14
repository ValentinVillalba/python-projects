def compruebaMail(mailUsuario):

	"""
	la funcion compruebamail evalua un mail
	recibido en busca del @, si tiene un @
	es correcto, en caso contrario o si @ esta al final
	sera incorrecto.

	>>> compruebaMail('villal@hotmail.com')
	True

	MUY IMPORTANTE PONER EL ESPACIO DESPUES DE LAS FLECHAS,
	SI FALTA ESO LA PRUEBA NO FUNCIONA.

	>>> compruebaMail('elvillal@')
	False

	>>> compruebaMail('picantoide360@hot@mail.com.ar')
	False

	EL RESULTADO DE LA SIGUIENTE SE INGRESO MAL A PROPOSITO

	>>> compruebaMail('XDDDDD')
	True

	"""
	arroba=mailUsuario.count('@')
	if(arroba!=1 or mailUsuario.rfind('@')==(len(mailUsuario)-1) or mailUsuario.find('@')==0):
		return False
	else:
		return True

import doctest
doctest.testmod()