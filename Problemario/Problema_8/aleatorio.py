import random

def random_autos_vendidos():
	nro_autos = random.random()	
	if 0 <= nro_autos and nro_autos <= 0.10:
		return 0
	elif 0.10 < nro_autos and nro_autos <= 0.25:
		return 1
	elif 0.25 < nro_autos and nro_autos <= 0.45:
		return 2
	elif 0.45 < nro_autos and nro_autos <= 0.70:
		return 3
	elif 0.70 < nro_autos and nro_autos <= 0.90:
		return 4
	elif 0.90 < nro_autos and nro_autos <= 1:
		return 5

def random_tipo_autos():
	tipo_auto = random.random()
	if 0 <= tipo_auto and tipo_auto <= 0.40:
		return "Compacto"
	elif 0.40 < tipo_auto and tipo_auto <= 0.75:
		return "Mediano"
	elif 0.75 < tipo_auto and tipo_auto <= 1:
		return "Lujo"


def random_tipo_autos_mediano():
	tipo_auto = random.random()
	if 0 <= tipo_auto and tipo_auto <= 0.40:
		return 400
	elif 0.40 < tipo_auto and tipo_auto <= 1:
		return 500

def random_tipo_autos_lujo():
	tipo_auto = random.random()
	if 0 <= tipo_auto and tipo_auto <= 0.35:
		return 1000
	elif 0.35 < tipo_auto and tipo_auto <= 0.75:
		return 1500
	elif 0.75 < tipo_auto and tipo_auto <= 1:
		return 2000
