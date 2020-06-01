#!/usr/bin/env python
import scapy.all as scapy
import argparse


def get_interface():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--interface", dest="interface", help="Especifica el dispositivo para hacer sniffing")
    arguments = parser.parse_args()
    return arguments.interface

def sniff(iface):
    n = int(input('¿cuantos paquetes quiere obtener?'))
    pkts = scapy.sniff(iface = iface, count = n)
    return pkts

def mostrar_general(pkts):
    print('este es un resumen de los paquetes:\n')
    print(pkts)

def mostrar_individual(pkts,n):
    print(pkts[n].summary())

def main():
    iface = get_interface()
    pkts = sniff(iface)
    mostrar_general(pkts)
    band = 1
    while(band!=0):
        band = int(input('Desea ver un paquete en especifico? (1 o 0): '))
        n = int(input('digite el numero del paquete: '))
        mostrar_individual(pkts, n)
        
if __name__=="__main__":
    main()
