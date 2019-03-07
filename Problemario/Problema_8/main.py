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

def problema(numero_simulaciones):
    
    print "********************************** Problema 8 **********************************"
    print ""
    
    vendedores = 5
    promedio = 0
    ventasArray = []
    
    for i in range(numero_simulaciones):
        x = iniciar_simulacion(vendedores)
        ventasArray.append(x)
        promedio += x
    
    promedio /= numero_simulaciones
        
    m_error_90 = error_90_prcnt(ventasArray, promedio)
    
    print ""
    print "El promedio de ventas TOTAL es: %f" % (promedio)
    
    print "El intervalo de confianza de 90 por ciento esta entre %f y %f" % (promedio-m_error_90,promedio+m_error_90)
    print ""

if __name__ == "__main__":
    aux = int(input("Ingrese el numero de simulaciones a realizar: "))
    problema(aux)
