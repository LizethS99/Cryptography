import tkinter as tk
from tkinter import scrolledtext as st
import sys #Para finalizar el programa llamando a la función exit
from tkinter import filedialog  as fd #Ventanas de dialogo
from tkinter import messagebox as mb
from tkinter import *
from PIL import ImageTk, Image
from turtle import bgcolor
import cryptocode
import pyperclip as pc
import os
import re
from re import I
#--------Limpiar pantalla-------
def limpiar():
    fek.set(f"No se puede obtener función EK")
    fdk.set(f"No se puede obtener función DK")
#--------Salida---------
def Salida(a, b, n, u0):
    fek.set(f"FUNCION EK : \nC ={a} (m) + {b} mod {n}")
    beta2 = n-b
    fdk.set(f"FUNCION DK : \nm = {u0} [C + {beta2}] mod {n}")

#--------Encontramos 1/alfa con el algoritmo extendido de Euclides--------
def xgcd(a, n, b):
    baux =b
    if n == 0:
        return 0,1,0
    u0 = 1
    u1 = 0
    v0 = 0
    v1 = 1
    while n != 0:
        q = a//n
        r = a - n * q
        u = u0 - q * u1
        v = v0 - q * v1
        #Update a,b
        a = n
        n = r
        #Update for next iteration
        u0 = u1
        u1 = u
        v0 = v1
        v1 = v
    newn = u*-1
    newa = v
    print(f"\t1 = {v}*({u0})+{newn}*({v0})")
    #print(f"a = {a}, b = {b}, u0 = {u0}, u1 = {u1}, v0 = {v0}, v1 = {v1}, beta = {baux}")
    Salida(newa, baux, newn, u0)

#--------Validamos alfa con el algoritmode Euclides---------
def validar(alfa, a, n, b):
    if(alfa == 1):
        mb.showinfo("Información","Alfa valido")
        xgcd(a, n, b)
    else:
        mb.showinfo("Información", "Alfa no valido, intente con otro valor.")
        limpiar()

def mcd():
    alfa = alf.get()
    na = alfa
    n = modn.get()
    nn = n
    b = beta.get()
    while(n!=0):
        aux=n
        n=alfa%n
        alfa=aux 
    validar(alfa, na, nn, b ) 

ventana1 =Tk()
ventana1.geometry("500x250")
ventana1.config(bg="#A8A8D3")
ventana1.title("Práctica 2")
image = Image
img = PhotoImage(file="Practica3\cfondo.gif")
lblImagen = Label(ventana1, image= img).place(x=0, y=0)
alf = IntVar()
beta = IntVar()
modn = IntVar()
fek = StringVar()
fdk = StringVar()

#A L F A
Label(text = "ALFA", fg="white", font = ("Verdana", 12), bg="#A8A8D3").place(x=65, y=30)
caja = Entry(ventana1, textvariable=alf)
caja.grid(column=0, row=0, padx=65, pady=60)
        
#B E T A
Label(text = "BETA", fg="white", font = ("Verdana", 12), bg="#A8A8D3").place(x=65, y=110)
caja = Entry(ventana1, textvariable=beta)
caja.grid(column=0, row=1, padx=65, pady=2)
#M O D  N
Label(text = "MOD N", fg="white", font = ("Verdana", 12), bg="#A8A8D3").place(x=65, y=180)
caja = Entry(ventana1, textvariable=modn)
caja.grid(column=0, row=2, padx=65, pady=48)

#F U N C I O N E S
textoEK = Label(textvariable=fek, fg="white", font = ("Verdana", 12), bg="#A8A8D3").place(x=220, y=30)
textoDK = Label(textvariable=fdk ,fg="white", font = ("Verdana", 12), bg="#A8A8D3").place(x=220, y=90)

#B O T O N
botonCifrar = Button(ventana1, text="Obtener Funciones", width=2, height=2, bg="#E5DBF7", fg="black",font=("Helvetica", 10, "bold"), command=mcd)
botonCifrar.place(x= 220, y= 180, width=180)
ventana1.mainloop()
