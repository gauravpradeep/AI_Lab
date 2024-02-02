class Graph:
	def __init__(self):
		self.adj_list={}

	def add_edge(self,node,connections):
		if node not in self.adj_list:
			self.adj_list[node]=[]
		if connections not in self.adj_list:
			self.adj_list[connections]=[]
		
		self.adj_list[node].append(connections)

	def top_sort(self):
		in_deg=[0]*len(self.adj_list)
		q=[]
		top=[]
		cntr=0
		for node in self.adj_list:
			for neighbour in self.adj_list[node]:
				in_deg[neighbour]+=1

		# print(in_deg)

		for i,count in enumerate(in_deg):
			if count==0:
				q.append(i)

		# print(q)

		while q:
			x=q.pop(0)
			# print(q)
			top.append(x)
			# print(top)
			cntr+=1

			for neighbour in self.adj_list[x]:
				in_deg[neighbour]-=1
				if in_deg[neighbour]==0:
					q.append(neighbour)


		if cntr == len(self.adj_list):
			print(top)
		else:
			print("Topological sort not possible")

if __name__ == '__main__':
    g = Graph()
    g.add_edge(5, 2)
    g.add_edge(5, 0)
    g.add_edge(4, 0)
    g.add_edge(4, 1)
    g.add_edge(2, 3)
    g.add_edge(3, 1)
    
    g.top_sort()