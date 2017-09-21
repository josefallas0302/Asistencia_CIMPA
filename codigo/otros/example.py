import networkx as nx
import matplotlib.pyplot as plt

if __name__ == "__main__":

	G= nx.Graph()
	G.add_nodes_from([2,3])

	H=nx.path_graph(10)	
	G.add_nodes_from(H)

	G.add_node(H)

	G.add_edge(1,2)

	e=(2,3)
	G.add_edge(*e) # unpack edge tuple*
	
	G.add_edges_from([(1,2),(1,3)])
	
	G.add_edges_from(H.edges())
	
	G.remove_node(H)
	
#	nx.draw(G)

#nx.draw_random(G)
#nx.draw_circular(G)
	nx.draw_spectral(G)
	plt.show()
