#! /usr/bin/python
# -*- encoding: utf-8 -*-

from random import randint, uniform
from collections import deque
from math import modf, log, sqrt, fabs
import numpy as np


def generarTiempoTrabajo():
    return np.random.exponential(12)

def generarTiempoA():
    return np.random.uniform(6,10)
   
def generarTiempoB():
    return np.random.triangular(1,3,5)

def mean_confidence_interval(data, confidence=0.90):
    a = 1.0*np.array(data)
    n = len(a)
    m, se = np.nanmean(a), scipy.stats.sem(a, nan_policy='omit')
    h = se * sp.stats.t._ppf((1+confidence)/2., n-1)
    return m, m-h, m+h


def varianza(lis_data, promedio):
    suma = 0
    for i in range(len(lis_data)):
        suma += ((lis_data[i] - promedio)*(lis_data[i] - promedio))
    suma /= (len(lis_data))
    return suma

def error_90_prcnt (lis_data, promedio):
    varz = varianza(lis_data, promedio)
    nmuestra = len(lis_data)
    return (1.65*(sqrt(varz/nmuestra)))

def simulacion(tiempo_max):

    colaA = []
    colaB = []
    llegadas = []
    tiempo_fallo = 0
    terminacionA = 0
    terminacionB = 0
    tiempo_terminacion = 0
    terminados = 0
    tiempo = 0

    A_ocupado = 0
    B_ocupado = 0
    A_trabajando = False
    B_trabajando = False
    cantidad_trabajos = []

    acumulado = 0
    tiempo_iniciados = []
    tiempo_terminados = []
    while tiempo < tiempo_max :

        llegada = generarTiempoTrabajo()

        acumulado += llegada

        llegadas.append(acumulado)

        tiempo += 1

    tiempo = 0

    while tiempo < tiempo_max:
    
        if (len(llegadas) > 0 and llegadas[0] <= tiempo):
            colaA.append(0)

        A_ocupado-=1
        B_ocupado-=1


        if (A_ocupado <= 0 and not A_trabajando):
            if (len(colaA) > 0):
                esperaA = colaA.pop(0)
                tiempo_iniciados.append(esperaA)
                A_ocupado = generarTiempoA()
                A_trabajando = True
                terminacionA = esperaA + A_ocupado

        if (A_ocupado <= 0 and A_trabajando):
            if (len(colaB) < 4):
                colaB.append(0)
                A_trabajando = False
            else:
                tiempo_fallo +=1

        if (A_ocupado > 0 and A_trabajando):
            if (len(colaA) > 0):
                i = 0
                while (i < len(colaA)):
                    colaA[i]+=1
                    i+=1

        if (B_ocupado <= 0 and not B_trabajando):
            if (len(colaB) > 0):
                esperaB = colaB.pop(0)
                B_ocupado = generarTiempoB()
                B_trabajando = True
                terminacionB = esperaB + B_ocupado

        if (B_ocupado <= 0 and B_trabajando):
            terminados +=1
            tiempo_terminados.append(tiempo)
            B_trabajando = False

        if (B_ocupado > 0 and B_trabajando):
            if (len(colaB) > 0):
                i = 0
                while (i < len(colaB)):
                    colaB[i]+=1
                    i+=1

        tiempo_terminacion += terminacionA + terminacionB
        cantidad_trabajos.append(len(colaA) + len(colaB))
        tiempo += 1

    tiempo_iniciados1 = np.array(tiempo_iniciados[0:len(tiempo_terminados)])
    tiempo_terminados1 = np.array(tiempo_terminados)

    return cantidad_trabajos, tiempo_fallo, tiempo_terminados1 - tiempo_iniciados1, terminados #promedio_terminacion, terminados

tiempo_max = int(input('introduzca la cantidad de minutos: '))
cantidad_trabajos, tiempo_fallo, tiempo_terminados, terminados = simulacion(tiempo_max)

print('El numero esperado de trabajos en el taller: ',np.mean(cantidad_trabajos))
print('El porcentaje de tiempo que se para el centro A: '+ str(tiempo_fallo*100/tiempo_max) + '%')
print('El tiempo esperado de terminacion de un trabajo: ',np.mean(tiempo_terminados))#promedio_terminacion)
print('Trabajos terminados: ',terminados)


print("El promedio del tiempo de falla es: {}".format(np.mean(cantidad_trabajos)))

promedio_falla = np.mean(cantidad_trabajos)

intervalo_confianza = error_90_prcnt(cantidad_trabajos, promedio_falla)

print ("El intervalo de confianza del 90 por ciento es: (%f , %f)" % (promedio_falla - intervalo_confianza, promedio_falla + intervalo_confianza))
