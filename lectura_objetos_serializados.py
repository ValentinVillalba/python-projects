import pickle
#import serializar_objetos #si importamos esta linea el programa funciona pero al final imprime dos veces la lista (?)

ficheroApertura=open("losCoches","rb") #read binary
misCoches=pickle.load(ficheroApertura)
ficheroApertura.close()

for c in misCoches:
	print(c.estado()) #este programa no funciona porque no conoce la clase vehiculos