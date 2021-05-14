from tkinter import *

root=Tk()
root.title("Doge Calculator")
root.iconbitmap("doge.ico")
root.geometry("300x450")
root.resizable(0,0)
root.config(bg="#3b4a3f")

miFrame=Frame(root)
miFrame.config(bg="#3b4a3f")
miFrame.pack()
operacion=""
tipo=""
resultado=0
#---------------pantalla-----------------
numeroPantalla=StringVar()
pantalla=Entry(miFrame, textvariable=numeroPantalla)
pantalla.grid(row=1,column=1, padx=5, pady=5, columnspan=4)
pantalla.config(background="black",fg="#03f943", justify="right")
#----------------funciones---------------
def funcionBoton(num):
	global operacion
	if num == "0" and numeroPantalla.get() == "":
		pass
	elif operacion !="":
		numeroPantalla.set(num)
		operacion=""
	else:
		numeroPantalla.set(numeroPantalla.get() + num)
def funcionComa():
	if numeroPantalla.get() != "" and "." not in numeroPantalla.get():
		numeroPantalla.set(numeroPantalla.get() + ".")
	else:
		pass
def funcionCancelar():
	numeroPantalla.set("")
def suma(num):
	global operacion
	global resultado
	global tipo
	resultado+=float(num)
	operacion="suma"
	tipo="suma"
	numeroPantalla.set(resultado)
def elResultado():
	global resultado
	global operacion
	if tipo == "suma":
		numeroPantalla.set(resultado+float(numeroPantalla.get()))
	elif tipo == "resta":
		numeroPantalla.set(resultado-float(numeroPantalla.get()))
	elif tipo == "division":
		numeroPantalla.set(resultado/float(numeroPantalla.get()))
	elif tipo == "multiplic":
		numeroPantalla.set(resultado*float(numeroPantalla.get()))
	resultado=0
def resta(num):
	global operacion
	global resultado
	global tipo
	resultado+=float(num)
	operacion="resta"
	tipo="resta"
	numeroPantalla.set(resultado)
def division(num):
	global operacion
	global resultado
	global tipo
	resultado+=float(num)
	operacion="division"
	tipo="division"
	numeroPantalla.set(resultado)
def multiplic(num):
	global operacion
	global resultado
	global tipo
	resultado+=float(num)
	operacion="multiplic"
	tipo="multiplic"
	numeroPantalla.set(resultado)
#-------------fila1----------------------
boton7=Button(miFrame, text="7", width=3, fg="#03f943", bg="black", command=lambda:funcionBoton("7"))
boton7.grid(row=2,column=1)
boton8=Button(miFrame, text="8", width=3, fg="#03f943", bg="black", command=lambda:funcionBoton("8"))
boton8.grid(row=2,column=2)
boton9=Button(miFrame, text="9", width=3, fg="#03f943", bg="black", command=lambda:funcionBoton("9"))
boton9.grid(row=2,column=3)
botonDiv=Button(miFrame, text="/", width=3, fg="#03f943", bg="black", command=lambda:division(numeroPantalla.get()))
botonDiv.grid(row=2,column=4)
#-------------fila2----------------------
boton4=Button(miFrame, text="4", width=3, fg="#03f943", bg="black", command=lambda:funcionBoton("4"))
boton4.grid(row=3,column=1)
boton5=Button(miFrame, text="5", width=3, fg="#03f943", bg="black", command=lambda:funcionBoton("5"))
boton5.grid(row=3,column=2)
boton6=Button(miFrame, text="6", width=3, fg="#03f943", bg="black", command=lambda:funcionBoton("6"))
boton6.grid(row=3,column=3)
botonMult=Button(miFrame, text="X", width=3, fg="#03f943", bg="black", command=lambda:multiplic(numeroPantalla.get()))
botonMult.grid(row=3,column=4)
#-------------fila3----------------------
boton1=Button(miFrame, text="1", width=3, fg="#03f943", bg="black", command=lambda:funcionBoton("1"))
boton1.grid(row=4,column=1)
boton2=Button(miFrame, text="2", width=3, fg="#03f943", bg="black", command=lambda:funcionBoton("2"))
boton2.grid(row=4,column=2)
boton3=Button(miFrame, text="3", width=3, fg="#03f943", bg="black", command=lambda:funcionBoton("3"))
boton3.grid(row=4,column=3)
botonResta=Button(miFrame, text="-", width=3, fg="#03f943", bg="black", command=lambda:resta(numeroPantalla.get()))
botonResta.grid(row=4,column=4)
#-------------fila4----------------------
boton0=Button(miFrame, text="0", width=3, fg="#03f943", bg="black", command=lambda:funcionBoton("0"))
boton0.grid(row=5,column=1)
botonComa=Button(miFrame, text=",", width=3, fg="#03f943", bg="black", command=lambda:funcionComa())
botonComa.grid(row=5,column=2)
botonIgual=Button(miFrame, text="=", width=3, fg="#03f943", bg="black", command=lambda:elResultado())
botonIgual.grid(row=5,column=3)
botonSuma=Button(miFrame, text="+", width=3, fg="#03f943", bg="black", command=lambda:suma(numeroPantalla.get()))
botonSuma.grid(row=5,column=4)
#--------------fila5----------------------
botonCancelar=Button(miFrame, text="CANCELAR", fg="#03f943", bg="black", command=lambda:funcionCancelar())
botonCancelar.grid(row=6, column=1, columnspan=4, pady=5,)
#-------------fila6-----------------------
textoAbajo=Label(root, text="Doge Calculator by Villal - Ver 1.0", bg="#3b4a3f", font=("Comic Sans MS", 12, "bold"), pady=5, fg="#03f943")
textoAbajo.pack()
imagenDoge=PhotoImage(file="gary.png")
Label(root, image=imagenDoge, width=200, height=200, relief="solid", borderwidth=5).place(x=50,y=220)

root.mainloop()