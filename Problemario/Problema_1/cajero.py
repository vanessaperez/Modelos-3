import Queue as Cola


class Cajero():
    def __init__(self):
        self.disponible = True
        self.cola_clientes = Cola.Queue()
        self.tiempo_servicio = 0
        self.tiempo_servicio_total = 0
        self.recien_asignado = False
        self.cliente_atendido = None
    
    @staticmethod    
    def tiempo_servicio_cajeros(lista_cajeros):
        lista = []
        
        for i in range(len(lista_cajeros)):
            if not lista_cajeros[i].disponible:
                lista.append(lista_cajeros[i].tiempo_servicio)
        return lista

    @staticmethod
    def existe_cajero_disponible(lista_cajeros):
        for i in range(len(lista_cajeros)):
            if lista_cajeros[i].disponible:
                return True
        return False
        
