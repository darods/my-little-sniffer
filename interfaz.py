#!/usr/bin/env python
import tkinter
from sniffer import sniffer

ventana = tkinter.Tk()
ventana.title('My Litle Sniffer')
class ingreso:
    def __init__(self,ventana):
        self.cajaIface = tkinter.Entry(ventana)
        self.caja_n_pkts = tkinter.Entry(ventana)
        
        self.nombres = tkinter.Label(ventana, text = 'hecho por: Daniel Rodriguez, Valentina Tobo y Jordy Pineda')
        self.etiquetaIface = tkinter.Label(ventana, text = "red: ")
        self.etiqueta_n_pkts = tkinter.Label(ventana, text = "numero de paquetes: ")
        self.botonIngresar = tkinter.Button(ventana, text="ingresar", command = self.guardar_todo) 
        
        self.nombres.grid(row = 0, column=0, columnspan=4)
        self.etiquetaIface.grid(row=1,column=0)
        self.cajaIface.grid(row=1, column=1)
        self.etiqueta_n_pkts.grid(row=1,column=2)
        self.caja_n_pkts.grid(row=1, column=3)
        self.botonIngresar.grid(row=1, column=4)
        self.snif = None

    def guardarIface(self):
        self.iface = self.cajaIface.get()

    def guardar_n_pkts(self):
        self.n_pkts = int(self.caja_n_pkts.get())

    def guardar_todo(self):
        self.guardarIface()
        self.guardar_n_pkts()
        self.set_sniffer()
        self.set_tabla(ventana)

    def set_sniffer(self):
        self.snif = sniffer(self.iface, self.n_pkts)
        self.snif.sniff()
        self.lista = self.snif.formato()

    def set_tabla(self,ventana):
        total_rows = len(self.lista)
        total_columns = len(self.lista[0])
        self.tabla= Table(ventana, total_rows, total_columns,self.lista, self.snif)
    

class Table: 
    def __init__(self,root, total_rows, total_columns,lst, sniffer): 
          
        self.e_fuente = tkinter.Label(ventana, text = "fuente")
        self.e_dst = tkinter.Label(ventana, text = "destino")
        self.e_info = tkinter.Label(ventana, text = "mas detalles")
        self.e_pdf = tkinter.Label(ventana, text = "explicacion")


        self.e_fuente.grid(row=2,column=0)
        self.e_dst.grid(row=2,column=1)
        self.e_info.grid(row=2,column=2)
        self.e_pdf.grid(row=2,column=3)
        # code for creating table 
        for i in range(total_rows): 
            for j in range(total_columns): 
                  
                self.e = tkinter.Entry(root, width=20, fg='blue', 
                               font=('Arial',16)) 
                  
                self.e.grid(row=i+3, column=j)
                self.e.insert(tkinter.END, lst[i][j]) 

            self.boton = tkinter.Button(ventana, text="mas sobre el paquete "+str(i+1), command = lambda idx = i: sniffer.mostrar_individual(idx,root))
            self.boton2 = tkinter.Button(ventana, text="explicación paquete ", command= lambda idx = i: sniffer.grafico_pdf(idx))
            self.boton.grid(row=i+3,column=j+1)
            self.boton2.grid(row=i+3,column=j+2)

def main():
    i = ingreso(ventana)
    ventana.mainloop()

if __name__ == '__main__':
    main()
