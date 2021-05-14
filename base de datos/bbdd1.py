import sqlite3

miConexion=sqlite3.connect("primeraBase")

miCursor=miConexion.cursor()
#miCursor.execute("CREATE TABLE PRODUCTOS (NOMBRE_ARTICULO VARCHAR(50), PRECIO INTEGER, SECCION VARCHAR(20))") 
#LAS LINEAS SE COMENTA UNA VEZ UTILIZADAS PARA NO CREAR OTRA TABLA
#miCursor.execute("INSERT INTO PRODUCTOS VALUES('BALÓN', 15, 'DEPORTES')")

#variosProductos=[
#	("Camiseta",10,"Deportes"),
#	("Jarrón",90,"Cerámica"),
#	("Camión",20,"Juguetería")
#]

#miCursor.executemany("INSERT INTO PRODUCTOS VALUES (?,?,?)", variosProductos)

miCursor.execute("SELECT * FROM PRODUCTOS")

variosProductos=miCursor.fetchall()

for producto in variosProductos:
	print("Nombre Artículo: ", producto[0], "Sección: ", producto[2])

miConexion.commit()

miConexion.close()