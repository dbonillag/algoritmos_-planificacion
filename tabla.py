# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 13:13:57 2019

@author: Daniel Bonilla - Andres Llinas
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

        print("{: ^15s} {: ^15s} {: ^15s} {: ^15s} {: ^15s} {: ^15s}".format(
            "Proceso","Rafaga","Quantum","TiempoLlegada","ResiduoRafaga","Estado")
        )
        print(" ".join([("-" * 15)] * 6))

        for pr in self.procesos:
            print("{: ^15s} {: ^15s} {: ^15s} {: ^15s} {: ^15s} {: ^15s}".format(
                str(pr.pid),str(pr.rafaga), str(pr.quantum) , str(pr.tmp_llegada) , str(
                pr.residuo_rafaga),pr.estado)
            )

        



