# *** coding: utf*8 ***
from simulacion import iniciar_simulacion
import math

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

def problema(numero_simulaciones=1):

    print ""
    print "********************************** Problema 7 **********************************"
    print ""

    diasMax = 360
    Q = 100
    reorden = 0
    costoPorUnidad = 0

    print "------------------- Preparando la simulacion! ------------------"
    print "Parametros: "
    print "(a) diasMax %d" % (diasMax)
    print "(b) reordenCota %d" % (Q)
    print ""

    print "------------------- Iniciando la simulacion! -------------------"
    print ""

    reordenArray = []
    costoPorUnidadArray = []

    for i in range(numero_simulaciones):
        result = iniciar_simulacion(diasMax,Q)

        reorden += result[0]
        reordenArray.append(result[0])
        costoPorUnidad += result[1]
        costoPorUnidadArray.append(result[1])

    mediaReorden = reorden/numero_simulaciones
    mediaCostoPorUnidad = costoPorUnidad/numero_simulaciones
    m_error_90Reorden = error_90_prcnt( reordenArray, mediaReorden)
    m_error_90RostoPorUnidad = error_90_prcnt( costoPorUnidadArray, mediaCostoPorUnidad)

    print "---------------- Se ha terminado la simulacion! ----------------"
    print "Analisis de resultados: "
    print "(a) El punto de reorden optimo es %d unidades con costo $%d " % (mediaReorden, mediaCostoPorUnidad)
    print ""

    print "Intervalo de Confianza: "
    print ""
    print "El intervalo de confianza de 90 por ciento del punto de reorden optimo esta entre (%f , %f)" % (mediaReorden-m_error_90Reorden,mediaReorden+m_error_90Reorden)
    print "El intervalo de confianza de 90 por ciento de las unidades de costo esta entre (%f , %f)" % (mediaCostoPorUnidad-m_error_90RostoPorUnidad,mediaCostoPorUnidad+m_error_90RostoPorUnidad)
    print ""

if __name__ == "__main__":
    aux = int(input("Ingrese el numero de simulaciones a realizar: "))
    problema(aux)
