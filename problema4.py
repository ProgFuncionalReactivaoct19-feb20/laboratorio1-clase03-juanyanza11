"""
	Dado el siguiente listado:

	notas = [(5, 5, 10, "Regular"), (10, 2, 4, "Bueno"), (10, 1, 9, "Muy Bueno"), (7, 2, 3, "Sobresaliente")]

	Filtrar aquellos que tiene la calificación cualitativa "Regular o Bueno"

	author: juanyanza 11
"""

notas = [(5, 5, 10, "Regular"), (10, 2, 4, "Bueno"), (10, 1, 9, "Muy Bueno"), (7, 2, 3, "Sobresaliente")]


n3 = lambda x: x[3] # Cadena Posición para validar

condicion = filter(lambda x: x[3] == "Regular" or x[3] == "Bueno", notas) # filtrar las tuplas que solo contengan Regular o Bueno
print(list(condicion))