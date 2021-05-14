import sqlite3

miConexion=sqlite3.connect("gestionProductos")

miCursor=miConexion.cursor()

#DE ESTA MANERA SE HACE UN READ:

miCursor.execute("SELECT * FROM PRODUCTOS WHERE SECCION='confección'")
#LAS INSTRUCCIONES SON SENSIBLES A MAYUSCULAS Y MINUSCULAS (CASE SENSITIVE)

productos=miCursor.fetchall()
print(productos)

miConexion.commit()

miConexion.close()