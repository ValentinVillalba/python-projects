from io import open

archivo_texto=open("archivo.txt","r+") #lectura y escritura

#archivo_texto.write("Comienzo del texto.") #este texto lo va a escribir en la primera linea del texto reemplazando lo que hay ahi.
lista_texto=archivo_texto.readlines()
lista_texto[1]="Esta linea ha sido incluida desde el exterior \n"

archivo_texto.seek(0)
archivo_texto.writelines(lista_texto)
archivo_texto.close()