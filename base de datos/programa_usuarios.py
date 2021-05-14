from tkinter import *
from tkinter import messagebox
import sqlite3

root=Tk()

id_string=StringVar()
name_string=StringVar()
pass_string=StringVar()
lname_string=StringVar()
adress_string=StringVar()

#FUNCIONES

#cierra el programa
def exitFunction():
	value=messagebox.askquestion("Exit","Are you sure you want to exit?")
	if value == "yes":
		root.destroy()

#borra todos los campos
def eraseFields():
	id_string.set("")
	name_string.set("")
	pass_string.set("")
	lname_string.set("")
	adress_string.set("")
	text_entry_commentary.delete(1.0, END)

#muestra el tutorial
def showTutorial():
	messagebox.showinfo("Tutorial", "Enter information to create an account, or use the ID to read, update or delete an entry.")

#muestra la licencia
def showLicence():
	messagebox.showinfo("Licence", "Your licence is valid.")

#muestra el acerca de...
def showAbout():
	messagebox.showinfo("About...", "This program was created by xX||VILLAL-360||Xx.")

#genera un archivo de texto que contiene toda la informacion de la base de datos
def getDatabase():
	value4=messagebox.askquestion("ADMIN ONLY","Are you sure you want to create a .txt with everything in the database?")
	if value4 == "yes":
		file=open("complete_database.txt","w+")
		try:
			myConnection=sqlite3.connect("User_Database")
			myCursor=myConnection.cursor()

			number_of_rows=myCursor.execute("SELECT * FROM USERS")
			Everything=myCursor.fetchall()
			file.write("ID - NAME - PASSWORD - LAST NAME - HOME ADRESS - COMMENTARY")
			file.write("\n")
			file.write("\n")
			for row in Everything:
				file.write(str(row))
				file.write("\n")
				file.write("\n")

			messagebox.showinfo("File created", "The text file was created.")

		except sqlite3.OperationalError as DataError:
			messagebox.showerror("Error", "The database is not connected.")

#BASE DE DATOS Y FUNCIONES RELACIONADAS
#si la base de datos ya esta creada debe salir un messagebox de error a traves de controlar la excepcion.

def connectDatabase():
	try:
		myConnection=sqlite3.connect("User_Database")
		myCursor=myConnection.cursor()

		myCursor.execute(''' 
			CREATE TABLE USERS(
			ID INTEGER PRIMARY KEY AUTOINCREMENT,
			NAME VARCHAR(50),
			PASSWORD VARCHAR(50),
			LAST_NAME VARCHAR(50),
			HOME_ADRESS VARCHAR(50),
			COMMENTARY VARCHAR(100))
			''')
		messagebox.showinfo("Connected", "The database was connected successfully.")

	except sqlite3.OperationalError as DatabaseError:
		messagebox.showerror("Error", "The database is already connected.")

def createFunction():
	try:
		if name_string.get() != "" and pass_string.get() != "" and lname_string.get() != "" and adress_string.get() != "":
			data=name_string.get(),pass_string.get(),lname_string.get(),adress_string.get(),text_entry_commentary.get("1.0", END)

			try:
				myConnection=sqlite3.connect("User_Database")
				myCursor=myConnection.cursor()
				#EN LOS VALORES USAR LOS SIGNOS DE PREGUNTA (CONSULTA PARAMETRIZADA) PARA EVITAR LAS INYECCIONES SQL!!!
				myCursor.execute("INSERT INTO USERS (ID,NAME,PASSWORD,LAST_NAME,HOME_ADRESS,COMMENTARY) VALUES(NULL,?,?,?,?,?)", (data))
				myConnection.commit()
				eraseFields()
				messagebox.showinfo("User created!", "The user was registered in the database successfully.")

			except NameError as CursorError:
				messagebox.showerror("Error", "The database is not connected.")
		else:
			messagebox.showerror("Error", "Not enough information.")

	except sqlite3.OperationalError as TableError:
		messagebox.showerror("Error", "The database is not connected.")

