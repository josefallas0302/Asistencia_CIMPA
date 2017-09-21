scipy from.integrate import odeint
import SED

#Valor de Parametros 
# Probabilidades de Estado

u = 0.0001
b = 0.00000000001
g = 0.00000001

# Condiciones iniciales

s = 100
i = 3
r = 0

#ODE parametros para resolver
abserr = 1.0e-8
relerr = 1.0e-6
stoptime = 10.0
numpoints = 250



