import sqlite3

miConexion=sqlite3.connect("gestionProductos")

miCursor=miConexion.cursor()

#DE ESTA MANERA SE HACE UN DELETE:

miCursor.execute("DELETE FROM PRODUCTOS WHERE ID=5")
#SIEMPRE INCLUIR WHERE EN EL DELETE PORQUE SI NO SE BORRA TODO

miConexion.commit()

miConexion.close()
