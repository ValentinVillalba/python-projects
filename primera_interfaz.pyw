from tkinter import *

raiz=Tk()
raiz.title("doge") #cambia el titulo
#raiz.resizable(0,0) #impide que se cambie manualmente la resolucion
raiz.iconbitmap("doge.ico") #cambia el icono
raiz.geometry("640x480") #cambia la resolucion
raiz.config(bg="darkblue") #cambia el color del fondo a azul
raiz.config(bd=10)
raiz.config(relief="groove")

miFrame=Frame() #crea un frame dentro del azul
miFrame.pack(side="left", anchor="n") #posiciona el frame a la izquierda y al norte
miFrame.config(bg="red")
miFrame.config(width="650", height="350")
miFrame.config(bd=30)
miFrame.config(relief="groove")
miFrame.config(cursor="pirate")

raiz.mainloop() #para que una ventana pueda estar en ejecucion debe estar en un bucle infinito.
				#el metodo mainloop debe estar siempre al final
