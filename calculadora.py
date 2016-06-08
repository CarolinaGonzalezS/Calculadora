from tkinter import *
import tkinter.messagebox

def Suma():
	n1=float(caja1.get())
	n2=float(caja2.get())
	suma=n1+n2
	tkinter.messagebox.showinfo("Mensaje","El resultado es: %.2f"%suma)
	caja1.delete(0, 20)
	caja2.delete(0, 20)

def Resta():
	n1=float(caja1.get())
	n2=float(caja2.get())
	suma=n1-n2
	tkinter.messagebox.showinfo("Mensaje","El resultado es: %.2f"%suma)
	caja1.delete(0, 20)
	caja2.delete(0, 20)

def Multiplicacion():
	n1=float(caja1.get())
	n2=float(caja2.get())
	suma=n1*n2
	tkinter.messagebox.showinfo("Mensaje","El resultado es: %.2f"%suma)
	caja1.delete(0, 20)
	caja2.delete(0, 20)

def Division():
	n1=float(caja1.get())
	n2=float(caja2.get())
	if n2==0:
		tkinter.messagebox.showinfo("Mensaje","No existe division para 0")
	else:
		suma=n1/n2
		tkinter.messagebox.showinfo("Mensaje","El resultado es: %.2f"%suma)
		caja1.delete(0, 20)
		caja2.delete(0, 20)
