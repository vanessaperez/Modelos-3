from random import random
from queue import PriorityQueue
import math

def varianza(lis_data, promedio):
    suma = 0
    for i in range(len(lis_data)):
        suma += ((lis_data[i] - promedio)*(lis_data[i] - promedio))
    suma /= (len(lis_data))
    return suma

def error_90_prcnt (lis_data, promedio):
    varz = varianza(lis_data, promedio)
    nmuestra = len(lis_data)
    return (1.65*(math.sqrt(varz/nmuestra))) 

def entrega():
	aleat = random()
	if aleat < 0.2:
		return 1
	elif aleat < 0.5:
		return 2
	elif aleat < 0.85:
		return 3
	else:
		return 4

def demanda():
	aleat = random()
	if aleat < 0.05:
		return 12
	elif aleat < 0.2:
		return 13
	elif aleat < 0.45:
		return 14
	elif aleat < 0.8:
		return 15
	elif aleat < 0.95:
		return 16
	else:
		return 17

def main():
	minCosto = 1000000000000000
	mejorReorden = -1
	arreglo_reorden = []
	arreglo_costo = []
	x = int(input("Ingrese el máximo punto de reorden: "))
	y = int(input("Ingrese la cantidad de semanas para cada punto: "))
	for reorden in range(x):
		inventario = 100
		escasez = 0
		diaEntrega = -1
		costo = 0
		for i in range(y):
			if diaEntrega == i:
				inventario += 100
				diaEntrega = -1
			elif diaEntrega == -1 and inventario <= reorden:
				diaEntrega = i + entrega()
			demandaHoy = demanda()
			if demandaHoy <= inventario:
				inventario -= demandaHoy
			else:
				escasez += demandaHoy - inventario
				inventario = 0
			costo += escasez + 0.2 * inventario
		#print("El costo con punto de reorden ", reorden, " después de 1000 semanas fue: ", costo)
		if costo < minCosto:
			#print(123123123123123123123123123)
			minCosto = costo
			mejorReorden = reorden
			arreglo_reorden.append(reorden)
			arreglo_costo.append(costo)

	print("---------------- Se ha terminado la simulacion! ----------------")
	print("Analisis de resultados: ")

	print("El mejor punto de reorden es ", mejorReorden, ", el costo después de 1000 semanas fue: ", minCosto)
	reorden = 0
	costoPorUnidad = 0
	for i in range(len(arreglo_reorden)): reorden += arreglo_reorden[i]
	for i in range(len(arreglo_costo)): costoPorUnidad += arreglo_costo[i]
	numero_simulaciones = y

	mediaReorden = reorden/numero_simulaciones
	mediaCostoPorUnidad = costoPorUnidad/numero_simulaciones
	m_error_90Reorden = error_90_prcnt(arreglo_reorden, mediaReorden)
	m_error_90RostoPorUnidad = error_90_prcnt(arreglo_costo, mediaCostoPorUnidad)

	print("Intervalo de Confianza: ")
	print("")
	print("El intervalo de confianza de 90 por ciento del punto de reorden optimo esta entre (%f , %f)" % (abs(mediaReorden-m_error_90Reorden),mediaReorden+m_error_90Reorden))
	print("El intervalo de confianza de 90 por ciento de las unidades de costo esta entre (%f , %f)" % (abs(mediaCostoPorUnidad-m_error_90RostoPorUnidad),mediaCostoPorUnidad+m_error_90RostoPorUnidad))
	print("")


if __name__=='__main__':
	main()
