"""
	Dada la siguiente lista:

	notas = [(5, 5, 10), (10, 2, 4), (10, 1, 9), (10, 2, 3)]

	En contrar una lista como sigue:

	[20, 16, 20, 15]

	author: juanyanza11
"""
notas = [(5, 5, 10), (10, 2, 4), (10, 1, 9), (10, 2, 3)]

n1 = lambda x: x[0] # Posicion [0] de la lista [0] de la tupla
n2 = lambda x: x[1] # Posicion [0] de la lista [1] de la tupla
n3 = lambda x: x[2] # Posicion [0] de la lista [2] de la tupla
funciones_suma = lambda x: (n1(x) + n2(x) + n3(x))
print(list(map(funciones_suma, notas)))