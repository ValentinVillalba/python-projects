import re

cadena="Vamos a aprender expresiones regulares en Python. Python es un lenguaje de sintaxis sencilla"

textoBuscar="Python"

print(len(re.findall(textoBuscar, cadena))) #Devuelve los strings que coinciden con la busqueda en forma de lista 
#con la funcion len devuelve la cantidad de veces que aparece

'''if re.search(textoBuscar, cadena) is not None:
	print("He encontrado el texto.")
else:
	print("No he encontrado el texto.")

textoEncontrado=re.search(textoBuscar,cadena)
print(textoEncontrado.start()) #Muestra la posicion en la que inicia la palabra encontrada
print(textoEncontrado.end()) #Lo mismo que arriba pero muestra donde termina
print(textoEncontrado.span()) #Donde comienza y donde finaliza.'''