from tkinter import *

root=Tk()
root.geometry("200x200") #PARA CAMBIAR EL TAMAÑO DE LA VENTANAAAAA

varOpcion=IntVar()

def imprimir():
	#print(varOpcion.get())
	if varOpcion.get() == 1:
		etiqueta.config(text="Has elegido masculino.")
	elif varOpcion.get() == 2:
		etiqueta.config(text="Has elegido femenino.")
	else:
		etiqueta.config(text="Has elegido otros.")

Label(root, text="Género:").pack()
Radiobutton(root, text="Masculino", variable=varOpcion, value=1, command=imprimir, anchor="w").pack()
Radiobutton(root, text="Femenino", variable=varOpcion, value=2, command=imprimir, anchor="w").pack()
Radiobutton(root, text="Otros", variable=varOpcion, value=3, command=imprimir, anchor="w").pack()

etiqueta=Label(root)
etiqueta.pack() #EL PACK ES IMPORTANTEEEE NO OLVIDAR

root.mainloop()