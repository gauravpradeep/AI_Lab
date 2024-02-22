class Graph:
    def __init__(self, heuristics):
        self.adj_list = {}
        self.heuristics = heuristics

    def add_edge(self, node, connections):
        if node not in self.adj_list:
            self.adj_list[node] = []
        self.adj_list[node].extend(connections)

    def astar(self, start, goals):
        openList = []
        closedList = set()
        parents = {}
        g_costs = {node: float('inf') for node in self.adj_list}
        g_costs[start] = 0

        openList.append((start, g_costs[start] + self.heuristics[start]))

        while openList:
            openList.sort(key=lambda x: x[1])
            current, current_f_cost = openList.pop(0)
            closedList.add(current)

            if current in goals:
                return self.reconstruct_path(parents, current)

            for neighbor, move_cost in self.adj_list[current]:
                tentative_g_cost = g_costs[current] + move_cost
                if neighbor not in closedList or tentative_g_cost < g_costs[neighbor]:
                    parents[neighbor] = current
                    g_costs[neighbor] = tentative_g_cost
                    f_cost = tentative_g_cost + self.heuristics[neighbor]
                    if neighbor not in [node for node, cost in openList]:
                        openList.append((neighbor, f_cost))

    def reconstruct_path(self, parents, current):
        path = [current]
        while current in parents:
            current = parents[current]
            path.append(current)
        path.reverse()
        return path

if __name__ == '__main__':
    heuristics = {
        0: 10, # A
        1: 8,  # B
        2: 5,  # C
        3: 7,  # D
        4: 8,  # E
        5: 6,  # F
        6: 5,  # G
        7: 3,  # H
        8: 1,  # I
        9: 0,  # J
    }
    
    g = Graph(heuristics)

    g.add_edge(0, [(1, 6), (5, 3)])  # A to B and F
    g.add_edge(1, [(0, 6), (2, 3), (3, 2)])  # B to A, C, and D
    g.add_edge(2, [(1, 3), (3, 1), (4, 5)])  # C to B, D, and E
    g.add_edge(3, [(1, 2), (2, 1), (4, 8), (6, 7)])  # D to B, C, E, and G
    g.add_edge(4, [(2, 5), (3, 8), (8, 5), (9, 3)])  # E to C, D, I, and J
    g.add_edge(5, [(0, 3), (6, 1), (7, 6)])  # F to A, G, and H
    g.add_edge(6, [(3, 7), (5, 1), (8, 3)])  # G to D, F, and I
    g.add_edge(7, [(5, 6), (8, 2)])  # H to F and I
    g.add_edge(8, [(4, 5), (6, 3), (7, 2), (9, 5)])  # I to E, G, H, and J
    g.add_edge(9, [(4, 3), (8, 5)])  # J to E and I

    path = g.astar(0, [9])
    print("Path: ", path)
