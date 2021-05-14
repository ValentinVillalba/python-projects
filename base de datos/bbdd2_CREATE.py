import sqlite3

miConexion=sqlite3.connect("gestionProductos")

miCursor=miConexion.cursor()

miCursor.execute(''' 
	CREATE TABLE PRODUCTOS(
	ID INTEGER PRIMARY KEY AUTOINCREMENT,
	NOMBRE_ARTICULO VARCHAR(50) UNIQUE,
	PRECIO INTEGER,
	SECCION VARCHAR(20))
	''')
#PRIMARY KEY CREA UN CAMPO CLAVE Y AUTOINCREMENT GESTIONA AUTOMATICAMENTE LA ID
#UNIQUE IMPIDE QUE SE REPITA INFORMACION EN ESE CAMPO

productos=[
	("pelota", 20, "juguetería"),
	("pantalón", 15, "confección"),
	("destornillador", 25, "ferretería"),
	("jarrón", 45, "cerámica"),
	("pantalones", 35, "confección")
]

miCursor.executemany("INSERT INTO PRODUCTOS VALUES (NULL,?,?,?)", productos) 
#CON NULL SE GESTIONA AUTOMATICAMENTE EL CAMPO CLAVE

#miCursor.execute("INSERT INTO PRODUCTOS VALUES ('AR05','tren',15,'juguetería')") 
#PERMITIO AGREGARLO PORQUE NO EXISTIA AR05

#CRUD:
#CREATE
#READ
#UPDATE
#DELETE

miConexion.commit()

miConexion.close()