from io import open

archivo_texto=open("archivo.txt","r")

#print(archivo_texto.read())
print(archivo_texto.read(11)) #lee hasta la posición 11 y deja el puntero ahí.

archivo_texto.seek(0) #mueve la posicion del puntero al inicio, si esto no estuviera el read de abajo no funcionaría.
#cada caracter o espacio son una posicion para el puntero.

print(archivo_texto.read()) #read lee desde donde queda el puntero.