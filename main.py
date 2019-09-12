# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 19:00:33 2019

@author: Daniel Bonilla - Andres Llinas
"""
import os
import random

from proceso import Proceso
import algoritmos as alg

procesos = []

def iniciar_procesos(cant,quan):
    procesos.clear()
    rafaga = list()
    tiempos_de_llegada = list()
    for i in range(cant):
        rafaga.append(random.randint(1, 10))
        tiempos_de_llegada.append(random.randint(1, 10))
        procesos.append(Proceso(i, rafaga[i], quan, tiempos_de_llegada[i]))


def menu():
    """
    Función que limpia la pantalla y muestra nuevamente el menu
    """
    os.system('cls')
    print("Selecciona una opción")
    print("\t1 - Algoritmo FCFS")
    print("\t2 - Algortimo SJF")
    print("\t3 - Algortimo SRTF")
    print("\t4 - Algortimo Round Robin")
    print("\t9 - Cambiar # de procesos y Quantum")
    print("\t0 - salir")

print("Ingrese la cantidad de procesos: ")
cantidad = int(input())

print("Ingrese el quantum")
quantum=int(input())

while True:
    # Mostramos el menu
    menu()
    iniciar_procesos(cantidad,quantum)
    # solicituamos una opción al usuario
    opcionMenu = input("inserta un numero valor >> ")

    if opcionMenu == "1":
        print("")
        input("Has seleccionado FCFS...\npulsa una tecla para continuar")
        alg.fcfs(procesos)
    elif opcionMenu == "2":
        print("")
        input("Has seleccionado SJF...\npulsa una tecla para continuar")
        alg.sjf(procesos)
    elif opcionMenu == "3":
        print("")
        input("Has seleccionado SRTF...\npulsa una tecla para continuar")
        alg.srtf(procesos)
    elif opcionMenu == "4":
        print("")
        input("Has seleccionado Round Robin...\npulsa una tecla para continuar")
        alg.round_robin(procesos)
    elif opcionMenu == "9":
        print("")
        cantidad = int(input("Ingrese la cantidad de procesos: "))
        quantum = int(input("Ingrese el quantum"))
        iniciar_procesos(cantidad,quantum)
    elif opcionMenu == "0":
        break
    else:
        print("")
        input("No has pulsado ninguna opción correcta...\npulsa una tecla para continuar")




