# Problema *
from __future__ import division
from aleatorio import random_autos_vendidos, random_tipo_autos,\
    random_tipo_autos_mediano, random_tipo_autos_lujo

def iniciar_simulacion(vendedores):
    print "----------------------------------------------------------------"
    print "------------------- Preparando la simulacion! ------------------"
    print "----------------------------------------------------------------"
    print "Parametros: "
    print "----------------------------------------------------------------"
    print "(a) vendedores %d" % (vendedores)
    print "----------------------------------------------------------------"
    print ""
    nro_autos = 0
    comision = [0] * vendedores
    
    print "----------------------------------------------------------------"
    print "------------------- Iniciando la simulacion! -------------------"
    print "----------------------------------------------------------------"
    print ""
    for i in range(vendedores):
        nro_autos = random_autos_vendidos()
    
        print "EL vendedor %d vendio %d carros: " % (i,nro_autos)
        for i in range(nro_autos):
            tipo_auto = random_tipo_autos()
            
            if tipo_auto == "Compacto":
                comision[i] = comision[i] + 250
    
            elif tipo_auto == "Mediano":
                comision_mediano = random_tipo_autos_mediano()
                comision[i] = comision[i] + comision_mediano
    
            elif tipo_auto == "Lujo":
                comision_lujo = random_tipo_autos_lujo()
                comision[i] = comision[i] + comision_lujo
    
        print "  Por una comision total de %d" % (comision[i])
    
    comision = sum(comision) / len(comision)
    print ""
    print "----------------------------------------------------------------"
    print "---------------- Se ha terminado la simulacion! ----------------"
    print "----------------------------------------------------------------"
    print "Analisis de resultados: "
    print "----------------------------------------------------------------"
    print "(a) La comision promedio de un vendedor es de : %d" % (comision)
    print "---------------------------------------------------------------- "
    print ""
    
    return comision

    
