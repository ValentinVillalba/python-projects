from tkinter import *

root=Tk()
miFrame=Frame(root, width=500, height=400)
miFrame.pack()
miFrame.config(bg="black")
Label(miFrame, text="Ola ke tal",bg="black",fg="red",font=("Comic Sans MS",20)).place(x=100,y=100)

miImagen=PhotoImage(file="gary.png", width=200, height=200)
Label(miFrame, image=miImagen).place(x=100,y=150)

root.mainloop()