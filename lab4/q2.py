class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_edge(self, node, connections):
        if node not in self.adj_list:
            self.adj_list[node] = []
        if connections not in self.adj_list:
            self.adj_list[connections] = []

        self.adj_list[node].append(connections)

    def has_cycle(self):
        visited = set()
        q = []

        for node in self.adj_list:
            if node not in visited:
                if self._has_cycle_bfs(node, visited, q):
                    return True

        return False

    def _has_cycle_bfs(self, start_node, visited, q):
        q.append((start_node, None))  # Tuple (node, parent)
        visited.add(start_node)

        while q:
            current_node, parent = q.pop(0)

            for neighbor in self.adj_list[current_node]:
                if neighbor not in visited:
                    q.append((neighbor, current_node))
                    visited.add(neighbor)
                elif neighbor != parent:
                    # Detected a back edge, indicating a cycle
                    print(f"Cycle detected at {neighbor}")
                    return True

        return False

if __name__ == '__main__':
    g = Graph()
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(2, 3)
    g.add_edge(2, 0)

    if g.has_cycle():
        print("Graph has a cycle.")
    else:
        print("Graph does not have a cycle.")
