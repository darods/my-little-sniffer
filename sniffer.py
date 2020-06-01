#!/usr/bin/env python
# -*- coding: utf-8 -*-:w

import scapy.all as scapy

class sniffer:
    def __init__(self, iface, n):
        self.iface = iface
        self.n = n
    
    def sniff(self):
        self.pkts = scapy.sniff(iface = self.iface, count = self.n)
        return self.pkts
    
    def mostrar_general(self):
        print('este es un resumen de los paquetes:\n')
        print(self.pkts)

    def mostrar_individual(self,n):
        print(self.pkts[n].summary())
    
    def formato(self):
        claves=[]
        for i in range (self.n):
            info = [self.pkts[i].src, self.pkts[i].dst]
            claves.append(info)
        return claves


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
