import tkinter as tk
from tkinter import *
from Tooltip import Tooltip
from tkinter import messagebox


    
class Gestion():

    def confirmar(self, event):
        opcion = messagebox.askyesnocancel("Confirmar", "Está seguro que quiere salir de la Ventana?")
        if(opcion == True):
            self.ventana.destroy()  # Destruye la ventana principal si la opción es verdadera
        else:
            pass  # No hace nada si la opción es falsa o cancelada

    def limpiar(self, event):
        self.txtNombre.delete(0, END) # Borra el contenido del campo de entrada de nombre
        self.txtApellido.delete(0, END)
        self.txtCedula.delete(0, END)  # Borra el contenido del campo de entrada de cédula
        self.txtEmail.delete(0, END)   # Borra el contenido del campo de entrada de email
        self.txtTelefono.delete(0, END)  # Borra el contenido del campo de entrada de contraseña
        self.txtNombre.focus_set()

    def validarCedula(self, event):
        caracter = event.keysym  # Obtiene el carácter introducido
        if(caracter.isdigit()):  # Verifica si el carácter es un dígito - (caracter.isdigit() Valida números)
            self.txtCedula.config(bg="#FFFFFF")  # Cambia el color de fondo del campo de cédula a blanco
        else:
            if(event.keysym != "BackSpace"):  # Verifica si la tecla pulsada no es retroceso
                self.txtCedula.delete(len(self.txtCedula.get())-1, END)  # Borra el último carácter introducido
    def validarNombre(self, event):
        caracter = event.keysym  # Obtiene el carácter introducido
        if(caracter.isalpha()):  # Verifica si el carácter es una letra - (caracter.isalpha() Valida letras - caracter.isalnum() Valida letras y números)
            self.txtNombre.config(bg="#FFFFFF")  # Cambia el color de fondo del campo de nombre a blanco
        else:
            if(event.keysym != "BackSpace"):  # Verifica si la tecla pulsada no es retroceso
                self.txtNombre.delete(len(self.txtNombre.get())-1, END)  # Borra el último carácter introducido

    def crearCliente(self):
       
        self.ventana = tk.Toplevel()
        self.ventana.geometry("400x400")
        self.menu = tk.Menu(self.ventana)
        self.ventana.resizable(0,0)

        iconoAyuda = tk.PhotoImage(file="icons/help.png")
        self.btnAyuda = tk.Button(self.ventana, image=iconoAyuda)
        self.btnAyuda.place(relx=0.9, rely=0.1, width=25, height=25)
        Tooltip(self.btnAyuda, "Presione para obtener ayuda!\nAlt+A")
        self.btnAyuda.bind('<Button-1>', self.mostrarAyuda)
        
        self.ventana.bind('<Alt-a>', self.mostrarAyuda)

        self.lblTitulo=tk.Label(self.ventana,text="Crear Cliente")
        self.lblTitulo.place(relx=0.5, rely=0.1, anchor= "center")

        self.lblCedula = tk.Label(self.ventana, text="Cedula*")
        self.lblCedula.place(relx=0.1, rely=0.2)
        self.txtCedula = Entry(self.ventana)
        self.txtCedula.place(relx=0.3, rely=0.2)
        Tooltip(self.txtCedula, "Ingrese su numero de Cedula sin espacios")
        self.txtCedula.bind('<KeyRelease>', self.validarCedula)

        self.lblNombre = tk.Label(self.ventana, text="Nombre*")
        self.lblNombre.place(relx=0.1, rely=0.3)
        self.txtNombre = Entry(self.ventana)
        self.txtNombre.place(relx=0.3, rely=0.3)
        Tooltip(self.txtNombre, "Ingrese su Nombre")
        self.txtNombre.bind('<KeyRelease>', self.validarNombre)

        self.lblApellido = tk.Label(self.ventana, text="Apellido*")
        self.lblApellido.place(relx=0.1, rely=0.4)
        self.txtApellido = Entry(self.ventana)
        self.txtApellido.place(relx=0.3, rely=0.4)
        Tooltip(self.txtApellido, "Ingrese su Apellido")
        self.txtApellido.bind('<KeyRelease>', self.validarNombre)

        self.lblTelefono = tk.Label(self.ventana, text="Teléfono*")
        self.lblTelefono.place(relx=0.1, rely=0.5)
        self.txtTelefono = Entry(self.ventana)
        self.txtTelefono.place(relx=0.3, rely=0.5)
        Tooltip(self.txtTelefono, "Ingrese su numero de Teléfono")

        self.lblEmail = tk.Label(self.ventana, text="Email*")
        self.lblEmail.place(relx=0.1, rely=0.6)
        self.txtEmail = Entry(self.ventana)
        self.txtEmail.place(relx=0.3, rely=0.6)
        Tooltip(self.txtEmail, "Ingrese su Correo Electronico")

        iconoAdd= tk.PhotoImage(file="icons/add.png")
        self.btnguardar = Button(self.ventana, image= iconoAdd, width=50)
        self.btnguardar.place(relx=0.2, rely=0.7)

        iconoLimpiar = tk.PhotoImage(file= r"icons/textfield_delete.png")
        self.btnlimpiar = Button(self.ventana, text= "Limpiar", image=iconoLimpiar, compound=LEFT)
        self.btnlimpiar.place(relx=0.5, rely=0.7)
        self.btnlimpiar.bind('<Button-1>', self.limpiar)
        Tooltip(self.btnlimpiar, "Borra todos los campos")

        iconosalir = tk.PhotoImage(file= r"icons/cancel.png")
        self.btnsalir = tk.Button(self.ventana, text="Salir", image=iconosalir, compound=LEFT)
        self.btnsalir.place(relx=0.8, rely=0.7)
        self.btnsalir.bind('<Button-1>', self.confirmar)

        self.ventana.mainloop()

    def eliminarCliente(self):    
        
        self.ventana = tk.Toplevel()
        self.ventana.geometry("400x400")
        self.menu = tk.Menu(self.ventana)
        self.ventana.resizable(0,0)

        iconoAyuda = tk.PhotoImage(file="icons/help.png")
        self.btnAyuda = tk.Button(self.ventana, image=iconoAyuda)
        self.btnAyuda.place(relx=0.9, rely=0.1, width=25, height=25)
        Tooltip(self.btnAyuda, "Presione para obtener ayuda!\nAlt+A")
        self.btnAyuda.bind('<Button-1>', self.mostrarAyuda)
        
        self.ventana.bind('<Alt-a>', self.mostrarAyuda)

        self.lblTitulo=tk.Label(self.ventana,text="Eliminar Cliente")
        self.lblTitulo.place(relx=0.5, rely=0.1, anchor= "center")

        self.lblCedula = tk.Label(self.ventana, text="Cedula*")
        self.lblCedula.place(relx=0.1, rely=0.2)
        self.txtCedula = Entry(self.ventana)
        self.txtCedula.place(relx=0.3, rely=0.2)
        Tooltip(self.txtCedula, "Ingrese su numero de Cedula sin espacios")
        self.txtCedula.bind('<KeyRelease>', self.validarCedula)

        self.lblNombre = tk.Label(self.ventana, text="Nombre*")
        self.lblNombre.place(relx=0.1, rely=0.3)
        self.txtNombre = Entry(self.ventana)
        self.txtNombre.place(relx=0.3, rely=0.3)
        Tooltip(self.txtNombre, "Ingrese su Nombre")
        self.txtNombre.bind('<KeyRelease>', self.validarNombre)
        
        self.lblApellido = tk.Label(self.ventana, text="Apellido*")
        self.lblApellido.place(relx=0.1, rely=0.4)
        self.txtApellido = Entry(self.ventana)
        self.txtApellido.place(relx=0.3, rely=0.4)
        Tooltip(self.txtApellido, "Ingrese su Apellido")
        self.txtApellido.bind('<KeyRelease>', self.validarNombre)

        self.lblTelefono = tk.Label(self.ventana, text="Teléfono*")
        self.lblTelefono.place(relx=0.1, rely=0.5)
        self.txtTelefono = Entry(self.ventana)
        self.txtTelefono.place(relx=0.3, rely=0.5)
        Tooltip(self.txtTelefono, "Ingrese su numero de Teléfono")

        self.lblEmail = tk.Label(self.ventana, text="Email*")
        self.lblEmail.place(relx=0.1, rely=0.6)
        self.txtEmail = Entry(self.ventana)
        self.txtEmail.place(relx=0.3, rely=0.6)
        Tooltip(self.txtEmail, "Ingrese su Correo Electronico")

        iconoAdd= tk.PhotoImage(file="icons/add.png")
        self.btnguardar = Button(self.ventana, image= iconoAdd, width=50)
        self.btnguardar.place(relx=0.2, rely=0.7)

    
        iconoLimpiar = tk.PhotoImage(file= r"icons/textfield_delete.png")
        self.btnlimpiar = Button(self.ventana, text= "Limpiar", image=iconoLimpiar, compound=LEFT)
        self.btnlimpiar.place(relx=0.5, rely=0.7)
        self.btnlimpiar.bind('<Button-1>', self.limpiar)
        Tooltip(self.btnlimpiar, "Borra todos los campos")

        iconosalir = tk.PhotoImage(file= r"icons/cancel.png")
        self.btnsalir = tk.Button(self.ventana, text="Salir", image=iconosalir, compound=LEFT)
        self.btnsalir.place(relx=0.8, rely=0.7)
        self.btnsalir.bind('<Button-1>', self.confirmar)

        self.ventana.mainloop()

    def modificarCliente(self):    
       
        self.ventana = tk.Toplevel()
        self.ventana.geometry("400x400")
        self.menu = tk.Menu(self.ventana)
        self.ventana.resizable(0,0)

        iconoAyuda = tk.PhotoImage(file="icons/help.png")
        self.btnAyuda = tk.Button(self.ventana, image=iconoAyuda)
        self.btnAyuda.place(relx=0.9, rely=0.1, width=25, height=25)
        Tooltip(self.btnAyuda, "Presione para obtener ayuda!\nAlt+A")
        self.btnAyuda.bind('<Button-1>', self.mostrarAyuda)
        
        self.ventana.bind('<Alt-a>', self.mostrarAyuda)

        self.lblTitulo=tk.Label(self.ventana,text="Modificar Cliente")
        self.lblTitulo.place(relx=0.5, rely=0.1, anchor= "center")

        self.lblCedula = tk.Label(self.ventana, text="Cedula*")
        self.lblCedula.place(relx=0.1, rely=0.2)
        self.txtCedula = Entry(self.ventana)
        self.txtCedula.place(relx=0.3, rely=0.2)
        Tooltip(self.txtCedula, "Ingrese su numero de Cedula sin espacios")
        self.txtCedula.bind('<KeyRelease>', self.validarCedula)

        self.lblNombre = tk.Label(self.ventana, text="Nombre*")
        self.lblNombre.place(relx=0.1, rely=0.3)
        self.txtNombre = Entry(self.ventana)
        self.txtNombre.place(relx=0.3, rely=0.3)
        Tooltip(self.txtNombre, "Ingrese su Nombre")
        self.txtNombre.bind('<KeyRelease>', self.validarNombre)
        
        self.lblApellido = tk.Label(self.ventana, text="Apellido*")
        self.lblApellido.place(relx=0.1, rely=0.4)
        self.txtApellido = Entry(self.ventana)
        self.txtApellido.place(relx=0.3, rely=0.4)
        Tooltip(self.txtApellido, "Ingrese su Apellido")
        self.txtApellido.bind('<KeyRelease>', self.validarNombre)

        self.lblTelefono = tk.Label(self.ventana, text="Teléfono*")
        self.lblTelefono.place(relx=0.1, rely=0.5)
        self.txtTelefono = Entry(self.ventana)
        self.txtTelefono.place(relx=0.3, rely=0.5)
        Tooltip(self.txtTelefono, "Ingrese su numero de Teléfono")

        self.lblEmail = tk.Label(self.ventana, text="Email*")
        self.lblEmail.place(relx=0.1, rely=0.6)
        self.txtEmail = Entry(self.ventana)
        self.txtEmail.place(relx=0.3, rely=0.6)
        Tooltip(self.txtEmail, "Ingrese su Correo Electronico")

        iconoAdd= tk.PhotoImage(file="icons/add.png")
        self.btnguardar = Button(self.ventana, image= iconoAdd, width=50)
        self.btnguardar.place(relx=0.2, rely=0.7)

        
        iconoLimpiar = tk.PhotoImage(file= r"icons/textfield_delete.png")
        self.btnlimpiar = Button(self.ventana, text= "Limpiar", image=iconoLimpiar, compound=LEFT)
        self.btnlimpiar.place(relx=0.5, rely=0.7)
        self.btnlimpiar.bind('<Button-1>', self.limpiar)
        Tooltip(self.btnlimpiar, "Borra todos los campos")

        iconosalir = tk.PhotoImage(file= r"icons/cancel.png")
        self.btnsalir = tk.Button(self.ventana, text="Salir", image=iconosalir, compound=LEFT)
        self.btnsalir.place(relx=0.8, rely=0.7)
        self.btnsalir.bind('<Button-1>', self.confirmar)
        

        self.ventana.mainloop()