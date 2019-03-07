# coding=utf-
import Queue


class Cajero():
    def __init__(self):
        self.disponible = True
        self.tiempo_servicio = 0
        self.tiempo_servicio_total = 0
        self.recien_asignado = False
        self.cliente_atendido = None

    #Retorna el número de caja con menor cola
    @staticmethod
    def seleccionar_cajero(colas, cajeros):
        cajero_menos_cola = colas[0]
        numero_cajero = 0
        
        for i in range(len(cajeros)):
            if len(cajero_menos_cola) > len(colas[i]):
                cajero_menos_cola = colas[i]
                numero_cajero = i
            elif len(cajero_menos_cola) == len(colas[i]) and cajeros[i].cliente_atendido is None and \
                 cajeros[numero_cajero].cliente_atendido is not None:
                cajero_menos_cola = colas[i]
                numero_cajero = i
        return numero_cajero

    @staticmethod
    def tiempo_servicio_cajeros(lista_cajeros):
        tiempo_cajeros = []
        for i in range(len(lista_cajeros)):
            if not lista_cajeros[i].disponible:
                tiempo_cajeros.append(lista_cajeros[i].tiempo_servicio)
        return tiempo_cajeros
    
    @staticmethod
    def cajeros_disponibles(lista):
        for servidor in lista:
            if not servidor.disponible:
                return False
        return True