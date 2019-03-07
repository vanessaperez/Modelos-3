#!/usr/bin/env python3
# -*- encoding: utf-8 -*-


from scipy.stats import poisson
from numpy.random import uniform
from numpy.random import exponential
from numpy.random import choice
import scipy as sp
import scipy.stats
import math


import numpy as np


"""
Extraído de https://stackoverflow.com/a/15034143
"""

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
    return (1.65*(math.sqrt(varz/nmuestra)))  



'''
Función que determina el tiempo de reparación de
una máquina cuando ésta se daña. Los tiempos de
reparación son variables aleatorias independientes 
con una función de distribución: G(x) = 1 − e^(− 2x)
'''
def generar_tiempo_reparacion():

	aleatorio = uniform(low=0, high=1)
	return -np.log((1 - aleatorio))/2
	

'''
Función que determina el tiempo que funciona una máquina
hasta descomponerse. El tiempo es una variable aleatoria,
con función de distribución (acumulada): F(x) = 1 − e^(−x)
'''

def generar_tiempo_trabajo():

	aleatorio = uniform(low=0, high=1)
	return -np.log((1 - aleatorio))


class Maquina :
    
    def __init__(self) :
        self.sirve = True
        self.reparado = False
        self.vida_util = 0
        self.tiempo_reparacion = 0


n_maquinas_trabajar = 4
s_maquinas_repuesto = 3

cola_taller = []

cola_repuestos = []

cola_trabajando = []

max_tiempo = 1000
tiempos_falla = []
paso = 0.01
n_max_experimentos = 100

for experimento in range(n_max_experimentos):
    
    # Inicializar experimento
    
    tiempo = 0
    
    for i in range(n_maquinas_trabajar):
        maquina = Maquina()
        maquina.vida_util = generar_tiempo_trabajo()
        #print(maquina.vida_util)
        cola_trabajando.append(maquina)

    for i in range(s_maquinas_repuesto):
        maquina = Maquina()
        maquina.vida_util = generar_tiempo_trabajo()
        cola_repuestos.append(maquina)
    
    # Correr experimento
    
    while tiempo < max_tiempo :
        
        for maquina in cola_trabajando:
            
            # Determinar si una máquina se ha dañado
            if maquina.vida_util <= 0 :
                
                # mandar al taller
                maquina.sirve = False
                maquina.tiempo_reparacion = generar_tiempo_reparacion()
                cola_taller.append(maquina)
            
            else :
                
                # se disminuye la vida útil
                maquina.vida_util -= paso
                
        # Sacar las máquinas dañadas
        #Filtrar las máquinas que sirven de la cola_trabajando
        cola_trabajando = list(filter(lambda x : x.sirve, cola_trabajando))
        
            
        # reponer si es necesario
        while len(cola_trabajando) < n_maquinas_trabajar :
            if len(cola_repuestos) > 0 :
                cola_trabajando.append(cola_repuestos.pop(0))
            else :
                break
                
        # Determinar si hay falla
        if (len(cola_repuestos) == 0) and (len(cola_trabajando) < n_maquinas_trabajar) :
            tiempos_falla.append(tiempo)
            #print("Experimento: {}. Hubo falla en el tiempo: {}".format(experimento,tiempo))
            break
        
        # ver si está listo en el taller
        if len(cola_taller) > 0 and cola_taller[0].tiempo_reparacion <= 0 :
            cola_repuestos.append(cola_taller.pop(0))
        elif len(cola_taller) > 0 :
            cola_taller[0].tiempo_reparacion -= paso
        
        tiempo += paso
            

print("El promedio del tiempo de falla es: {}".format(np.mean(tiempos_falla)))

promedio_falla = np.mean(tiempos_falla)

intervalo_confianza = error_90_prcnt(tiempos_falla, promedio_falla)

print ("El intervalo de confianza del 90 por ciento es: (%f , %f)" % (promedio_falla - intervalo_confianza, promedio_falla + intervalo_confianza))
