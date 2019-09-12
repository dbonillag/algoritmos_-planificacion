# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 19:01:25 2019

@author: Daniel Bonilla - Andres Llinas
"""

class Proceso:
    
    def __init__(self,pid,rafaga,quantum,tiempo_llegada):
        self.pid=pid
        self.rafaga=rafaga
        self.quantum=quantum
        self.residuo_rafaga=rafaga
        self.tiempo_llegada=0
        self.tmp_esp=0
        self.estado="ESPERA"
    
   