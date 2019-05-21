from simulacion import *
from statistics import mean , stdev


gastos = list()
def estadisticas_globales(n):
	for i in range(n):
		simulacion = Hospitaland(30,i)
		simulacion.run()
		gastos.append(simulacion.gasto)
		print(simulacion.gasto)
	print(stdev(estadisticas))


if __name__ == '__main__':
	estadisticas_globales(100)



