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

# Distribucion de probabilidades del numero de automoviles vendidos
def ventas_autos():
	aux = random()

	# probabilidad automoviles vendidos semanalmente
	if aux <= 0.10: return 0
	elif aux <= 0.25: return 1
	elif aux <= 0.45: return 2
	elif aux <= 0.70: return 3
	elif aux <= 0.90: return 4
	else: return 5

# Distribucion de probabilidades de la demanda semanal
def tipo_autos():
	aux = random()

	# probabilidad tipo de automovil vendido en la semana
	if aux <= 0.40: return "Compacto"
	elif aux <= 0.75: return "Mediano"
	else: return "Lujo"

# Distribucion de probabilidades para la paga de comisión dado tipo de carro
def pagar_comision(tipo):
	
	if tipo == "Compacto": return 250
	elif tipo == "Mediano":
		aux = random()
		return 400 if aux <= 0.40 else 600
	else: 
		aux = random()
		if aux <= 0.35: return 1000
		elif aux <= 0.60: return 1500
		else: return 2000
		
def main():

	vendedores = int(input("Colocar el numero de vendedores: "))
	tiempo_max = int(input("Colocar el numero de semanas: "))
	simulaciones_max = Q = int(input("Colocar el numero de simulaciones: "))
	comision_simulaciones = [0.0 for x in range(simulaciones_max)]

	for simulaciones in range(simulaciones_max):
		# Iteramos sobre varias semanas
		comision_vendedores = [0.0 for x in range(vendedores)]
		for tiempo in range(tiempo_max):
			# Iteramos sobre los vendedores
			for vendedor in range(vendedores):
				comision = 0
				numero_ventas_por_vendedor = ventas_autos()

				for auto in range(numero_ventas_por_vendedor):
					tipo = tipo_autos()
					comision += pagar_comision(tipo)

				# Sumamos la comision por semana
				comision_vendedores[vendedor] = comision_vendedores[vendedor] + comision

		# Arreglo con el promedio de comision de cada vendedor para TODAS las semanas dada una simulacion
		promedio_semanal_comision = [ (x/tiempo_max) for x in comision_vendedores ]	
		comision_simulaciones[simulaciones] = sum(promedio_semanal_comision)/len(promedio_semanal_comision)

	promedio_comision = sum(comision_simulaciones)/simulaciones_max
	m_error_90Rcomision = error_90_prcnt(comision_simulaciones, promedio_comision)

	print("\nLa comisión promedio por empleado en una semana es de: %d" % (promedio_comision))
	print("El intervalo de confianza de 90 por ciento de la comision de un empleado en una semana es (%f , %f)" % (promedio_comision - m_error_90Rcomision, promedio_comision + m_error_90Rcomision))

if __name__ == "__main__":

	main()