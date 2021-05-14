from io import open

archivo_texto=open("archivo.txt","r")

lineas_texto=archivo_texto.readlines() #guarda la informacion dentro de una lista (manipulable)

#texto=archivo_texto.read() #lee lo que tenga el archivo
archivo_texto.close()

print(lineas_texto[0]) #se puede acceder con indice, lineas_texto es una lista