import tkinter as tk
from tkinter import *
from tkinter import messagebox
from Tooltip import Tooltip  # Importa la clase Tooltip desde un módulo externo
from loggin import loggin

class Registro():
    # Función para mostrar un mensaje de ayuda
    
    def mostrarAyuda(self, event):
        messagebox.showinfo("Ayuda", "Debe diligenciar todos los campos marcados con *\nluego presione el botón Registrarse")

    # Función para confirmar la salida de la aplicación
    def confirmar(self, event):
        opcion = messagebox.askyesnocancel("Confirmar", "Está seguro que quiere salir de la Aplicación?")
        if(opcion == True):
            self.ventana.destroy()  # Destruye la ventana principal si la opción es verdadera
        else:
            pass  # No hace nada si la opción es falsa o cancelada
    
    # Función para limpiar los campos de texto
    def limpiar(self, event):
        self.txtNombre.delete(0, END)  # Borra el contenido del campo de entrada de nombre
        self.txtCedula.delete(0, END)  # Borra el contenido del campo de entrada de cédula
        self.txtEmail.delete(0, END)   # Borra el contenido del campo de entrada de email
        self.txtPassword.delete(0, END)  # Borra el contenido del campo de entrada de contraseña
        self.btnRegistrar.config(state="disabled")  # Deshabilita el botón de registro
        self.txtNombre.focus_set()  # Coloca el foco de entrada en el campo de nombre

    # Función para validar el campo de nombre
    def validarNombre(self, event):
        caracter = event.keysym  # Obtiene el carácter introducido
        if(caracter.isalpha()):  # Verifica si el carácter es una letra - (caracter.isalpha() Valida letras - caracter.isalnum() Valida letras y números)
            self.txtNombre.config(bg="#FFFFFF")  # Cambia el color de fondo del campo de nombre a blanco
        else:
            if(event.keysym != "BackSpace"):  # Verifica si la tecla pulsada no es retroceso
                self.txtNombre.delete(len(self.txtNombre.get())-1, END)  # Borra el último carácter introducido
            
        if(len(self.txtNombre.get()) >= 8 and len(self.txtCedula.get()) >= 8):  # Verifica si los campos tienen al menos 8 caracteres
            self.btnRegistrar.config(state="normal")  # Habilita el botón de registro
        else:
            self.btnRegistrar.config(state="disabled")  # Deshabilita el botón de registro si no se cumplen las condiciones

    # Función para validar el campo de cédula
    def validarCedula(self, event):
        caracter = event.keysym  # Obtiene el carácter introducido
        if(caracter.isdigit()):  # Verifica si el carácter es un dígito - (caracter.isdigit() Valida números)
            self.txtCedula.config(bg="#FFFFFF")  # Cambia el color de fondo del campo de cédula a blanco
        else:
            if(event.keysym != "BackSpace"):  # Verifica si la tecla pulsada no es retroceso
                self.txtCedula.delete(len(self.txtCedula.get())-1, END)  # Borra el último carácter introducido
            
        if(len(self.txtNombre.get()) >= 8 and len(self.txtCedula.get()) >= 8):  # Verifica si los campos tienen al menos 8 caracteres
            self.btnRegistrar.config(state="normal")  # Habilita el botón de registro
        else:
            self.btnRegistrar.config(state="disabled")  # Deshabilita el botón de registro si no se cumplen las condiciones

    # Función para validar el campo de correo electrónico
    def validarEmail(self, event):
        return True  # Por implementar

    # Función para validar el campo de contraseña
    def validarPass(self, event):
        return True  # Por implementar
    
    # Función para registrar un nuevo usuario
    def registrarUsuario(self):
        self.ventana.destroy()
        logg = loggin()
        logg.ventana.mainloop()
        

    def __init__(self):
        # Configuración de la ventana principal
        self.ventana = tk.Tk()  # Crea una nueva ventana
        self.ventana.resizable(0,0)  # Evita que se pueda redimensionar la ventana
        self.ventana.config(width=280, height=230)  # Establece el tamaño de la ventana
        self.ventana.title("Registro de Usuarios")  # Establece el título de la ventana

        # Creación de widgets: etiquetas, campos de entrada y botones
        self.lblTitulo = tk.Label(self.ventana, text="Registrarse")
        self.lblTitulo.place(relx=0.5, y=45, height=15, anchor="center")

        iconoAyuda = tk.PhotoImage(file= r"icons/help.png")
        self.btnAyuda = tk.Button(self.ventana, image=iconoAyuda)
        self.btnAyuda.place(relx=1, x=-45, y=10, width=25, height=25)
        Tooltip(self.btnAyuda, "Presione para obtener ayuda!\nAlt+a")

        self.lblNombre = tk.Label(self.ventana, text="Nombres*:")
        self.lblNombre.place(x=20, y=70, height=15)
        self.txtNombre = tk.Entry(self.ventana)
        self.txtNombre.place(relx=1, x=-170, y=70, width=150, height=15)
        Tooltip(self.txtNombre, "Ingrese su nombre completo, mínimo 8 caracteres.\nSolo letras [a-z]")
        self.txtNombre.bind('<KeyRelease>', self.validarNombre)

        self.lblCedula = tk.Label(self.ventana, text="Cédula*:")
        self.lblCedula.place(x=20, y=100, height=15)
        self.txtCedula = tk.Entry(self.ventana)
        self.txtCedula.place(relx=1, x=-170, y=100, width=150, height=15)
        Tooltip(self.txtCedula, "Ingrese su número de Cédula, mínimo 8 caracteres.\nSolo números [0-9]")
        self.txtCedula.bind('<KeyRelease>', self.validarCedula)

        self.lblEmail = tk.Label(self.ventana, text="Email*:")
        self.lblEmail.place(x=20, y=130, height=15)
        self.txtEmail = tk.Entry(self.ventana)
        self.txtEmail.place(relx=1, x=-170, y=130, width=150, height=15)
        Tooltip(self.txtEmail, "Ingrese su Correo Electrónico.\nSolo recibe letas, números y los caracteres especiales listados [a-z, 0-9, @, -, _ ]")
        self.txtEmail.bind('<KeyRelease>', self.validarEmail)

        self.lblPassword = tk.Label(self.ventana, text="Password*:")
        self.lblPassword.place(x=20, y=160, height=15)
        self.txtPassword = tk.Entry(self.ventana)
        self.txtPassword.place(relx=1, x=-170, y=160, width=150, height=15)
        Tooltip(self.txtPassword, "Ingrese su Password.\nSolo letas, números y el punto [a-z, 0-9, .]")
        self.txtPassword.bind('<KeyRelease>', self.validarPass)

        iconoSalir = tk.PhotoImage(file= r"icons/cancel.png")
        #El atributo compound determina la ubicación del icono en el botón respecto al texto LEFT-UP-DOWN-RIGTH.
        self.btnSalir = tk.Button(self.ventana, text="Salir", image=iconoSalir, compound=LEFT)
        self.btnSalir.place(relx=1, x=-80, rely=1, y=-45, width=60, height=25)
        Tooltip(self.btnSalir, "Presione para Salir de la Aplicación.\nAlt+s")

        iconoLimpiar = tk.PhotoImage(file= r"icons/textfield_delete.png")
        self.btnLimpiar = tk.Button(self.ventana, text="Limpiar", image=iconoLimpiar, compound=LEFT)
        self.btnLimpiar.place(relx=1, x=-170, rely=1, y=-45, width=70, height=25)
        Tooltip(self.btnLimpiar, "Presione para Limpiar los campos de texto.\nAlt+l")

        iconoRegistrar = tk.PhotoImage(file= r"icons/user_add.png")
        self.btnRegistrar = tk.Button(self.ventana, text="Registrar", image=iconoRegistrar, compound=LEFT, state="disabled", command=lambda:self.registrarUsuario())
        self.btnRegistrar.place(x=20, rely=1, y=-45, width=70, height=25)
        Tooltip(self.btnRegistrar, "Presione para Registrarse como usuario o presione la tecla 'Enter'.\n")

        # Asociación de funciones con eventos y atajos de teclado
        self.btnAyuda.bind('<Button-1>', self.mostrarAyuda)  # Asocia el evento clic del botón de ayuda con la función mostrarAyuda
        self.btnSalir.bind('<Button-1>', self.confirmar)  # Asocia el evento clic del botón de salida con la función confirmar
        self.btnLimpiar.bind('<Button-1>', self.limpiar)  # Asocia el evento clic del botón de limpieza con la función limpiar
        self.ventana.bind('<Alt-a>', self.mostrarAyuda)  # Asocia la combinación de teclas Alt+a con la función mostrarAyuda
        self.ventana.bind('<Alt-s>', self.confirmar)  # Asocia la combinación de teclas Alt+s con la función confirmar
        self.ventana.bind('<Alt-l>', self.limpiar)  # Asocia la combinación de teclas Alt+l con la función limpiar

        self.ventana.mainloop()  # Inicia el bucle principal de la aplicación


