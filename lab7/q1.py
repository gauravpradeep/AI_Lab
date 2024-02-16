class Graph:
    def __init__(self,heuristics):
        self.adj_list = {}
        self.heuristics = heuristics

    def add_edge(self, node, connections):
        if node not in self.adj_list:
            self.adj_list[node] = []

        self.adj_list[node].append(connections)

    def astar(self,start,goals):
        openList=[]
        closedList=[]
        parents={}
        reached_goal=None
        openList.append([start,11])
        costs=[0]*len(self.adj_list)
        costs[0]
        while openList:
            print(openList)
            openList.sort(key=lambda x:x[1])
            current=openList.pop(0)
            closedList.append(current[0])
            cost=current[1]
            if current[0] in goals:
                print("goal reached")
                final_path=[]
                current=current[0]
                final_cost=0
                while current!= start:
                    final_path.append(current)
                    current=parents[current]
                final_path.append(start)
                print("Path : ",final_path[::-1])
                print("Path Cost : ",cost)
                return

            for neighbour in self.adj_list[current[0]]:
                temp_cost=cost-self.heuristics[current[0]]+self.heuristics[neighbour[0]]+neighbour[1]
                if neighbour[0] in closedList:
                    if temp_cost < costs[neighbour[0]]:
                        costs[neighbour[0]]=temp_cost
                        parents[neighbour[0]]=current[0]
                if neighbour[0] not in closedList:
                    openList.append([neighbour[0],temp_cost])
                    parents[neighbour[0]]=current[0]
                    costs[neighbour[0]]=temp_cost

        print("done")





if __name__ == '__main__':
    heuristics={
0: 11,
1: 6,
2: 99,
3: 1,
4: 7,
5: 0,
}
    g=Graph(heuristics)

    g.add_edge(0,[1,2])
    g.add_edge(0,[4,3])
    g.add_edge(1,[0,2])
    g.add_edge(1,[2,1])
    g.add_edge(1,[5,9])
    g.add_edge(2,[1,1])
    g.add_edge(3,[4,6])
    g.add_edge(3,[5,1])
    g.add_edge(4,[0,3])
    g.add_edge(4,[3,6])
    g.add_edge(5,[1,9])
    g.add_edge(5,[3,1])

    g.astar(0,[5])