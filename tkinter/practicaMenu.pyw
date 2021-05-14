from tkinter import *
from tkinter import messagebox

root=Tk()

def infoAdicional():
	messagebox.showinfo("Acerca de...","Este programa fue creado por el mismisimo Villal en 2021")

def avisoLicencia():
	messagebox.showwarning("Licencia", "Te quedan 2 días de licencia")

def salirAplicacion():
	valor=messagebox.askquestion("Salir","¿Seguro que quiere salir?") #ESTO DEVUELVE UN VALOR YES O NO
	if valor == "yes":
		root.destroy() #ESTO CIERRA EL PROGRAMA

barraMenu=Menu(root)
root.config(menu=barraMenu)

root.title("Villal Corporation.exe")
root.geometry("400x350")
root.resizable(0,0)

archivoMenu=Menu(barraMenu, tearoff=0)
archivoMenu.add_command(label="Nuevo")
archivoMenu.add_separator()
archivoMenu.add_command(label="Guardar")
archivoMenu.add_command(label="Guardar como")
archivoMenu.add_separator()
archivoMenu.add_command(label="Salir", command=salirAplicacion)

archivoEdicion=Menu(barraMenu, tearoff=0)
archivoEdicion.add_command(label="Copiar")
archivoEdicion.add_command(label="Pegar")

archivoHerramientas=Menu(barraMenu, tearoff=0)
archivoHerramientas.add_command(label="Configuración")

archivoAyuda=Menu(barraMenu, tearoff=0)
archivoAyuda.add_command(label="Comandos")
archivoAyuda.add_command(label="Licencia", command=avisoLicencia)
archivoAyuda.add_command(label="Acerca de...", command=infoAdicional)

barraMenu.add_cascade(label="Archivo", menu=archivoMenu)
barraMenu.add_cascade(label="Edición", menu=archivoEdicion)
barraMenu.add_cascade(label="Herramientas", menu=archivoHerramientas)
barraMenu.add_cascade(label="Ayuda", menu=archivoAyuda)

root.mainloop()