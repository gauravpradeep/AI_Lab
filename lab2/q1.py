class Graph:
	def __init__(self):
		self.adj_list={}

	def add_node(self,node,connections):
		if node not in self.adj_list:
			self.adj_list[node]=[]
		
		self.adj_list[node].append(connections)

def main():
	g=Graph()
	g.add_node(0,1)
	g.add_node(1,2)
	g.add_node(2,0)
	g.add_node(2,1)
	g.add_node(3,2)
	g.add_node(4,5)
	g.add_node(5,4)

	for key in g.adj_list:
		print(f"{key} : {g.adj_list[key]}")
		print("\n")

if __name__ == '__main__':
	main()