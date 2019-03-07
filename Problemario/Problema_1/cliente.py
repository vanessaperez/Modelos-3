class Cliente():
    def __init__(self):
        self.tiempo_en_sistema = 0
        
    @staticmethod
    def tiempo_promedio_espera(clientes):
        res = 0
        
        for cliente in clientes:
            res += cliente.tiempo_en_sistema
        return res / len(clientes)
