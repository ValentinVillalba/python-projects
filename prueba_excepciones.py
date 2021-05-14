def evaluaEdad(edad):
	if edad<0:
		raise TypeError("lo rompiste man")

	if edad<20:
		return "muy joven"
	elif edad<40:
		return "joven"
	elif edad<65:
		return "maduro"
	elif edad<100:
		return "viejo"

print(evaluaEdad(-70))