def readFunction():
	if id_string.get() != "":
		theID=id_string.get()
		try:
			myConnection=sqlite3.connect("User_Database")
			myCursor=myConnection.cursor()

			myCursor.execute("SELECT * FROM USERS WHERE ID=(?)",theID)
			allTheInformation=myCursor.fetchall()
			myConnection.commit()

			id_string.set(allTheInformation[0][0])
			name_string.set(allTheInformation[0][1])
			pass_string.set(allTheInformation[0][2])
			lname_string.set(allTheInformation[0][3])
			adress_string.set(allTheInformation[0][4])
			text_entry_commentary.insert(1.0, allTheInformation[0][5])

			messagebox.showinfo("Information", "All the information of the user was loaded.")

		except sqlite3.OperationalError as NoDatabase:
			messagebox.showerror("Error", "The database is not connected.")
		except IndexError as WrongID:
			messagebox.showerror("Error", "The ID does not exist.")
		except sqlite3.ProgrammingError as BadID:
			messagebox.showerror("Error", "The ID does not exist.")
	else:
		messagebox.showerror("Error", "No ID entered.")

def updateFunction():
	if id_string.get() != "":
		try:
			myConnection=sqlite3.connect("User_Database")
			myCursor=myConnection.cursor()

			if name_string.get() != "" and pass_string.get() != "" and lname_string.get() != "" and adress_string.get() != "":
				data=name_string.get(),pass_string.get(),lname_string.get(),adress_string.get(),text_entry_commentary.get("1.0", END)

				value2=messagebox.askquestion("Update","Are you sure you want to update all the information of the user?")
				if value2 == "yes":
					myCursor.execute("UPDATE USERS SET NAME=?, PASSWORD=?,LAST_NAME=?,HOME_ADRESS=?,COMMENTARY=?" + "WHERE ID=" + id_string.get(),(data))
					myConnection.commit()

					messagebox.showinfo("Update", "All the information of the user was updated.")
			else:
				messagebox.showerror("Error", "Not enough information.")

		except sqlite3.OperationalError as NoDatabase:
			messagebox.showerror("Error", "The database is not connected.")
		except IndexError as WrongID:
			messagebox.showerror("Error", "The ID does not exist.")
		except sqlite3.ProgrammingError as BadID:
			messagebox.showerror("Error", "The ID does not exist.")
	else:
		messagebox.showerror("Error", "No ID entered.")

def destroyFunction():
	if id_string.get() != "":
		theID=id_string.get()
		try:
			myConnection=sqlite3.connect("User_Database")
			myCursor=myConnection.cursor()

			value3=messagebox.askquestion("Destroy","Are you sure you want to delete all the information of the user?")
			if value3 == "yes":
				myCursor.execute("DELETE FROM USERS WHERE ID=(?)", theID)
				myConnection.commit()

				messagebox.showinfo("Destroyed!", "All the information of the user was deleted from the database.")
				eraseFields()
			else:
				messagebox.showinfo("Not destroyed", "The user was not destroyed.")

		except sqlite3.OperationalError as NoDatabase:
			messagebox.showerror("Error", "The database is not connected.")
		except IndexError as WrongID:
			messagebox.showerror("Error", "The ID does not exist.")
		except sqlite3.ProgrammingError as BadID:
			messagebox.showerror("Error", "The ID does not exist.")
	else:
		messagebox.showerror("Error", "No ID entered.")

#ROOT

menuBar=Menu(root)
root.config(menu=menuBar)
root.title("User Manager")
root.iconbitmap("doge.ico")
root.resizable(0,0)

#MENU

BBDD_menu=Menu(menuBar, tearoff=0)
BBDD_menu.add_command(label="Connect", command=connectDatabase) #crea una base de datos
BBDD_menu.add_command(label="Exit", command=exitFunction) #mostrar messagebox para confirmar
BBDD_menu.add_separator()
BBDD_menu.add_command(label="GET DATABASE [ADMIN ONLY]", command=getDatabase)

