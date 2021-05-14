from tkinter import *
from random import randrange

root=Tk()
root.title("get a job.exe")
root.iconbitmap("jcd.ico")
root.geometry("500x480")
root.resizable(0,0)

totalLugares=[]
nombre="Denton"

newYork=IntVar()
china=IntVar()
paris=IntVar()
area=IntVar()

textoPregunta=Label(root,text="Where should {} get a job?".format(nombre), font=("Courier", 20, "bold"), pady=5, padx=5)
textoPregunta.pack()

def opcionesViaje():
	opcionEscogida=""
	if(newYork.get()==1):
		opcionEscogida+=" New York "
	if(china.get()==1):
		opcionEscogida+=" China "
	if(paris.get()==1):
		opcionEscogida+=" Paris "
	if(area.get()==1):
		opcionEscogida+=" Area 51 "

	textoFinal.config(text=opcionEscogida)

def funcionEnviar():
	global totalLugares

	if(newYork.get()==1):
		totalLugares.append(" New York ")
	if(china.get()==1):
		totalLugares.append(" China ")
	if(paris.get()==1):
		totalLugares.append(" Paris ")
	if(area.get()==1):
		totalLugares.append(" Area 51 ")

	else:
		totalLugares.append(" Nowhere [BAD ENDING] ")

	totalLugares=list(set(totalLugares))

	textoFinal.config(text=" {} found a job in: ".format(nombre), font=("Courier", 20), pady=5, padx=5)

	textoLugar.pack()
	textoLugar.config(text=totalLugares[randrange(len(totalLugares))], font=("Courier", 20), pady=5, padx=5)

	textoPregunta.config(text="Congratulations!", font=("Courier", 20, "bold"), pady=5, padx=5)

	foto.config(file="happy_jcd.png")

	sendButton.pack_forget() #ESTO ELIMINA EL BOTON AL HACER CLICK EN ÉL
	destinationText.pack_forget()
	nyb.pack_forget()
	chb.pack_forget()
	pab.pack_forget()
	arb.pack_forget()

foto=PhotoImage(file="denton.png")
fotoPanel=Label(root, image=foto).pack()

frame=Frame(root)
frame.pack()

destinationText=Label(frame, text="Destinations:", width=50, font=("Courier", 20))
destinationText.pack()

nyb=Checkbutton(root, text="New York", font=("Courier", 14), variable=newYork, onvalue=1, offvalue=0, command=opcionesViaje)
nyb.pack()
chb=Checkbutton(root, text="China", font=("Courier", 14), variable=china, onvalue=1, offvalue=0, command=opcionesViaje)
chb.pack()
pab=Checkbutton(root, text="Paris", font=("Courier", 14), variable=paris, onvalue=1, offvalue=0, command=opcionesViaje)
pab.pack()
arb=Checkbutton(root, text="Area 51", font=("Courier", 14), variable=area, onvalue=1, offvalue=0, command=opcionesViaje)
arb.pack()

sendButton=Button(root,text="Send Denton", font=("Courier", 14), pady=2, padx=2, command=funcionEnviar)
sendButton.pack()

textoFinal=Label(frame, font=("Courier", 12))
textoFinal.pack()
textoLugar=Label(frame, font=("Courier", 12))

root.mainloop()