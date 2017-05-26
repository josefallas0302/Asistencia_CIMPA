from network import network
import matplotlib.pyplot as plt

def print_network(network) :
		central_n = len(network.list_nodes)/2
		plt.plot(central_n, central_n, 'ro')
		for i in range(len(network.list_nodes))
			

		plt.show()


if __name__ == "__main__":


	red_1 = network(10)


	for i in range(10):
		red_1.insert_data(i)
		red_1.go_next()


	red_1.connect (0,2)
	red_1.connect (0,9)

	red_1.connect (1,7)
	red_1.connect (1,8)

	red_1.connect (2,4)
	red_1.connect (2,3)
	red_1.connect (3,5)

	nodo_1 = red_1.find(6)
	nodo_2 = red_1.find(15)
	
	print_network(red_1)
	

