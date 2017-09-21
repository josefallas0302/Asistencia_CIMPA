
"""
Esta funcion contiene el sistema de ecuaciones diferenciales:

"""

def eq_population(y,t):
	dy0= -beta*y[0]*y[7]/_Nc_
	dy1=  beta*y[0]*y[7]/_Nc_-alphah*y[1]
	dy2= alphah*y[1]-(gamma+delta)*y[2]

