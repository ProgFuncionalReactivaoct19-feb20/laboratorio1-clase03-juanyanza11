"""
	Dadas las siguientes edad:

	[10, 12, 13, 14, 16, 18, 20, 30, 31, 32, 33, 40, 50]

	Se ha generado una lista denomindad black_edades, formada así:

	[10, 14, 30, 32, 40, 16]

	Generar el listado de edades que no estén dentro de las black_edades.

	author: juanyanza11
"""

edades = [10, 12, 13, 14, 16, 18, 20, 30, 31, 32, 33, 40, 50]
black_edades = [10, 14, 30, 32, 40, 16]

def no_black(x):
	if x in black_edades:
		return False
	else:
		return True
resultado = filter(no_black, edades)
print(list(resultado)) # Imprime las edades que no se encuentran en black_edades comprandola dcon edades