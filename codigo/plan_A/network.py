import matplotlib.pyplot as plt

class network:
	def __init__(self,num_node):
		self.list_nodes = []
		self.actual_node = 0
		for i in range (num_node):
			self.add(node())

#		set_iterator (self)


#Graficar RED

#Reinicia el nodo actual
	def set_iterator (self):
		if(self.list_nodes == False):
			print "Lista esta Vacia"
		else:
			self.actual_node = 0

# Agrego un nuevo nodo a la red, este no tiene ninguna conexion
	def add (self,node):
		self.list_nodes.append(node) 

# Meter dato
	def insert_data (self, dato):
		self.list_nodes[self.actual_node].data.append(dato)
		

#Elimina un nodo de la red.	
	def delete (self, node):
		self.list_nodes.remove(node)

#Va al siguiente nodo (No necesariamente esta conectado)
	def go_next (self):
		if (self.actual_node +1 >= len(self.list_nodes) ):
			self.actual_node = 0
		else:
			self.actual_node = self.actual_node +1

#Retorna el dato actual
#	def return_data (self)
#		data = self.list_nodes[actual_node].data	

# Conecto dos nodos segun el indice dado por la network
	def connect (self,index_node_a,index_node_b):
		self.list_nodes[index_node_a].neighbors.append(self.list_nodes[index_node_b])
		self.list_nodes[index_node_b].neighbors.append(self.list_nodes[index_node_a])

# Desconecto dos nodos segun el indice dado por la network
	def disconnect (self, index_node_a, index_node_b):
		self.list_nodes[index_node_a].neighbors.remove(self.list_nodes[index_node_b])
		self.list_nodes[index_node_b].neighbors.remove(self.list_nodes[index_node_a])

# Retorna un int diciendo el indice de mi nodo principal en la network
	def principal_node ():
		for i in self.list_nodes:
			nodo_principal
			size_principal
			if ( size_principal < self.list_nodes[i].len(neighbors) ):
				size_principal = self.list_nodes[i].len(neighbors)
				nodo_principal = {i}
			print nodo_principal			

#Encontrar un elemento en la red
	def find (self, data):
		# Variable utilizada para saber si encontre el dato que buscaba
		found = False	
		nodelio = self.list_nodes[0]		
		for i in range (len(self.list_nodes)):
			print "Estoy en el nodo " +str(i)
			if (data == self.list_nodes[i].data[0]):
				nodelio = self.list_nodes[i]
				break
			vecindario = len(self.list_nodes[i].neighbors)
			for j in range(vecindario) :
				print "Estoy en el nodo " +str(j)
				if(data == self.list_nodes[j].data[0]):
					found = True
					nodelio = self.list_nodes[j]
					break

		if (found == True):
			print "Lo encontre"
	

		return nodelio
			
						
class node:
	def __init__(self):
		self.data = []
		self.neighbors= []

#if __name__ == "__main__":
		
#		network_1 = network()
#		network_1.add()

