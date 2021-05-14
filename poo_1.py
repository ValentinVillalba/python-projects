class Coche():

	def __init__(self):
		self.__largoChasis=250
		self.__anchoChasis=120
		self.__ruedas=4
		self.__enmarcha=False

	def metodoArrancar(self,arrancar):
		self.__enmarcha=arrancar

		if(self.__enmarcha):
			chequeo=self.__metodoChequeo()

		if(self.__enmarcha and chequeo):
			return "El coche está encendido"
		elif(self.__enmarcha and chequeo==False):
			return "Algo ha ido mal en el chequeo."
		else:
			return "El coche está apagado."

	def metodoEstado(self):
		print("El coche tiene ",self.__ruedas,"ruedas. Un ancho de ",self.__anchoChasis," y un largo de ",self.__largoChasis)

	def __metodoChequeo(self):
		print("Se realizara el chequeo interno...")
		self.gasolina="ok"
		self.aceite="bajo" #se cambió para que el chequeo falle
		self.puertas="cerradas"

		if(self.gasolina =="ok" and self.aceite=="ok" and self.puertas=="cerradas"):

			return True
		else:

			return False

miCoche=Coche()
print(miCoche.metodoArrancar(True))
miCoche.metodoEstado()

print("-----Coche número 2-----")

miCoche2=Coche()
miCoche2.ruedas = 6 #está encapsulada por los dos guiones por lo que no afecta al numero original
print(miCoche2.metodoArrancar(False))
miCoche2.metodoEstado()