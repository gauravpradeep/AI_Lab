class Graph:
	def __init__(self):
		self.adj_list={}
		self.adj_matrix=[]

	def add_node(self,node,connections):
		if node not in self.adj_list:
			self.adj_list[node]=[]
		for i in range(len(connections)):
			if connections[i] not in self.adj_list[node]:
				self.adj_list[node].append(connections[i])
			if connections[i] not in self.adj_list:
				self.adj_list[connections[i]]=[]
			if node not in self.adj_list[connections[i]]:	
				self.adj_list[connections[i]].append(node)

	def create_matrix(self):
		for i in range(len(self.adj_list)):
			self.adj_matrix.append([0]*len(self.adj_list))

		for node in self.adj_list:
			for j,connection in enumerate(self.adj_list[node]):
				self.adj_matrix[ord(node)-65][ord(connection)-65]=1

def main():
	g=Graph()
	g.add_node("A",["B","C","E"])
	g.add_node("C",["A","B","D","E"])
	g.add_node("B",["D"])

	for key in g.adj_list:
		print(f"{key} : {g.adj_list[key]}")
		print("\n")
	g.create_matrix()

	print(g.adj_matrix)

if __name__ == '__main__':
		main()	