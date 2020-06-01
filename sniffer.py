#!/usr/bin/env python
# -*- coding: utf-8 -*-:w

import scapy.all as scapy
import tkinter
from scapy.all import *
class sniffer:
    def __init__(self, iface, n):
        self.iface = iface
        self.n = n
    
    def sniff(self):
        self.pkts = sniff(iface = self.iface, count = self.n)
        return self.pkts
    
    def mostrar_general(self):
        print('este es un resumen de los paquetes:\n')
        print(self.pkts)

    def mostrar_individual(self,n,root):
        window = tkinter.Toplevel(root)
        label = tkinter.Label(window, text =self.pkts[n].summary())
        label.pack()
    
    def grafico_pdf(self,n):
        self.pkts[n].pdfdump()

    def formato(self):
        claves=[]
        for i in range (self.n):
            info = [self.pkts[i].src, self.pkts[i].dst]
            claves.append(info)
        return claves
    

'''
prueba en interfaz de las funciones de la clase
def main():
    n=4
    snif = sniffer('enp4s0f2',n)
    snif.sniff()
    snif.mostrar_general()
    print('resumen individual\n')
    for i in range (n):
        snif.mostrar_individual(i)
    
    print(snif.formato())



if __name__=="__main__":
    main()
'''
