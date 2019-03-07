#!/usr/bin/env python3

import numpy as np
from numpy.random import choice
import math


def generar_demanda_diaria() :
    
    return choice([12,13,14,15,16,17],
                  p = [0.05,0.15,0.25,0.35,0.15,0.05])
                  
def generar_tiempo_entrega() :
    
    return choice([1,2,3,4],
                  p = [0.2,0.3,0.35,0.15])

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

R = 100
Q = 100

# $ / (producto * día)
costo_inventario = 0.2

# $ / (producto * día)
costo_escasez = 1

# $ / pedido
costo_pedido = 10

tiempo_max = 10
paso = 1

for R in range(Q) :
    
    tiempo = 0
    escasez = 0
    # guarda los tiempos
    por_entregar = []
    arreglo_costo = []
    # E(costo_total_inventario) + E(costo_total_pedidos) + E(costo_total_escasez)
    costo_total = 0
    costoPorUnidad = 0

    productos_en_almacen = Q

    while tiempo < tiempo_max :
        
        demanda = generar_demanda_diaria()
        
        # Si los productos en almacen no cubren la demanda
        if productos_en_almacen < demanda :
            productos_en_almacen = 0
            
            # la escasez se acumula
            escasez = escasez + demanda - productos_en_almacen
        else :
            productos_en_almacen -= demanda
        
        # Si se alcanza el punto de reorden
        hay_pedido = 0
        if productos_en_almacen <= R :
            tiempo_de_entrega = generar_tiempo_entrega()
            hay_pedido = 1
            por_entregar = por_entregar + ( [tiempo_de_entrega] * Q )
        
        # Si la entrega llega
        entrega = len(list(filter(lambda x : x <= 0, por_entregar)))
        por_entrega = list(filter(lambda x : x > 0, por_entregar))
        
        productos_en_almacen += entrega
        
        costo_total = productos_en_almacen*costo_inventario + escasez*costo_escasez + hay_pedido*costo_pedido
        arreglo_costo.append(costo_total)
        
        tiempo += paso
        # print(tiempo)

    print("El costo total para R={} es: {} $".format(R,costo_total))

    for i in range(len(arreglo_costo)): costoPorUnidad += arreglo_costo[i]
    mediaCostoPorUnidad = costoPorUnidad/tiempo_max
    m_error_90RostoPorUnidad = error_90_prcnt(arreglo_costo, mediaCostoPorUnidad)
    print("Intervalo de Confianza: ")
    print("")
    print("El intervalo de confianza de 90 por ciento de las unidades de costo esta entre (%f , %f)" % (mediaCostoPorUnidad-m_error_90RostoPorUnidad,mediaCostoPorUnidad+m_error_90RostoPorUnidad))