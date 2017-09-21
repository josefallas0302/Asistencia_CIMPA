"""
	En este módulo se define el sistema de ecuaciones diferenciales
	de la dinámica de la población dentro de una comunidad.
"""

	def vectorfield(w,t,p)

"""
Define la ecuacion diferencial para la dinamica poblacional

Se definen 3 vectores:
	- w: Vector de variables de Estado
			[s, i, e]

	- t: tiempo

	- p: Parametros
			[u, b, g]
"""	

		s, i, e = w
		u, b, g = p
		n = s+i+e

# Create f = (s’,i’,r’):

		f = [s,
			 u * n - b*s*i/n - u*s ,
			 i,
			 (b * s * i/n - (u+g) * i,
			 r,
			 g * i- u * n
			]
	return f
	
	
