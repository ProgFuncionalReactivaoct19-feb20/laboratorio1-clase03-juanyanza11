"""
	Dada la siguiente frase:

	"No hay medicina que cure lo que no cura la felicidad"

	Encuentre el listado que sigue:

	["No", "hay", "que", "lo", "que", "no", "la"]
	
	author: juanyanza11
"""

def validar_palabras(x):
	palabras = ["No", "hay", "que", "lo", "que", "no", "la"]
	if x in palabras:
		return True
	else:
		return False

cadena ="No hay medicina que cure lo que no cura la felicidad"
cadena_sep = cadena.split(' ') # Funcion para separar la palabra y almacenarla en una lista SEPARADOR SPACE
resultado = filter(validar_palabras,cadena_sep) # filtrar las palabras permitidas
print(list(resultado))