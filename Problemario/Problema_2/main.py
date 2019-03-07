# coding=utf-8
from simulacion import Simular
import numpy
from scipy.stats import sem, t
import scipy.stats
import math


def varianza( lis_data, promedio ):
    suma = 0
    for i in range(len(lis_data)):
        suma += ((lis_data[i] - promedio)*(lis_data[i] - promedio))
    suma /= (len(lis_data))
    return suma

def error_90_prcnt (lis_data, promedio):
    varz = varianza( lis_data, promedio )
    nmuestra = len(lis_data)
    return (1.65*(math.sqrt(varz/nmuestra)))
    

def problema_2(numero_simulaciones):
    
    tiempo = 480  #minutos que hay en 8 horas
    numero_servidores = 4
    declinaron = []
    esperanza = []
    promedio_declinaron = 0
    promedio_esperanza = 0
    promedio_cajero_1 = 0
    promedio_cajero_2 = 0
    promedio_cajero_3 = 0
    promedio_cajero_4 = 0
    cajero_1 = []
    cajero_2 = []
    cajero_3 = []
    cajero_4 = []
    
    for i in range(numero_simulaciones):
        simulacion = Simular(tiempo, numero_servidores)
        declinaron.append(simulacion[0])
        esperanza.append(simulacion[1])
        promedio_declinaron += simulacion[0]
        promedio_esperanza += simulacion[1]
        cajero_1.append(simulacion[2][0])
        cajero_2.append(simulacion[2][1])
        cajero_3.append(simulacion[2][2])
        cajero_4.append(simulacion[2][3])
        promedio_cajero_1 += simulacion[2][0]
        promedio_cajero_2 += simulacion[2][1]
        promedio_cajero_3 += simulacion[2][2]
        promedio_cajero_4 += simulacion[2][3]
        
        
    promedio_declinaron = promedio_declinaron / numero_simulaciones
    promedio_esperanza = promedio_esperanza / numero_simulaciones


    m_error_90_esp = error_90_prcnt(esperanza, promedio_esperanza)
    
    print "(a) El tiempo promedio que un cliente pasa en el sistema es: %0.2f" % (promedio_esperanza)
    print "    El intervalo de confianza de 90 por ciento de la espera esta entre %0.4f y %0.4f" % (promedio_esperanza-m_error_90_esp,promedio_esperanza+m_error_90_esp)

    m_error_90_decl = error_90_prcnt(declinaron, promedio_declinaron)

    print ""
    print "(b)El promedio de porcentaje de los clientes que declinaron es: %0.2f" % (promedio_declinaron)
    print "   El intervalo de confianza de 90 por ciento de declinar esta entre %f y %f" % (promedio_declinaron-m_error_90_decl,promedio_declinaron+m_error_90_decl)

    promedio_cajero_1 = promedio_cajero_1 / numero_simulaciones 
    promedio_cajero_2 = promedio_cajero_2 / numero_simulaciones
    promedio_cajero_3 = promedio_cajero_3 / numero_simulaciones
    promedio_cajero_4 = promedio_cajero_4 / numero_simulaciones

    m_error_90_cajero_1 = error_90_prcnt(cajero_1, promedio_cajero_1)
    m_error_90_cajero_2 = error_90_prcnt(cajero_2, promedio_cajero_2)
    m_error_90_cajero_3 = error_90_prcnt(cajero_3, promedio_cajero_3)
    m_error_90_cajero_4 = error_90_prcnt(cajero_4, promedio_cajero_4)

    print ""
    print "(c) El promedio e intervalo de confianza de 90 por ciento del tiempo desocupado del :"
    print "    *primer cajero: (%f,%f)" % (promedio_cajero_1 - m_error_90_cajero_1, promedio_cajero_1 + m_error_90_cajero_1 )
    print "     promedio: %f" %promedio_cajero_1
    print "    *segundo cajero: (%f,%f)" % (promedio_cajero_2 - m_error_90_cajero_2, promedio_cajero_2 + m_error_90_cajero_2 )
    print "     promedio: %f" % promedio_cajero_2
    print "    *tercer cajero: (%f,%f)" % (promedio_cajero_3 - m_error_90_cajero_3, promedio_cajero_3 + m_error_90_cajero_3 )
    print "     promedio: %f" % promedio_cajero_3
    print "    *cuarto cajero: (%f,%f)" % (promedio_cajero_4 - m_error_90_cajero_4, promedio_cajero_4 + m_error_90_cajero_4 )
    print "     promedio: %f" % promedio_cajero_4
