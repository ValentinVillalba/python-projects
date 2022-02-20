from tkinter import *
root=Tk()

miFrame=Frame(root, width=1200, height=600)
miFrame.pack()

miNombre=StringVar()

cuadroNombre=Entry(miFrame, textvariable=miNombre)
cuadroNombre.grid(row=0, column=1, padx=5, pady=5)

cuadroContraseña=Entry(miFrame,show="*") #se muestran asteriscos.
cuadroContraseña.grid(row=1, column=1, padx=5, pady=5)

cuadroHC=Entry(miFrame)
cuadroHC.grid(row=2, column=1, padx=5, pady=5)

cuadroComentarios=Text(miFrame, width=16, height=5)
cuadroComentarios.grid(row=3, column=1, padx=5, pady=5)

scrollVert=Scrollbar(miFrame, command=cuadroComentarios.yview)
scrollVert.grid(row=3, column=2, sticky="nsew") #este sticky hace que se adapte al tamaño del cuadro.

cuadroComentarios.config(yscrollcommand=scrollVert.set) #indica en que punto del cuadro nos encontramos.

#----labels----

nombreLabel=Label(miFrame, text="Cuenta Riot: ")
nombreLabel.grid(row=0,column=0,sticky="e", pady=5)

contraseLabel=Label(miFrame, text="Contraseña: ")
contraseLabel.grid(row=1,column=0,sticky="e", pady=5)

hcLabel=Label(miFrame, text="Riot Points: ")
hcLabel.grid(row=2,column=0,sticky="e", pady=5)

comentariosLabel=Label(miFrame, text="Comentario: ")
comentariosLabel.grid(row=3,column=0,sticky="e", pady=5)

def codigoBoton():
	miNombre.set("TROLLEADO")

botonEnviar=Button(root, text="Enviar", command=codigoBoton)
botonEnviar.pack()

root.mainloop()
