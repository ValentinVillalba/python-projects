import pickle

class Persona:

	def __init__(self,nombre,genero,edad):
		self.nombre=nombre
		self.genero=genero
		self.edad=edad
		print("Se ha creado una persona nueva con el nombre: ",self.nombre)
	def __str__(self): #convierte en cadena de texto la información de un objeto.
		return "{} {} {}".format(self.nombre,self.genero,self.edad)

class ListaPersonas:
	personas=[]

	def __init__(self):
		listaDePersonas=open("ficheroExterno","ab+")
		listaDePersonas.seek(0)
		try:
			self.personas=pickle.load(listaDePersonas)
			print("Se cargaron {} personas del fichero externo.".format(len(self.personas)))
		except:
			print("El fichero está vacío.")
		finally:
			listaDePersonas.close()
			del(listaDePersonas)
	def agregarPersonas(self,p):
		self.personas.append(p)
		self.guardarPersonasEnFicheroExterno()
	def mostrarPersonas(self):
		for p in self.personas:
			print(p)
	def guardarPersonasEnFicheroExterno(self):
		listaDePersonas=open("ficheroExterno","wb")
		pickle.dump(self.personas, listaDePersonas)
		listaDePersonas.close()
		del(listaDePersonas)
	def mostrarInfoFicheroExterno(self):
		print("La infromación actual del fichero externo es la siguiente: ")
		for p in self.personas:
			print(p)

miLista=ListaPersonas()

nombrePersona=""
while nombrePersona != "0":
	nombrePersona=input("Ingrese el nombre de la nueva persona (0 para cancelar): ")
	if nombrePersona == "0":
		break
	generoPersona=input("Ingrese la inicial del genero de la persona: ")
	edadPersona=int(input("Ingrese la edad de la persona: "))
	persona=Persona(nombrePersona,generoPersona,edadPersona)
	miLista.agregarPersonas(persona)

miLista.mostrarInfoFicheroExterno()