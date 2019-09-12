# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 19:00:33 2019

@author: h
"""
from proceso import Proceso
import algoritmos as alg

print("Ingrese la cantidad de procesos: ")
cantidad = int(input())
print("Ingrese el tiempo de ejecución de los procesos: \n")
rafaga=list(map(int, input().split()))
print("Ingrese el quantum")
quantum=int(input())
procesos=[]

for i in range(cantidad):
    procesos.append(Proceso(i,rafaga[i],quantum))
    
alg.SJF(procesos)


