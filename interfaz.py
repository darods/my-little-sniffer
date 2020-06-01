#!/usr/bin/env python
import tkinter
ventana = tkinter.Tk()

cajaIface = tkinter.Entry(ventana)
caja_n_pkts = tkinter.Entry(ventana)

etiquetaIface = tkinter.Label(ventana, text = "red: ")
etiqueta_n_pkts = tkinter.Label(ventana, text = "numero de paquetes: ")

def guardarIface():
    iface = cajaIface.get()
    print(iface)

def guardar_n_pkts():
    n_pkts = caja_n_pkts.get()
    print(n_pkts)

def guardar_todo():
    guardarIface()
    guardar_n_pkts()

botonIngresar = tkinter.Button(ventana, text="clic", command = guardar_todo)

# take the data 
lst = [(1,'Raj','Mumbai',19), 
       (2,'Aaryan','Pune',18), 
       (3,'Vaishnavi','Mumbai',20), 
       (4,'Rachna','Mumbai',21), 
       (5,'Shubham','Delhi',21)] 
   
# find total number of rows and 
# columns in list 
total_rows = len(lst) 
total_columns = len(lst[0]) 

class Table: 
    def __init__(self,root): 
          
        # code for creating table 
        for i in range(total_rows): 
            for j in range(total_columns): 
                  
                self.e = tkinter.Entry(root, width=20, fg='blue', 
                               font=('Arial',16,'bold')) 
                  
                self.e.grid(row=i+1, column=j)
                self.e.insert(tkinter.END, lst[i][j]) 

            self.boton = tkinter.Button(ventana, text="expandir "+str(i+1))
            self.boton.grid(row=i+1,column=j+1)

etiquetaIface.grid(row=0,column=0)
cajaIface.grid(row=0, column=1)
etiqueta_n_pkts.grid(row=0,column=2)
caja_n_pkts.grid(row=0, column=3)

botonIngresar.grid(row=0, column=4)
t = Table(ventana)
ventana.mainloop()
