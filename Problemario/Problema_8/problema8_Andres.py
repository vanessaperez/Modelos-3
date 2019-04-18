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
	return True

if __name__ == "__main__":
	main()