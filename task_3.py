import heapq

class Graph:
    def __init__(self):
        self.nodes = set()
        self.edges = {}
        self.distances = {}

    def add_node(self, value):
        self.nodes.add(value)
        self.edges[value] = []

    def add_edge(self, from_node, to_node, distance):
        self.edges[from_node].append(to_node)
        self.edges[to_node].append(from_node)
        self.distances[(from_node, to_node)] = distance
        self.distances[(to_node, from_node)] = distance


def dijkstra(graph, start):
    # Ініціалізація відстаней до всіх вершин як нескінченність і до початкової вершини як 0
    distances = {node: float('infinity') for node in graph.nodes}
    distances[start] = 0

    # Пріоритетна черга для вершин
    priority_queue = [(0, start)]
    heapq.heapify(priority_queue)

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_distance > distances[current_node]:
            continue

        for neighbor in graph.edges[current_node]:
            distance = graph.distances[(current_node, neighbor)]
            new_distance = current_distance + distance

            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                heapq.heappush(priority_queue, (new_distance, neighbor))

    return distances


def main():
    graph = Graph()
    nodes = ['A', 'B', 'C', 'D', 'E', 'F']

    for node in nodes:
        graph.add_node(node)

    graph.add_edge('A', 'B', 7)
    graph.add_edge('A', 'C', 9)
    graph.add_edge('A', 'F', 14)
    graph.add_edge('B', 'C', 10)
    graph.add_edge('B', 'D', 15)
    graph.add_edge('C', 'D', 11)
    graph.add_edge('C', 'F', 2)
    graph.add_edge('D', 'E', 6)
    graph.add_edge('E', 'F', 9)

    initial_node = 'A'
    distances = dijkstra(graph, initial_node)

    print(f"Найкоротші відстані від вершини {initial_node}:")
    for node in distances:
        print(f"Відстань до {node}: {distances[node]}")

if __name__ == "__main__":
    main()
