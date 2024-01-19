class Graph:
	def __init__(self):
		self.adj_list={}

	def add_edge(self,node,connections):
		if node not in self.adj_list:
			self.adj_list[node]=[]
		if connections not in self.adj_list:
			self.adj_list[connections]=[]
		
		self.adj_list[node].append(connections)
		self.adj_list[connections].append(node)

	def dfs(self,node,visited,path,goal):
		visited[node]=True
		if node==goal:
			print('Maze solved')
			print(path)
			exit(0)

		for neighbour in self.adj_list[node]:
			if visited[neighbour]==False:
				path.append(neighbour)
				self.dfs(neighbour,visited,path,goal)

	
	def solve_maze(self,goal):
		visited=[False]*(len(self.adj_list)+1)
		path=[]
		for vertex in self.adj_list:
			print(vertex)
			if visited[vertex]==False:
				path.append(vertex)
				self.dfs(vertex,visited,path,goal)


if __name__ == '__main__':
    g = Graph()
    g.add_edge(1,2)
    g.add_edge(1,6)
    g.add_edge(2,3)
    g.add_edge(3,8)
    g.add_edge(8,7)
    g.add_edge(6,11)
    g.add_edge(11,12)
    g.add_edge(12,17)
    g.add_edge(17,16)
    g.add_edge(17,18)
    g.add_edge(18,19)
    g.add_edge(19,14)
    g.add_edge(14,13)
    g.add_edge(14,9)
    g.add_edge(9,10)
    g.add_edge(10,5)
    g.add_edge(5,4)
    g.add_edge(10,15)
    g.add_edge(15,20)
    goal=20
    g.solve_maze(goal)