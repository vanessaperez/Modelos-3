import random
import numpy 
from cajero import Cajero
from cliente import Cliente


def tiempo_llegada_cliente():
    return numpy.random.exponential(scale=1)
   
   
def tiempo_servicio_cajero():
    return numpy.random.uniform(3, 5)
    
    
def probabilidad_declinar(cola_clientes, clientes_declinaron, personas_atendidas):
    probabilidad = random.random()

    if 6 <= len(cola_clientes) <= 8:
        if probabilidad <= 0.2:
            clientes_declinaron += 1
            personas_atendidas.append(Cliente())
        else:
            cola_clientes.append(Cliente())
    elif 9 <= len(cola_clientes) <= 10:
        if probabilidad <= 0.4:
            clientes_declinaron += 1
            personas_atendidas.append(Cliente())
        else:
            cola_clientes.append(Cliente())
    elif 11 <= len(cola_clientes) <= 14:
        if probabilidad <= 0.6:
            clientes_declinaron += 1
            personas_atendidas.append(Cliente())
        else:
            cola_clientes.append(Cliente())
    elif len(cola_clientes) >= 15:
        if probabilidad <= 0.8:
            clientes_declinaron += 1
            personas_atendidas.append(Cliente())
        else:
            cola_clientes.append(Cliente())
    
    return clientes_declinaron
    
    
def proximo_evento(proxima_llegada, lista_cajeros):
    cajeros_activos = Cajero.tiempo_servicio_cajeros(lista_cajeros)

    if len(cajeros_activos) > 0 and proxima_llegada is not None:
        if proxima_llegada <= min(cajeros_activos):
            return proxima_llegada
        elif proxima_llegada > min(cajeros_activos):
            return min(cajeros_activos)
    elif proxima_llegada is None:
        return min(cajeros_activos)
    else:
        return proxima_llegada



