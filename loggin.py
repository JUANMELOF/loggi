#JUAN SEBASTIAN MELO FRANKY 2362707

import tkinter as tk 
from tkinter import*
from tkinter import messagebox
from menu import Menu
from Tooltip import Tooltip

class loggin(Menu):
    
    def mostrarAyuda(self, event):
        messagebox.showinfo("Ayuda", "Debe diligenciar todos los campos marcados con *\nLa contraseña tiene como minimo 8 caracteres")


    def verCaracteres(self,event):
        self.txtPasword.configure(show='')
        self.btnVer.configure(text="ocultar")



    def ocultarCaracteres(self,event):
        self.txtPasword.configure(show="*")
        self.btnVer.configure(text="ver")
    def validarLongitud(self,event):
        longitud=len(self.txtPasword.get())#Este .get trae el texto de la caja para contarlo con len
        if longitud >=8:
            self.btnIngresar.configure(state="normal")#Si la longitud de la contraseña es >= a 8 se deja clicar de lo contrario else
        else:
            self.btnIngresar.configure(state="disabled")
    


    def __init__(self):
        
        self.ventana = tk.Tk()  # Crea una nueva ventana
        self.ventana.resizable(0,0)  # Evita que se pueda redimensionar la ventana
        self.ventana.config(width=280, height=230)  # Establece el tamaño de la ventana
        self.ventana.title("Iniciar sesión")  # Establece el título de la ventana

        self.lblTitulo=tk.Label(self.ventana,text="inicio sesion ")
        self.lblTitulo.grid(row=0,column=0,columnspan=3)

        iconoAyuda = tk.PhotoImage(file="icons\help.png")
        self.btnAyuda = tk.Button(self.ventana, image=iconoAyuda)
        self.btnAyuda.place(relx=0.85, rely=0.15, width=25, height=25)
        Tooltip(self.btnAyuda, "Presione para obtener ayuda!\nAlt+A")
        self.btnAyuda.bind('<Button-1>', self.mostrarAyuda)

        self.lblUsuario=tk.Label(self.ventana,text="Usuario*")
        self.lblUsuario.grid(row=1,column=0,)
        self.txtUsuario=tk.Entry(self.ventana,width=25)
        self.txtUsuario.grid(row=1,column=1)
        Tooltip(self.txtUsuario, "Ingrese su nombre de usuario con el que está registrado")

        self.lblPasword=tk.Label(self.ventana,text="contraseña*")
        self.lblPasword.grid(row=2,column=0) 
        self.txtPasword=tk.Entry(self.ventana,width=25,show="*")#show Cada que el usuario ingresa algo por teclado aparece un *
        self.txtPasword.grid(row=2,column=1)
        self.txtPasword.bind("<KeyRelease>",self.validarLongitud)#escucha
        Tooltip(self.txtPasword, "Ingrese su contraseña para validar su usuario")


        botonVer= tk.PhotoImage(file="icons\eye.png")
        self.btnVer=tk.Button(self.ventana,image= botonVer)
        self.btnVer.grid(row=2,column=2)
        Tooltip(self.btnVer, "Al pasar el cursor verá la contraseña")

        self.btnVer.bind("<Enter>",self.verCaracteres)# Cuando se pasa el cursor muestra los caracteres
        self.btnVer.bind("<Leave>",self.ocultarCaracteres)

        
        iconoAccept = tk.PhotoImage(file="icons/accept.png")
        self.btnIngresar=tk.Button(self.ventana,text="Ingresar",image= iconoAccept ,command= self.cerrarYAbrirVentana,width=80,state="disabled", compound=LEFT)#pa que el usuario no pueda dar clic 
        self.btnIngresar.grid(row=3,column=1)
        Tooltip(self.btnIngresar, "Presione para validar e iniciar Sesion")
    
        self.btnLimpiar=tk.Button(self.ventana,text="limpiar") 
        self.btnLimpiar.grid(row=3,column=2)

        self.ventana.mainloop()
    
    def cerrarYAbrirVentana(self):
        
        self.ventana.destroy()  #Cerrar la ventana actual
        self.crearVentanaM()












        

