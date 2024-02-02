# class Graph:
# 	def __init__(self):
# 		self.adj_list={}

# 	def add_edge(self,node,connections):
# 		if node not in self.adj_list:
# 			self.adj_list[node]=[]
# 		if connections not in self.adj_list:
# 			self.adj_list[connections]=[]
		
# 		self.adj_list[node].append(connections)

# 	def top_sort(self):
# 		in_deg=[0]*len(self.adj_list)
# 		q=[]
# 		top=[]
# 		cntr=0
# 		for node in self.adj_list:
# 			for neighbour in self.adj_list[node]:
# 				in_deg[neighbour]+=1

# 		for i,count in enumerate(in_deg):
# 			if count==0:
# 				q.append(i)

# 		while q:
# 			x=q.pop(0)
# 			top.append(x)
# 			cntr+=1

# 			for neighbour in self.adj_list[x]:
# 				in_deg[neighbour]-=1
# 				if in_deg[neighbour]==0:
# 					q.append(neighbour)

# 		if cntr == len(self.adj_list):
# 			print("Acyclic")
# 		else:
# 			print("Cyclic graph")

# if __name__ == '__main__':
#     g = Graph()
#     g.add_edge(5, 2)
#     g.add_edge(5, 0)
#     g.add_edge(4, 0)
#     g.add_edge(4, 1)
#     g.add_edge(2, 3)
#     g.add_edge(3, 1)
    
#     g.top_sort()


class Graph:
	def __init__(self):
		self.adj_list={}

	def add_edge(self,node,connections):
		if node not in self.adj_list:
			self.adj_list[node]=[]
		if connections not in self.adj_list:
			self.adj_list[connections]=[]
		
		self.adj_list[node].append(connections)


	def check_cyclic(self):
		parents={}
		q=[]
		q.append(2)
		for node in self.adj_list:
			parents[node]=[]

		# for node in self.adj_list:
		while q:
			x=q.pop(0)
			print(x)
			for neighbour in self.adj_list[x]:
				q.append(neighbour)
				parents[neighbour].append(x)


		print(parents)


if __name__ == '__main__':
    g = Graph()
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(2, 3)
    g.add_edge(2, 0)


    g.check_cyclic()
