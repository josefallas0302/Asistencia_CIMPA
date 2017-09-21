import networkx as nx
import random
import time
impot Sympy

class Comunidad
	"""Metodo Constructor, inicializa la comunidad con un número determinado de personas SIR, el cual decide el usuario"""
	def __init__(n_sanos, n_infectados, n_recuperados):
			work_list[]
			register []
		for i in n_sanos 
			persona = Person(S, i)
			self.register.append(persona)

		for j in n_infectados
			persona = Person(I, j)
			self.register.append(persona)

		for k in n_recuperados
			persona = Person(R, k)
			self.register.append(persona)

	"""Da un Estado de la comunidad, el número de personas Sanas, Infectadas y Recuperadas  """

	def stadistic (self)
		S_counter = 0
		I_counter = 0
		R_counter = 0

		for i in self.register
			p_state = self.register(i).get_state

			if(p_state = S ){
				S_counter = S_counter + 1
			} 
			if(p_state = I){
				I_counter = I_counter + 1 
			}
			if(p_state = R){
				R_state = R_counter + 1
			}

		total = S_counter + I_counter + R_counter

		print ("Poblacion Total: ", total, " Sanos: ", S_counter, " Infectados - ", I_counter, " Recuperados - " , R_counter  )


#Funcion que envia un numero de personas determinado de una comunidad A a una comunidad B.
	def send_p(self, comunidad_B, n_persona)
		for i in range(n_personas):
			a = randrange(len(self.register)-1)
			p_aux = self.register(a)
			self.revome(a)
			
			

class Person:

		"""Constructor de persona, crea una persona con 
		identidad y estado de Salud"""
	def __init__(self, initial_state, identidad):

		self.state = initial_state
		self.ID = identidad

		"""Cambia el Estado de la Persna S-I-R"""
	def set_state(self,new_state):
		self.state = new_state

		"""Imprime el Estado de salud de la persona"""
	def get_state (self):
		print  (self.state)
		return (self.state)		

		"""Retorna e imprime el ID de la persona"""
	def get_id (self):
		print (self.ID)
		return self.ID

		
