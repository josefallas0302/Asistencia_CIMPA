#	En este modulo se define el sistema de ecuaciones diferenciales
#	de la dinamica de la poblacion dentro de una comunidad.


def vectorfield (w,t,p):


#Define la ecuacion diferencial para la dinamica poblacional

#Se definen 3 vectores:
#	- w: Vector de variables de Estado
#			[s, i, e]
#	- t: tiempo
#	- p: Parametros	[u, b, g]	

	Ys,Xs,Yi,Xi,Yr,Xr = w
	u, b, g = p
	n = Xs+Xi+Xr

# Create f = (s_prima,s(t),i_prima,i(t),r_prima,r(t)):

	f = [Ys,
	u*n - (b*Xs*Xi)/n - u*Xs,
	Yi,
	(b*Xs*Xi)/n - (u+g) * Xi,
	Yr,
	g * Xi - u * n]
	return f
