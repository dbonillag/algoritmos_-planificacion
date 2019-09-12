# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 18:54:19 2019
Descripción algoritmos de planificación utilizados por el sistema operativo para
la gestión de procesos
@author: Daniel Bonilla - Andres Llinas
"""
import proceso
from tabla import Tabla
from proceso import Proceso
import time as tm


def fcfs(procesos):
    tb = Tabla(procesos)
    for proceso in procesos:
        proceso.estado = "EJECUTANDO"
        while (proceso.residuo_rafaga > 0):
            proceso.residuo_rafaga -= 1
            tm.sleep(1)
            tb.mostrar()

        proceso.estado = "TERMINADO"
    tb.mostrar()


def sjf(procesos):
    procesos.sort(key=lambda proceso: proceso.rafaga)
    tb = Tabla(procesos)
    for proceso in procesos:
        proceso.estado = "EJECUTANDO"
        while (proceso.residuo_rafaga > 0):
            proceso.residuo_rafaga -= 1
            tm.sleep(1)
            tb.mostrar()
        proceso.estado = "TERMINADO"
    tb.mostrar()


def srtf(procesos):

    tb=Tabla(procesos)
    while (len(procesos)>0):
        procesoEjecutandose = procesos.pop(0)
        procesoEjecutandose.estado = "EJECUTANDO"
        if procesoEjecutandose.residuo_rafaga > 0:
            tm.sleep(1)
            if procesoEjecutandose.residuo_rafaga > procesoEjecutandose.quantum:
                procesoEjecutandose.residuo_rafaga = procesoEjecutandose.residuo_rafaga - procesoEjecutandose.quantum
            else:
                procesoEjecutandose.residuo_rafaga = 0;
            tb.mostrar()
            flag = procesoEjecutandose.residuo_rafaga
            if flag:
                procesoEjecutandose.estado="ESPERA"
                procesos.append(procesoEjecutandose)
                procesos.sort(key=lambda proceso: proceso.residuo_rafaga)
        tb.mostrar()
    tb.mostrar()




def round_robin(procesos):

    tb=Tabla(procesos)
    while (len(procesos)>0):
        procesoEjecutandose = procesos.pop(0)
        procesoEjecutandose.estado = "EJECUTANDO"
        if procesoEjecutandose.residuo_rafaga > 0:
            tm.sleep(1)
            if procesoEjecutandose.residuo_rafaga > procesoEjecutandose.quantum:
                procesoEjecutandose.residuo_rafaga = procesoEjecutandose.residuo_rafaga - procesoEjecutandose.quantum
            else:
                procesoEjecutandose.residuo_rafaga = 0;
            tb.mostrar()
            flag = procesoEjecutandose.residuo_rafaga
            if flag:
                procesoEjecutandose.estado = "ESPERA"
                procesos.append(procesoEjecutandose)
        tb.mostrar()
    tb.mostrar()

