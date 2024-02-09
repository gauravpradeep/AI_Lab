class Graph:
	def __init__(self,cost_matrix):
		self.adj_list={}
		self.cost_matrix=cost_matrix

	def add_edge(self,node,connections):
		if node not in self.adj_list:
			self.adj_list[node]=[]
		if connections not in self.adj_list:
			self.adj_list[connections]=[]
		
		self.adj_list[node].append(connections)


	def ucs(self,start,goals):
		cost=0
		costs=[0]*len(self.adj_list)
		costs[0]=0
		path=[]
		q=[]
		reached_goal=None
		parents={}
		visited=[False]*len(self.adj_list)
		q.append((start,0))
		parents[0]=0
		while q:
			q.sort(key=lambda x:x[1])
			x=q.pop(0)
			# path.append(x[0])
			cost=x[1]
			if x[0] in goals:
				reached_goal=x[0]
				break
			for neighbour in self.adj_list[x[0]]:
				if visited[neighbour]:
					if cost+self.cost_matrix[x[0]][neighbour] < costs[neighbour]:
						costs[neighbour]=cost+self.cost_matrix[x[0]][neighbour]
						parents[neighbour]=x[0]
				if not visited[neighbour]:
					q.append((neighbour,cost+self.cost_matrix[x[0]][neighbour]))
					parents[neighbour]=x[0]
					visited[neighbour]=True
					costs[neighbour]=cost+self.cost_matrix[x[0]][neighbour]

		final_path=[]
		current=reached_goal
		while current!= start:
			final_path.append(current)
			current=parents[current]

		final_path.append(start)
		print("Path : ",final_path[::-1])
		print("Path Cost : ",cost)


if __name__ == '__main__':
	cost_matrix=[[0,2,0,5,0,0,0],[0,0,0,0,0,0,1],[0,4,0,0,0,0,0],[0,5,0,0,2,0,6],[0,0,4,0,0,5,0],[0,0,6,0,0,0,3],[0,0,0,0,7,0,0]]
	g=Graph(cost_matrix)
	g.add_edge(0, 1)
	g.add_edge(0, 3)
	g.add_edge(3, 1)
	g.add_edge(3, 6)
	g.add_edge(1, 6)
	g.add_edge(3, 4)
	g.add_edge(6, 4)
	g.add_edge(4, 2)
	g.add_edge(2, 1)
	g.add_edge(4, 5)
	g.add_edge(5, 2)
	g.add_edge(5, 6)
	g.ucs(0,[6])