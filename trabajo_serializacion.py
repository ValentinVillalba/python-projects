import pickle

lista_nombres=["Juan","Jorge","Julio","Mauricio"]

fichero_binario=open("lista_nombres","wb") #wb es write binary

pickle.dump(lista_nombres, fichero_binario)

fichero_binario.close()

del(fichero_binario)