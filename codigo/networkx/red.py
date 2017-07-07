import networkx as nx
import matplotlib.pyplot as plt
import random

def generate(num_nodes,num_edges):
	G = nx.Graph() 
	for i in range(num_nodes):
		G.add_node(i)

	for i in range(num_edges):
		G.add_edge(random.randint(0,num_nodes),random.randint(0,num_nodes))

	return G 
if __name__ == "__main__":
	
	n_nodes = int(input("Inserte el numero de nodos que desea:"))

	
	n_edges = 	int(input("Inserte el numero de enlaces que desea:"))


	red_1= generate(n_nodes,n_edges)

	nx.draw(red_1)
	#red_1.draw()
	plt.show()
