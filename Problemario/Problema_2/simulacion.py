from cajero import Cajero
from cliente import Cliente
from probabilidades import tiempo_llegada_cliente, tiempo_servicio_cajero, probabilidad_declinar, proximo_evento


def Simular(tiempo_laborable, numero_servidores):
    tiempo_transcurrido = 0
    clientes_declinaron = 0
    cajeros = numero_servidores * [Cajero()]
    personas_atendidas = []
    
    cajero_1, cajero_2, cajero_3, cajero_4 = [], [], [], []
    colas = [cajero_1, cajero_2, cajero_3, cajero_4]
    
    proxima_llegada = tiempo_llegada_cliente()


    for i in range(numero_servidores):
        cajeros[i] = Cajero()
        

    while tiempo_transcurrido < tiempo_laborable or len(colas[0]) > 0 or len(colas[1]) > 0 or len(colas[2]) > 0 or len(colas[3]) > 0:
        proxima_actividad = proximo_evento(proxima_llegada, cajeros)
        tiempo_transcurrido += proxima_actividad
        proxima_llegada -= proxima_actividad    
        
        if proxima_llegada == 0:
            cajero_seleccionado = Cajero.seleccionar_cajero(colas, cajeros)
            #cajero esta desocupado
            if cajeros[cajero_seleccionado].cliente_atendido is None:
                cajeros[cajero_seleccionado].tiempo_servicio = tiempo_servicio_cajero()
                cajeros[cajero_seleccionado].cliente_atendido = Cliente()
                cajeros[cajero_seleccionado].disponible = False
                cajeros[cajero_seleccionado].recien_asignado = True
            #se encola a la persona
            elif len(colas[cajero_seleccionado]) < 6:
                colas[cajero_seleccionado].append(Cliente())
            #la cola es mayor a 6 y se debe ver si el cliente declina
            else:
                clientes_declinaron = probabilidad_declinar(colas[cajero_seleccionado], clientes_declinaron, personas_atendidas)
            
            proxima_llegada = tiempo_llegada_cliente()
        
        for i in range(numero_servidores):
            if cajeros[i].tiempo_servicio > 0 and not cajeros[i].disponible:
                if cajeros[i].recien_asignado:
                    cajeros[i].recien_asignado = False
                else:
                    cajeros[i].tiempo_servicio -= proxima_actividad
                    cajeros[i].tiempo_servicio_total += proxima_actividad
                    cajeros[i].cliente_atendido.tiempo_en_sistema += proxima_actividad
                    #se desocupa un cajero
                    if cajeros[i].tiempo_servicio == 0:
                        #se revisa si hay personas por atender en la cola de la caja
                        if len(colas[i]) > 0:
                            personas_atendidas.append(cajeros[i].cliente_atendido)
                            cajeros[i].cliente_atendido = colas[i].pop()
                            cajeros[i].tiempo_servicio = tiempo_servicio_cajero()
                            cajeros[i].disponible = False
                        else:
                            personas_atendidas.append(cajeros[i].cliente_atendido)
                            cajeros[i].cliente_atendido = None
                            cajeros[i].disponible = True
            
        for cola in colas:
            for cliente in cola:
                cliente.tiempo_en_sistema += proxima_actividad

        
    porcentaje_clientes_declinaron = (clientes_declinaron * 100) / len(personas_atendidas)
    tiempo_espera_cliente = Cliente.tiempo_promedio_espera(personas_atendidas)
        
        
    tiempo_total = [0]*4
    for i in range(numero_servidores):
        tiempo_total[i] = tiempo_transcurrido - cajeros[i].tiempo_servicio_total
        tiempo_total[i] = tiempo_total[i] * 100 / tiempo_transcurrido
        
        
    return [porcentaje_clientes_declinaron, tiempo_espera_cliente, tiempo_total]