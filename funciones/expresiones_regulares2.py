import re

listaNombres=[
	'Ana Gomez',
	'María Martín',
	'Sandra Lopez',
	'Santiago Martín',
	'Sandra Fernandez',
	'Sandra Rodriguez',
	'Sandra Gomez',]

#USO DE METCARACTERES (SIMBOLOS EN EL STRING)
for i in listaNombres:
	if re.findall('^Sandra', i): #REGULAR EXPRESSION FIND ALL
		print(i)

print("--------------")
for i in listaNombres:
	if re.findall('Martín$', i):
		print(i)

print("--------------")
listaRango=[
	'Ma1',
	'Se1',
	'Ma2',
	'MaA',
	'Va1',
	'Va2',
	'MaB',
	'Ma3']

for i in listaRango:
	if re.findall('Ma[0-3A-B]', i): #BUSCA EN RANGO 0 - 3 Y RANGO A - B
		print(i)