"""
Colors:
    ligth pink      #F2B3C4
    pale violet red #F391C7
    medium purple   #9475BF
    green yellow    #B4D966
    burlywood       #F2CC85

"""
import time # espacio de tiempo
import tkinter as tk

ventana = tk.Tk()
ventana.title('Bienvenido')
ventana.geometry('300x300')
boton = tk.Button('Hola')
ventana.configure(background='#F2B3C4')
etiqueta=tk.Label(ventana,text="Bienvenido",bg="#F391C7",
                  fg='#FFFFFF')
                  
etiqueta.pack(fill=tk.X,padx=5,pady=10)
ventana.mainloop()