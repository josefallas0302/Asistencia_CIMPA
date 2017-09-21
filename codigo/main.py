import networkx as nx
import matplotlib.pyplot as plt
import random
import time
import os, sys
import clases

def generate(num_nodes,num_edges):
	G = nx.Graph() 
	for i in range(num_nodes):
		G.add_node(i)

	for i in range(num_edges):
		G.add_edge(random.randint(0,num_nodes),random.randint(0,num_nodes))

	return G 

if __name__ == "__main__":
	
	n_nodes  = int(input("Inserte el numero de nodos que desea:"))

	
	n_edges  = int(input("Inserte el numero de enlaces que desea:"))

	sim_time = int(input("Inserte el tiempo de simulacion que desea: "))

	red_1= generate(n_nodes,n_edges)

 # Dibujo la red de nodos que deseo 
	nx.draw(red_1)
	plt.show()

#Defino el tiempo de simulacion

	for x in xrange(sim_time + 1):	
		time.sleep(1)
		sim_time -= 1
	print "FIN"


