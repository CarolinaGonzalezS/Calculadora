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
		
gui=Tk()
gui.title("Calculadora")
gui.geometry("400x250+400+200")

var1=StringVar()
var1.set("Escribe el primer numero:")
label1= Label(gui, bd=4, textvariable=var1, height=2)
label1.pack()

numero1=StringVar()
caja1=Entry(gui, bd=4, textvariable=numero1)
caja1.pack()

var2=StringVar()
var2.set("Escriba el segundo numero:")
label2= Label(gui, bd=4, textvariable=var2, height=2)
label2.pack()

numero2=StringVar()
caja2=Entry(gui, bd=4, textvariable=numero2)
caja2.pack()

boton1=Button(gui, text="Suma", command=Suma, width=15)
boton1.pack()

boton2=Button(gui, text="Resta", command=Resta, width=15)
boton2.pack()

boton3=Button(gui, text="Multiplicacion", command=Multiplicacion, width=15)
boton3.pack()

boton4=Button(gui, text="Division", command=Division, width=15)
boton4.pack()

gui.mainloop()
