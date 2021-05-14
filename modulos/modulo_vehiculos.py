class vehiculos():
	def __init__(self, marca, modelo):
		self.marca=marca
		self.modelo=modelo
		self.enmarcha=False
		self.acelera=False
		self.frena=False
	def arrancar(self):
		self.enmarcha=True
	def acelerar(self):
		self.acelera=True
	def frenar(self):
		self.frena=True
	def estado(self):
		print("Marca: ",self.marca, "\nModelo: ",self.modelo,"\nEn marcha: ",
			self.enmarcha,"\nAcelerando: ",self.acelera,"\nFrenando: ",self.frena)

class moto(vehiculos): #esta es la sintaxis para heredar, se usa como parametro la clase de la que se van a heredar los metodos.
	hcaballito="No voy haciendo el caballito"
	def caballito(self):
		self.hcaballito="Voy haciendo el caballito"
	def estado(self): #se sobreescribio el metodo estado de la clase padre (vehiculos)
		print("Marca: ",self.marca, "\nModelo: ",self.modelo,"\nEn marcha: ",
			self.enmarcha,"\nAcelerando: ",self.acelera,"\nFrenando: ",self.frena,"\nLa moto: ", self.hcaballito) #al sobreescribir se puede usar hcaballito

class furgoneta(vehiculos):
	def carga(self,cargar): #un nuevo metodo ademas de los que hereda de vehiculos.
		self.cargado=cargar
		if(self.cargado):
			return "La furgoneta está cargada"
		else:
			return "La furgoneta no está cargada"
class vehElectricos():
	def __init__(self, marca, modelo):
		super().__init__(marca, modelo)
		self.autonomia=100
	def cargarEnergia(self):
		self.cargado=True