import numpy as np
from scipy.stats import norm

class Pasajero:
	def __init__(self, embarque):
		self.estacion_embarque = embarque
		self.estacion_desembarque = generar_estaciones(embarque+1)+embarque

class Estacion : 
    def __init__(self,ident) :
        self.id = ident
        self.pasajeros_embarcados = []
        self.pasajeros_desembarcados = []
        self.tiempo_llegada = 0.0
        self.tiempo_salida = 0.0

def tiempo_recorrido(Npas) :
    return 100 * ( 1 + 0.1 * np.log(Npas) )

def tiempo_desembarque(Ndes, Nemb) :
    return 20 * ( 1 + 0.1 * np.log(Ndes + Nemb) )

def generar_estaciones(est_entrada) :
    Nder = 10-est_entrada
    return np.random.binomial(Nder, 0.5)

Nemb = [127,162,179,75,223,186,124,45,100,171,235,176,130,159,117,100,92,68,242,122,184,84,240,319,61,78,20,141,202, 
        213,204,360,169,206,326,210,335,233,102,243,135,310,138,95,216,99,346,220,191,230,219,225,271,270,110,305,157,
        128,163,90,148,70,40,80,105,159,141,150,164,200,213,195,134,141,107,177,109,48,145,114,400,212,258,198,229,175,
        199,177,194,185,303,335,310,104,374,190,211,160,138,227,122,230,97,166,232,187,212,125,119,90,286,310,115,277,
        189,159,266,170,28,141,155,309,152,122,262,111,254,124,138,190,136,110,396,96,86,111,81,226,50,134,131,120,112,
        140,280,145,208,333,250,221,318,120,72,166,194,87,94,170,65,190,359,312,205,77,197,359,174,140,167,181,143,99,
        297,92,246,211,275,224,171,290,291,220,239,126,89,66,35,26,129,234,181,180,58,40,54,123,78,319,389,121]

m, s = norm.fit(Nemb)

estaciones = []
for x in range(10):
	estaciones.append(Estacion(x))

pasajeros = []

tiempo = 0
Nemb = 0
Npas = 0
Npas_estacion = []

for est in estaciones:
	est.tiempo_llegada = tiempo
	Nemb = int(np.random.normal(m, s))
	Npas += Nemb

	for x in range(Nemb):
		pasajero = Pasajero(est.id)
		pasajeros.append(pasajero)
		est.pasajeros_embarcados.append(pasajero)

	for pasajero in pasajeros:
		if pasajero.estacion_desembarque == est.id:
			est.pasajeros_desembarcados.append(pasajero)
			pasajeros.remove(pasajero)
			Npas -= 1

	tiempo += tiempo_recorrido(Npas)
	Npas_estacion.append(Npas)

cant_pasajeros_estacion = []
for x in estaciones:
	cant_pasajeros_estacion.append(len(pasajeros_embarcados))

print("Tiempo total recorrido %d" % (tiempo))
print("Numero de pasajeros promedio a bordo del tren %f" % (np.mean(Npas_estacion)))
print("Numero maximo de pasajeros embarcados %d" % (max(cant_pasajeros_estacion)))