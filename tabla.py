# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 13:13:57 2019

@author: h
"""
from proceso import Proceso
import os
clear = lambda: os.system('cls')

class Tabla:

    def __init__(self,procesos):
        self.procesos=procesos
        

    def mostrar(self):
        clear()
        print("\n")
        print("Proceso\t Rafaga\t Quantum\t Tiempo de espera\t Residuo de rafaga\t Estado")
        
        for pr in self.procesos:
            print(str(pr.pid)+"\t\t"+str(pr.rafaga)+"\t\t"+str(pr.quantum)+"\t\t"+str(pr.tmp_esp)+"\t\t"+str(pr.residuo_rafaga)+"\t\t"+pr.estado)
            print("\n")  
    