Erase_menu=Menu(menuBar, tearoff=0)
Erase_menu.add_command(label="Erase fields", command=eraseFields) #vaciar todos los campos

CRUD_menu=Menu(menuBar, tearoff=0)
CRUD_menu.add_command(label="Create", command=createFunction) #lo mismo que los botones
CRUD_menu.add_command(label="Read", command=readFunction)
CRUD_menu.add_command(label="Update", command=updateFunction)
CRUD_menu.add_command(label="Destroy", command=destroyFunction)

Help_menu=Menu(menuBar, tearoff=0)
Help_menu.add_command(label="Licence", command=showLicence) #mostrar messagebox con cosas
Help_menu.add_command(label="About...", command=showAbout)
Help_menu.add_command(label="Tutorial", command=showTutorial)

menuBar.add_cascade(label="Data Base", menu=BBDD_menu)
menuBar.add_cascade(label="Erase", menu=Erase_menu)
menuBar.add_cascade(label="CRUD", menu=CRUD_menu)
menuBar.add_cascade(label="Help", menu=Help_menu)

#FRAME

myFrame=Frame(root)
myFrame.pack()

#ID

text_id=Label(myFrame,text="ID: ") #este debe ser un campo primary key, los demas de texto
text_id.grid(row=0, column=0, pady=10, padx=10, sticky="e")

entry_id=Entry(myFrame, textvariable=id_string)
entry_id.grid(row=0, column=1, pady=10, padx=5)

#NOMBRE

text_name=Label(myFrame,text="Name: ")
text_name.grid(row=1, column=0, pady=10, padx=10, sticky="e")

entry_name=Entry(myFrame, textvariable=name_string)
entry_name.grid(row=1, column=1, pady=10, padx=5)

#PASSWORD

text_pass=Label(myFrame,text="Password: ")
text_pass.grid(row=2, column=0, pady=10, padx=10, sticky="e")

entry_pass=Entry(myFrame, show="*", textvariable=pass_string)
entry_pass.grid(row=2, column=1, pady=10, padx=5)

#APELLIDO

text_lname=Label(myFrame,text="Last Name: ")
text_lname.grid(row=3, column=0, pady=10, padx=10, sticky="e")

entry_lname=Entry(myFrame, textvariable=lname_string)
entry_lname.grid(row=3, column=1, pady=10, padx=5)

#DIRECCION

text_dir=Label(myFrame,text="Home Adress: ")
text_dir.grid(row=4, column=0, pady=10, padx=10, sticky="e")

entry_dir=Entry(myFrame, textvariable=adress_string)
entry_dir.grid(row=4, column=1, pady=10, padx=5)

#COMENTARIOS

text_commentary=Label(myFrame,text="Commentary: ")
text_commentary.grid(row=5, column=0, pady=10, padx=10, sticky="e")

text_entry_commentary=Text(myFrame, width=16, height=5)
text_entry_commentary.grid(row=5, column=1, pady=10, padx=5)

#BOTONES

myFrame2=Frame() #hice otro frame para que los botones queden facheros sin depender de las cosas de arriba
myFrame2.pack()

create_button=Button(myFrame2, text="Create", command=createFunction)
create_button.grid(row=6, column=0, pady=10, padx=10, sticky="w")

read_button=Button(myFrame2, text="Read", anchor="w", command=readFunction)
read_button.grid(row=6, column=1, pady=10, padx=10, sticky="w")

update_button=Button(myFrame2, text="Update", anchor="w", command=updateFunction)
update_button.grid(row=6, column=2, pady=10, padx=10, sticky="w")

destroy_button=Button(myFrame2, text="Destroy", anchor="w", fg="red", command=destroyFunction)
destroy_button.grid(row=6, column=3, pady=10, padx=10, sticky="w")

#SCROLLBAR

scrollVert=Scrollbar(myFrame, command=text_entry_commentary.yview)
scrollVert.grid(row=5, column=2, sticky="nsew")

text_entry_commentary.config(yscrollcommand=scrollVert.set)

root.mainloop()