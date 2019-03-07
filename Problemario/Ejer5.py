import numpy as np
import scipy as st


def gen_buques(tiempo):
	temp = 1
	buques = []
	buques.append(buque(1))
	while temp < tiempo:
		temp += np.random.choice([1,2,3,4,5], p=[0.20,0.25,0.35,0.15,0.05])
		if temp > tiempo:
			return buques
		else:
			b = buque(temp)
			buques.append(b)
	return buques

def gen_tipo():
	return np.random.choice(['tanque', 'mediano', 'pequeno'], p= [0.40,0.35,0.25])


class buque():
	def __init__(self,t):
		self.tipo = gen_tipo()
		self.tiempo_llegada = t
		self.tiempo_salida = 0
		self.tiempo_esperando = 0

	def descargar(self, terminal):
		if self.tipo == 'tanque':
			if terminal == 'A':
				return 4
			else:
				return 3
		elif self.tipo == 'mediano':
			if terminal == 'A':
				return 3
			else:
				return 2
		else:
			if terminal == 'A':
				return 2
			else:
				return 1


class terminal():
	def __init__(self,tipo):
		self.tipo = tipo
		self.libre = True
		self.buque = None
		self.tiempo_trabajando = 0
		self.tiempo_desocupado = 0
		self.buques_atendidos = []
		self.ocupado = 0

	def atender(self, buque, dia_actual):
		self.libre = False
		if self.tipo == 'A':
			self.tiempo_trabajando = buque.descargar('A')
			self.ocupado = buque.descargar('A')-1
			buque.tiempo_esperando = dia_actual - buque.tiempo_llegada
		else:
			self.tiempo_trabajando = buque.descargar('B')
			self.ocupado = buque.descargar('B')-1
			buque.tiempo_esperando = dia_actual - buque.tiempo_llegada
		self.buque = buque

	def nuevo_dia(self, dia_actual):
		self.ocupado -= 1
		if self.libre:
			self.tiempo_desocupado += 1
		if self.ocupado == 0:
			print("Manana sale buque tipo %s del terminal %s" % (self.buque.tipo,self.tipo))
			self.libre = True
			self.buques_atendidos.append(self.buque)
			self.buque.tiempo_salida = dia_actual
			self.buque = None

t_max = int(input('Maximo de dias: '))
puerto = gen_buques(t_max)
max_buques = len(puerto)
buques_en_puerto = []

terminial_A = terminal('A')
terminial_B = terminal('B')
print("tiemos de llegada")
for x in puerto:
	print("Buque tipo %s llega el dia %d" % (x.tipo,x.tiempo_llegada))
print("==================")
dia = 1
while dia <= t_max:
	print("==> Dia %d" % (dia))
	if terminial_A.libre and len(puerto) > 0 and puerto[0].tiempo_llegada <= dia:
		terminial_A.atender(puerto.pop(0),dia)
		print("Buque %s entra al terminal A en el tiempo %d" % (terminial_A.buque.tipo,terminial_A.buque.tiempo_llegada))
	else:
		terminial_A.nuevo_dia(dia + 1)
	
	if terminial_B.libre and len(puerto) > 0 and puerto[0].tiempo_llegada <= dia:
		terminial_B.atender(puerto.pop(0),dia)
		print("Buque %s entra al terminal B en el tiempo %d" % (terminial_B.buque.tipo,terminial_B.buque.tiempo_llegada))
	else:
		terminial_B.nuevo_dia(dia + 1)
	buques_en_puerto.append(len(puerto))
	dia += 1
	
print(terminial_A.tiempo_desocupado)
print(terminial_B.tiempo_desocupado)
#print(puerto)

buques_tanque_en_puerto = []
buques_mediano_en_puerto = []
buques_pequeno_en_puerto = []

for x in terminial_A.buques_atendidos:
	if x.tipo == 'tanque':
		buques_tanque_en_puerto.append(x.tiempo_esperando)
	elif x.tipo == 'mediano':
		buques_mediano_en_puerto.append(x.tiempo_esperando)
	else:
		buques_pequeno_en_puerto.append(x.tiempo_esperando)
for x in terminial_B.buques_atendidos:
	if x.tipo == 'tanque':
		buques_tanque_en_puerto.append(x.tiempo_esperando)
	elif x.tipo == 'mediano':
		buques_mediano_en_puerto.append(x.tiempo_esperando)
	else:
		buques_pequeno_en_puerto.append(x.tiempo_esperando)
if len(puerto) > 0:
	for x in puerto:
		if x.tipo == 'tanque':
			buques_tanque_en_puerto.append(t_max - x.tiempo_llegada)
		elif x.tipo == 'mediano':
			buques_mediano_en_puerto.append(t_max - x.tiempo_llegada)
		else:
			buques_pequeno_en_puerto.append(t_max - x.tiempo_llegada)

print("-------------------DATOS ESTADISTICOS------------------------------")
print("Numero promedio de tanques en el puerto: %f" % (np.mean(buques_en_puerto)))
print("Numero promedio de dias que pasa un buque tanque en el puerto: %f" % (np.mean(buques_tanque_en_puerto)))
print("Numero promedio de dias que pasa un buque tanque mediano en el puerto: %f" % (np.mean(buques_mediano_en_puerto)))
print("Numero promedio de dias que pasa un buque tanque pequeno en el puerto: %f" % (np.mean(buques_pequeno_en_puerto)))
print("Porcentaje de tiempo que pasa el terminal A desocupado %d %%" % (terminial_A.tiempo_desocupado*100/t_max))
print("Porcentaje de tiempo que pasa el terminal B desocupado %d %%" % (terminial_B.tiempo_desocupado*100/t_max))
print("Cantidad de buques que llegaron al puerto: %d" % (max_buques))
if terminial_A.buque:
	print("Cantidad de buques atendidos en el terminal A: %d  y uno descargando" % (len(terminial_A.buques_atendidos)))
else:
	print("Cantidad de buques atendidos en el terminal A: %d" % (len(terminial_A.buques_atendidos)))
if terminial_B.buque:
	print("Cantidad de buques atendidos en el terminal B: %d  y uno descargando" % (len(terminial_B.buques_atendidos)))
else:
	print("Cantidad de buques atendidos en el terminal B: %d" % (len(terminial_B.buques_atendidos)))
print("Cantidad de buques en el puerto: %d" % (len(puerto)))
