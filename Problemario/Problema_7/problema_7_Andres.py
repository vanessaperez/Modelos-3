#!/usr/bin/env python3
import math
from random import random

# Calcular la varianza
def varianza(lis_data, promedio):
	suma = 0
	for i in range(len(lis_data)):
		suma += ((lis_data[i] - promedio)*(lis_data[i] - promedio))
	suma /= (len(lis_data))
	return suma

# Calcular el error porcentual
def error_90_prcnt (lis_data, promedio):
	varz = varianza(lis_data, promedio)
	nmuestra = len(lis_data)
	return (1.65*(math.sqrt(varz/nmuestra))) 

# Distribucion de probabilidades del tiempo de entrega
def tiempo_entrega():
	aux = random()

	# Tiempo en dias
	if aux <= 0.2: return 1
	elif aux <= 0.50: return 2
	elif aux <= 0.85: return 3
	else: return 4

# Distribucion de probabilidades de la demanda diaria
def demanda_diaria():
	aux = random()

	# Unidades
	if aux <= 0.05: return 12
	elif aux <= 0.20: return 13
	elif aux <= 0.45: return 14
	elif aux <= 0.80: return 15
	elif aux <= 0.95: return 16
	else: return 17

def main():

	costo_inventario = 0.2
	costo_escasez = 1
	costo_pedido = 10

	arreglo_reorden = []

	tiempo_max = int(input("Colocar el numero de dias: "))
	Q = int(input("Colocar el punto maximo de reorden: "))
	simulaciones_max = Q = int(input("Colocar el numero de simulaciones: "))

	for simulaciones in range(simulaciones_max):
		# Iteramos sobre varios puntos de reorden para conseguir un optimo
		for punto_reorden in range(Q):
			tiempo = 0					# tiempo en dias transcurridos
			escasez = 0 				# Escasez acumulativa		
			costo = 0					# Costo acumulativo
			inventario_actual = Q 		# Inventario que se tiene para el punto de reorden actual
			dias_prox_envio = 0			# Dias para el proximo envio
			envio_en_camino = False 	# Existe o no un envio en camino
			arreglo_costo_por_dia = []	# Arreglo de los costos por dia

			# Mientras no se cumpla la totalidad de dias
			while tiempo < tiempo_max:

				# Si habia un pedido solicitado y llego, se recibe
				if dias_prox_envio == 0 and envio_en_camino:
					inventario_actual += Q
					envio_en_camino = False

	            # Si hay un envio en camino pero no ha llegado, se reduce el tiempo
				elif dias_prox_envio > 0 and envio_en_camino:
					dias_prox_envio -= 1

	            # Generamos una demanda aleatoria para el dia correspondiente
				demanda = demanda_diaria()

				# Reducimos la demanda adquiridad diaria por el consumo de los clientes
				inventario_actual -= demanda

				# Manejo del costo de la escasez
				if inventario_actual < 0: costo += abs(inventario_actual) * costo_escasez

	            # Manejo del costo por mantener inventario
				elif inventario_actual > 0: costo += inventario_actual * costo_inventario

	            # Si estamos por debajo del punto de reorden, hacemos un pedido
				if inventario_actual <= punto_reorden and not envio_en_camino:
					dias_prox_envio = tiempo_entrega()
					costo += costo_pedido		# Al hacer el pedido se suma el costo
					envio_en_camino = True

				arreglo_costo_por_dia.append(costo)
				tiempo += 1

			# Buscamos los puntos de reorden optimos
			costo_promedio = sum(arreglo_costo_por_dia)/len(arreglo_costo_por_dia)
			if punto_reorden == 0:
				reorden_optimo = punto_reorden
				costo_minimo = costo_promedio

			elif costo_promedio < costo_minimo:
				reorden_optimo = punto_reorden
				costo_minimo = costo_promedio

	    # Agregamos cada uno de los puntos de reorden optimo para cada simulacion
		arreglo_reorden.append(reorden_optimo)

	#print(arreglo_reorden)
	promedio_reorden_optimo = sum(arreglo_reorden)/simulaciones_max
	m_error_90Reorden = error_90_prcnt(arreglo_reorden, promedio_reorden_optimo)

	print("\nEl punto de reorden optimo es %d" % (promedio_reorden_optimo))
	print("El intervalo de confianza de 90 por ciento del punto de reorden optimo esta entre (%f , %f)" % (promedio_reorden_optimo - m_error_90Reorden, promedio_reorden_optimo + m_error_90Reorden))

if __name__ == "__main__":
	main()