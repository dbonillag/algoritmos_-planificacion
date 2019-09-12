# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 18:54:19 2019
Descripción algoritmos de planificación utilizados por el sistema operativo para
la gestión de procesos
@author: Daniel

"""
from tabla import Tabla
from proceso import Proceso
import time as tm



def FCFS(procesos):     
    tb=Tabla(procesos)
    for proceso in procesos:
        proceso.estado="EJECUTANDO"
        while(proceso.residuo_rafaga>0):
            
            proceso.residuo_rafaga-=1
            tm.sleep(1)
            tb.mostrar()
            
        proceso.estado="TERMINADO"
    
def SJF(procesos):  
    
    procesos.sort(key=lambda proceso: proceso.rafaga)
    
    tb=Tabla(procesos)
    
    
    for proceso in procesos:
        proceso.estado="EJECUTANDO"
        while(proceso.residuo_rafaga>0):
            
            proceso.residuo_rafaga-=1
            tm.sleep(1)
            tb.mostrar()
            
        proceso.estado="TERMINADO"
