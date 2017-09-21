from scipy.integrate import odeint
import SED

#Valor de Parametros 
# Probabilidades de Estado

u = 0.000054
b = 0.3
g = 0.14

# Condiciones iniciales
Ys = 0
Xs = 100
Yi = 0
Xi = 3
Yr = 0
Xr = 0

#ODE parametros para resolver
abserr = 1.0e-8
relerr = 1.0e-6
stoptime = 10.0
numpoints = 250


"""Crea los puntos de tiempo a los que toma los datos para la salida del  ODE solver.
Se utilizan bastantes puntos para poder hacer una grafica"""

t = [stoptime * float(i) / (numpoints - 1) for i in range(numpoints)]

#Para pasar los parametros y las condiciones inicaiales a la funcion
p  = [u,b,g]
w0 = [Ys,Xs,Yi,Xi,Yr,Xr]


#Llamada a la funcion de scipy para resolver la ecuacion diferencial
wsol = odeint(SED.vectorfield, w0, t, args=(p,),atol=abserr, rtol=relerr)
file = open("datoslistaa.dat", "w")
titulos = ["Tiempo".rjust(20),"Sanos".rjust(20),"Enfermos".rjust(20),"Recuperados".rjust(20), '\n']
file.writelines(titulos)
#Imprimir Solucion
for t1, w1 in zip(t, wsol):
	da = [str(t1).rjust(20), str(w1[1]).rjust(20),str(w1[3]).rjust(20),str(w1[5]).rjust(20), '\n' ]
	file.writelines(da)
file.close()



