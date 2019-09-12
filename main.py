# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 19:00:33 2019

@author: Daniel Bonilla - Andres Llinas
"""
import random

from proceso import Proceso
import algoritmos as alg

print("Ingrese la cantidad de procesos: ")
cantidad = int(input())
print("Ingrese el tiempo de ejecución de los procesos: \n")

print("Ingrese el quantum")
quantum=int(input())
procesos=[]

rafaga =list()
tiempos_de_llegada =list()
for i in range(cantidad):
    rafaga.append(random.randint(1,10))
    tiempos_de_llegada.append(random.randint(1,10))
    procesos.append(Proceso(i,rafaga[i],quantum,tiempos_de_llegada))

def menuAlgortimos(opcion):
    return {
        '3': alg.srtf(procesos),
    }.get(opcion, )

menuAlgortimos(input("Digite el numero del algoritmo que desea ejecutar \n1. FCFS\n2. SJF\n3. RR"))



