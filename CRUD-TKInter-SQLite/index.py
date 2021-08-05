"""
Colors:
Primary   #C2185B
P-Ligth   #E91E63
P-Dark    #8BC34A
White     #FFFFFF
Black     #000000
Gray      #757575
"""
from tkinter import ttk
from tkinter import *

import sqlite3

db_name = 'productos.db'

# Funcionalidad de las ventanas
class Product:
    # 
    def __init__(self,window):
        # Intancamos la ventana
        self.wind = window
        # Utilizamos la ventana con una propiedad
        self.wind.title('Product Application')
        self.wind.configure(background="#FFFFFF")
        self.wind.geometry('505x500')
        self.wind.resizable(0,0)
        
        # Cremaos un Frame Container
        frame = LabelFrame(self.wind,text = 'Register a New Product',bg="#FFFFFF",
        fg='#C2185B',borderwidth=0,font='Helvetica 18 bold')
        frame.grid(row=0,column=0,padx=5,pady=20)    
        ## Entradas ##
        # Nombre
        Label(frame, text = 'Name:',bg="#FFFFFF",fg='#C2185B',borderwidth=0,font='Helvetica 13 ').grid(row =1, column = 0,pady=10)
        self.name=Entry(frame,width=73)
        self.name.focus()
        self.name.grid(row =1, column = 1,sticky=W+E)
        #Price
        Label(frame, text = 'Price:',bg="#FFFFFF",fg='#C2185B',borderwidth=0,font='Helvetica 13 ').grid(row =2, column = 0,pady=10)
        self.name=Entry(frame,width=73)
        self.name.grid(row =2, column = 1,sticky=W+E) 
        
        ttk.Button(frame,text='Save Product').grid(row=3,columnspan=3,pady=5, sticky=W+E)

        # Tabla
        self.tree=ttk.Treeview(heig=10,columns=2)
        self.tree.grid(row=4,column=0)
        self.tree.heading('#0',text='Name',anchor=CENTER)
        self.tree.heading('#1',text='Precio',anchor=CENTER)
    def run_query(self,query,parameters):
        with sqilite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            result = cursor.execute(query, parameters)
            conn.commit()
        return result

# Inicar la aplicacion
if __name__ == '__main__':
    #Creamos la ventana
    window = Tk()
    # Instanciamos la ventana y la pasamos como parametro
    application = Product(window)
    
    window.mainloop()