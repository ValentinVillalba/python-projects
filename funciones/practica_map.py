class Empleado:
	def __init__(self, nombre, cargo, salario):
		self.nombre=nombre
		self.cargo=cargo
		self.salario=salario
	def __str__(self):
		return "{} que trabaja como {} tiene un salario de {}$".format(self.nombre, self.cargo, self.salario)

listaEmpleados=[
	Empleado("Juan","Director",7500),
	Empleado("Ana","Presidenta",8000),
	Empleado("Antonio","Administrador",3400),
	Empleado("Sara","Secretaria",2700),
	Empleado("Mario","Botones",2100)
]

def calculoComision(empleado):
	if(empleado.salario<=3000):
		empleado.salario=empleado.salario*1.03
	return empleado

listaEmpleadosComision=map(calculoComision, listaEmpleados) #A CADA ELEMENTO DE LA LISTA EMPLEADOS LE APLICA LA FUNCION CALCULO COMISION

for empleado in listaEmpleadosComision:
	print(empleado)