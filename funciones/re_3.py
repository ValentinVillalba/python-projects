import re

nombre1="Sandra Lopez"
nombre2="Antonio Gomez"
nombre3="sandra Gomez"

if re.match("Sandra", nombre3, re.IGNORECASE):
	print("Se encontro el nombre.")
else:
	print("No se encontro.")