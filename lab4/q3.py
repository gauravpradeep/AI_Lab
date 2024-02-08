class TSPSolver:
    def __init__(self, distance_matrix):
        self.distance_matrix = distance_matrix
        self.num_cities = len(distance_matrix)

    def tsp_bfs(self):
        start_node = 0
        initial_state = (start_node, [start_node], 0)  # (current_node, path, cost)
        queue = [initial_state]
        best_path=[]
        minimum_cost=float('inf')
        while queue:
            current_node, path, cost = queue.pop(0)

            # If all cities are visited and we can return to the starting city
            if len(path) == self.num_cities:
                if(cost+self.distance_matrix[path[-1]][0]<minimum_cost):
                    minimum_cost=cost+self.distance_matrix[path[-1]][0]
                    best_path=path+[0]

            for next_node in range(self.num_cities):
                if next_node not in path:
                    new_path = path + [next_node]
                    new_cost = cost + self.distance_matrix[current_node][next_node]
                    queue.append((next_node, new_path, new_cost))

        print(best_path)
        print(minimum_cost)
            
            
if __name__ == "__main__":
    distance_matrix = [
        [0, 2, 3, 1],
        [2, 0, 4, 2],
        [3, 4, 0, 3],
        [1, 2, 3, 0]
    ]

    tsp_solver = TSPSolver(distance_matrix)
    tsp_solver.tsp_bfs()
