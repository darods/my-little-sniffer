#!/usr/bin/env python
import tkinter
from sniffer import sniffer
ventana = tkinter.Tk()

class ingreso:
    def __init__(self,ventana):
        self.cajaIface = tkinter.Entry(ventana)
        self.caja_n_pkts = tkinter.Entry(ventana)

        self.etiquetaIface = tkinter.Label(ventana, text = "red: ")
        self.etiqueta_n_pkts = tkinter.Label(ventana, text = "numero de paquetes: ")
        self.botonIngresar = tkinter.Button(ventana, text="clic", command = self.guardar_todo) 
        
        self.etiquetaIface.grid(row=0,column=0)
        self.cajaIface.grid(row=0, column=1)
        self.etiqueta_n_pkts.grid(row=0,column=2)
        self.caja_n_pkts.grid(row=0, column=3)
        self.botonIngresar.grid(row=0, column=4)
        self.snif = None

    def guardarIface(self):
        self.iface = self.cajaIface.get()
        print(self.iface)

    def guardar_n_pkts(self):
        self.n_pkts = int(self.caja_n_pkts.get())
        print(self.n_pkts)

    def guardar_todo(self):
        self.guardarIface()
        self.guardar_n_pkts()
        self.set_sniffer()
        self.set_tabla(ventana)

    def set_sniffer(self):
        self.snif = sniffer(self.iface, self.n_pkts)
        self.snif.sniff()
        self.snif.mostrar_general()
        self.lista = self.snif.formato()
        print(self.lista)
        total_rows = len(self.lista)
        total_columns = len(self.lista[0])
        print(total_rows)
        print(total_columns)

    def get_sniffer(self):
        return self.snif

    def set_tabla(self,ventana):
        total_rows = len(self.lista)
        total_columns = len(self.lista[0])
        self.tabla= Table(ventana, total_rows, total_columns,self.lista)

class Table: 
    def __init__(self,root, total_rows, total_columns,lst): 
          
        # code for creating table 
        for i in range(total_rows): 
            for j in range(total_columns): 
                  
                self.e = tkinter.Entry(root, width=20, fg='blue', 
                               font=('Arial',16,'bold')) 
                  
                self.e.grid(row=i+1, column=j)
                self.e.insert(tkinter.END, lst[i][j]) 

            self.boton = tkinter.Button(ventana, text="expandir "+str(i+1))
            self.boton.grid(row=i+1,column=j+1)

def main():
    i = ingreso(ventana)
    snif = i.get_sniffer()
    lst = sniffer.formato 
# find total number of rows and 
# columns in list 
    #total_rows = len(lst)
    #total_columns = len(lst[0])


    #t = Table(ventana, total_rows, total_columns,lst)
    ventana.mainloop()

if __name__ == '__main__':
    main()
