import sqlite3

miConexion=sqlite3.connect("gestionProductos")

miCursor=miConexion.cursor()

#DE ESTA MANERA SE HACE UN UPDATE:

miCursor.execute("UPDATE PRODUCTOS SET PRECIO=35 WHERE NOMBRE_ARTICULO='pelota'")

miConexion.commit()

miConexion.close()