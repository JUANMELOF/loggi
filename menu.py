import tkinter as tk
from tkinter import *
from Tooltip import *

from Info import Gestion

class Menu(Gestion):
    
    def crearVentanaM(self):
        self.ventana = tk.Tk()
        
        self.ventana.geometry("400x400")
        self.menu = tk.Menu(self.ventana)
        self.ventana.resizable(0,0)
        self.ventana.title("Gestion")
        self.lblwelcome = tk.Label(self.ventana, text= "WELCOME!!!", width= 10)
        self.lblwelcome.place(relx= 0.5, rely= 0.5, anchor= "center")

        self.gestionarCliente = tk.Menu(self.menu, tearoff=0)
        self.gestionarCliente.add_command(label="Crear Cliente ", command=self.crearCliente)
        self.gestionarCliente.add_command(label="Eliminar Cliente", command=self.eliminarCliente)
        self.gestionarCliente.add_command(label="Modificar Cliente ", command=self.modificarCliente)

        self.gestionarCuenta = tk.Menu(self.menu, tearoff=0)
        self.gestionarTrans = tk.Menu(self.menu, tearoff=0)
        self.salir= tk.Menu(self.menu, tearoff=0)

        self.menu.add_cascade(label="Gestionar Clientes", menu=self.gestionarCliente)
        self.menu.add_cascade(label="Gestionar Cuenta", menu=self.gestionarCuenta)
        self.menu.add_cascade(label="Gestionar Transaccion", menu=self.gestionarTrans)
        self.menu.add_cascade(label="SALIR", menu=self.salir )

        self.ventana.config(menu=self.menu)
    
        self.ventana.mainloop()
    
        
    
    


