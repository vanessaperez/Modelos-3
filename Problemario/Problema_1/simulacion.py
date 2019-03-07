import Queue as Cola
from cajero import Cajero
from cliente import Cliente
from probabilidades import tiempo_llegada_cliente, tiempo_servicio_cajero, probabilidad_declinar, llegada_cliente


def Simular(tiempo_laborable, numero_servidores):
    tiempo_transcurrido = 0
    clientes_declinaron = 0
    personas_atendidas = []
    cola_clientes = Cola.Queue()
    cajeros = numero_servidores * [Cajero()]
    proxima_llegada = tiempo_llegada_cliente()
    clientes_en_cola = []


    for i in range(numero_servidores):
        cajeros[i] = Cajero()
        

    while tiempo_transcurrido < tiempo_laborable or cola_clientes.qsize() > 0:
        tiempo_para_ser_atendido = llegada_cliente(proxima_llegada, cajeros)
        tiempo_transcurrido += tiempo_para_ser_atendido
        proxima_llegada -= tiempo_para_ser_atendido  
        
        if proxima_llegada == 0:
            if cola_clientes.empty() and Cajero.existe_cajero_disponible(cajeros):
                for cajero in cajeros:
                    if cajero.disponible:
                        cajero.tiempo_servicio = tiempo_servicio_cajero()
                        cajero.cliente_atendido = Cliente() 
                        cajero.disponible = False
                        cajero.recien_asignado = True 
                        break
            else:
                if cola_clientes.qsize() < 6:
                    cola_clientes.put(Cliente())
                    clientes_en_cola.append(Cliente())
                else: 
                    clientes_declinaron = probabilidad_declinar(cola_clientes, clientes_declinaron, personas_atendidas, clientes_en_cola)
            
            proxima_llegada = tiempo_llegada_cliente()    
            
        for cajero in cajeros:
            if cajero.tiempo_servicio > 0:
                if cajero.recien_asignado:
                    cajero.recien_asignado = False
                else:
                    cajero.tiempo_servicio -= tiempo_para_ser_atendido
                    cajero.tiempo_servicio_total += tiempo_para_ser_atendido
                    cajero.cliente_atendido.tiempo_en_sistema += tiempo_para_ser_atendido
                    
                    if cajero.tiempo_servicio == 0:
                        if cola_clientes.qsize() > 0:
                            personas_atendidas.append(cajero.cliente_atendido)
                            cajero.cliente_atendido = cola_clientes.get()
                            cajero.tiempo_servicio = tiempo_servicio_cajero()
                            cajero.cliente_atendido.tiempo_en_sistema = clientes_en_cola.pop().tiempo_en_sistema
                        else:
                            personas_atendidas.append(cajero.cliente_atendido)
                            cajero.cliente_atendido = None
                            cajero.disponible = True
      
      
        for cliente in clientes_en_cola:
            cliente.tiempo_en_sistema += tiempo_para_ser_atendido


    porcentaje_clientes_declinaron = (clientes_declinaron * 100) / len(personas_atendidas)
    tiempo_espera_cliente = Cliente.tiempo_promedio_espera(personas_atendidas)


    tiempo_total = [0]*4
    for i in range(numero_servidores):
        tiempo_total[i] = tiempo_transcurrido - cajeros[i].tiempo_servicio_total
        tiempo_total[i] = tiempo_total[i] * 100 / tiempo_transcurrido

    
    return [porcentaje_clientes_declinaron, tiempo_espera_cliente, tiempo_total]
