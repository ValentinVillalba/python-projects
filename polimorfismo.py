class coche():
	def desplazamiento(self):
		print("Me desplazo con cuatro ruedas.")
class moto():
	def desplazamiento(self):
		print("Me desplazo con dos ruedas.")
class camion():
	def desplazamiento(self):
		print("Me desplazo con seis ruedas.")

def desplazamientoVehiculo(vehiculo): 
	#se ingreso un vehiculo de tipo moto por lo que esta funcion sabe de que clase tomar el metodo desplazamiento.
	#en otros lenguajes es mas dificil
	vehiculo.desplazamiento()

miVehiculo=moto()
desplazamientoVehiculo(miVehiculo)