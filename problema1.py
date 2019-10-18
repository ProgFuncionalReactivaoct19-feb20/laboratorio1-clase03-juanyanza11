"""
	Determinar los estudiantes que pasan de ciclo. Todos los estudiantes que
	pasan de ciclo son aquellos que tienen un promedio de 16.5 o mayor.

	author: juanyanza11
"""

notas = open("promedios.txt") # Abrir el txt para leerlo
x = notas.read() # Leer las notas
list(x)
y = x.split(',') # separar los caracteres por comas y convierte en lista
#print(y)

y = list(map(int,y)) # Convierte en enteros los elementos de la lista de str
resultado = filter(lambda x: x >= 16.5 ,y)
print(list(resultado)) # Imprimir el resultado en una lista
