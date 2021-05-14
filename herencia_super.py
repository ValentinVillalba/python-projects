class persona():
	def __init__(self, nombre, edad, lugarResidencia):
		self.nombre=nombre
		self.edad=edad
		self.lugarResidencia=lugarResidencia
	def descripcion(self):
		print("Nombre: ",self.nombre,"\nEdad: ",self.edad,"\nResidencia: ",self.lugarResidencia)

class empleado(persona):
	def __init__(self, salario, antiguedad, nombre_empleado, edad_empleado, lugarResidencia_empleado):
		super().__init__(nombre_empleado, edad_empleado,lugarResidencia_empleado)
		#super ejecuta primero el constructor __init__ de la clase persona, por eso se ingresan sus datos.
		self.salario=salario
		self.antiguedad=antiguedad
	def descripcion(self):
		super().descripcion()
		print("Salario: ",self.salario,"\nAntiguedad: ", self.antiguedad)

manuel=empleado(2000,15, "Manuel",54,"Colombia")
manuel.descripcion()
print(isinstance(manuel, empleado))