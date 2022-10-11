import tkinter as tk
from tkinter import scrolledtext as st
import sys #Para finalizar el programa llamando a la función exit
from tkinter import filedialog  as fd #Ventanas de dialogo
from tkinter import messagebox as mb
from tkinter import *
from turtle import bgcolor
import cryptocode
import pyperclip as pc
import re
from re import I

class Aplication:
    def __init__(self):
        self.ventana1 = tk.Tk()
        self.ventana1.config(bg="#A8A8D3")
        self.menu()
        #T E X T O  A  C I F R A R  O  D E C I F R A R
        Label(text = "MENSAJE", fg="white", font = ("Verdana", 12), bg="#A8A8D3").place(x=15, y=0)
        self.scrolledtext1 = st.ScrolledText(self.ventana1, width = 60, height = 20, bg="#EFDBF7")
        self.scrolledtext1.grid(column=0, row=0, padx=10, pady=20)

        #L L A V E
        Label(text = "LLAVE", fg="white", font = ("Verdana", 12), bg="#A8A8D3").place(x=15, y=350)
        self.scrolledtext2 = st.ScrolledText(self.ventana1, width = 60, height =2, bg="#EFDBF7")
        self.scrolledtext2.grid(column=0, row=1, padx=10, pady=10)

        #B O T O N E S
        self.botones()

        #T E X T O  C I F R A D O  O  D E C I F R A D O
        Label(text = "MENSAJE CIFRADO/DECIFRADO", fg="white", font = ("Verdana", 12), bg="#A8A8D3").place(x=570, y=0)
        self.scrolledtext3 = st.ScrolledText(self.ventana1, width = 40, height = 20, bg="#EFDBF7")
        self.scrolledtext3.grid(column=1, row=0, padx=10, pady=20)

        self.ventana1.mainloop()
    

    def menu(self):
        menubar1 = tk.Menu(self.ventana1)
        self.ventana1.config(menu=menubar1)
        opc1 = tk.Menu(menubar1, tearoff=0)
        opc1.add_command(label="Guardar archivo", command=self.guardar)
        opc1.add_command(label="Guardar archivo Cif/Des", command=self.guardarCifDescif)
        opc1.add_command(label="Seleccionar archivo", command=self.recuperar)
        opc1.add_separator()
        opc1.add_command(label="Salir", command=self.salir)
        menubar1.add_cascade(label="File", menu=opc1)

    def salir(self):
        sys.exit(0)

    def guardar(self):
        nomArchivo = fd.asksaveasfilename(initialdir= "e:/CRYPTOGRAPHY", title= "Guardar como", filetypes= (("txt files", "*.txt"),("todos los archivos", "*.*")))
        if nomArchivo!='':
            arch1 = open(nomArchivo, "w", encoding="utf-8") #encoding es el tipo de archivo utf-8
            arch1.write(self.scrolledtext1.get("1.0", tk.END)) #con get grabamos d principio ("1.0)" a fin (tk.END))
            arch1.close()
            mb.showinfo("Información", "Los datos han sido guardados.")

    def recuperar(self):
        nomArchivo = fd.askopenfilename(initialdir= "e:/CRYPTOGRAPHY", title= "Seleccionar Archivo", filetypes= (("txt files", "*.txt"),("todos los archivos", "*.*")))
        if nomArchivo!='':
            arch1 = open(nomArchivo, "r", encoding="utf-8")
            contenido = arch1.read()
            arch1.close()
            self.scrolledtext1.delete("1.0", tk.END)
            self.scrolledtext1.insert("1.0", contenido)

    def guardarCifDescif(self):
        nomArchivo = fd.asksaveasfilename(initialdir= "e:/CRYPTOGRAPHY", title= "Guardar como", filetypes= (("txt files", "*.txt"),("todos los archivos", "*.*")))
        if nomArchivo!='':
            arch1 = open(nomArchivo, "w", encoding="utf-8") #encoding es el tipo de archivo utf-8
            arch1.write(self.scrolledtext3.get("1.0", tk.END)) #con get grabamos d principio ("1.0)" a fin (tk.END))
            arch1.close()
            mb.showinfo("Información", "Los datos han sido guardados.")

    def botones(self):
        botonCifrar = Button(self.ventana1, text="Cifrar", width=2, height=2, bg="#E5DBF7", fg="black",font=("Helvetica", 10, "bold"), command=self.cifrar)
        botonCifrar.place(x= 610, y= 380, width=90)
        botonDecifrar = Button(self.ventana1, text="Decifrar", width=2, height=2, bg="#E5DBF7", fg="black",font=("Helvetica", 10, "bold"), command=self.decifrar)
        botonDecifrar.place(x= 710, y= 380, width=90)

    def cifrar(self):
        msg = self.scrolledtext1.get("1.0", tk.END)
        clave = self.scrolledtext2.get("1.0", tk.END)
        cifrar = cryptocode.encrypt(msg,clave)
        msgCif = cifrar
        self.scrolledtext3.delete("1.0", tk.END)
        self.scrolledtext3.insert("1.0", msgCif)
    
    def decifrar(self):
        msg = self.scrolledtext1.get("1.0", tk.END)
        clave = self.scrolledtext2.get("1.0", tk.END)
        decifrar = cryptocode.decrypt(msg,clave)
        msgDecif = decifrar
        self.scrolledtext3.delete("1.0", tk.END)
        self.scrolledtext3.insert("1.0", msgDecif)


aplication = Aplication()