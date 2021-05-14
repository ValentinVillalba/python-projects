from io import open

archivo_texto=open("archivo.txt","w") #abre el archivo en modo escritura (write)
frase="ola k ase kuentame lo k ase"

archivo_texto.write(frase) #escribe en el archivo lo que hay en la variable frase
archivo_texto.close() #cierra el espacio en la memoria que se habia creado para abrir el archivo.