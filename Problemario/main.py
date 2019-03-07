import sys
from Problema_1.main import problema_1
from Problema_2.main import problema_2


numero_simulaciones = 1

for i in range(len(sys.argv)):
    if '-p' == sys.argv[i] or '--problema' == sys.argv[i]:
        if '1' == sys.argv[i + 1]:
            problema_a_correr = problema_1
        elif '2'  == sys.argv[i + 1]:
            problema_a_correr = problema_2
            
    elif '-s' == sys.argv[i] or '--simulaciones' == sys.argv[i]:
        numero_simulaciones = int(sys.argv[i + 1])
 
problema_a_correr(numero_simulaciones)
