nombreUsuario=input("Introduzca un nombre de usuario: ")

print("El nombre es: ", nombreUsuario.upper())
print("El nombre es: ", nombreUsuario.capitalize())

edad=input("Introduzca su edad: ")
while(edad.isdigit()==False):
	print("Por favor introduzca un valor numérico.")
	edad=input("Introduzca su edad: ")

#encriptador magico de mensajes
enMinusculas=nombreUsuario.lower()
fraseFinal=""
for letra in enMinusculas:
	if(letra == "a"):
		letra="4"
	elif(letra == "e"):
		letra="3"
	elif(letra == "i"):
		letra="1"
	elif(letra == "o"):
		letra="0"
	elif(letra == "u"):
		letra="Ü"
	fraseFinal+=letra
print(fraseFinal)