import uuid
import heapq
from collections import deque
import networkx as nx
import matplotlib.pyplot as plt


class Node:
    def __init__(self, key, color="#1296F0"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())

def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph

def build_heap(heap_list):
    heapq.heapify(heap_list)
    tree = [Node(i) for i in heap_list]
    for i, node in enumerate(tree):
        if 2 * i + 1 < len(tree):
            node.left = tree[2 * i + 1]
        if 2 * i + 2 < len(tree):
            node.right = tree[2 * i + 2]
    return tree

def draw_tree(tree_root):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()

def generate_colors(num_colors):
    colors = []
    for i in range(num_colors):
        shade = int(255 * (i / num_colors))
        color = f'#{shade:02x}{shade:02x}ff'  # Від темного до світло-синього
        colors.append(color)
    return colors

def bfs(root):
    if not root:
        return []

    queue = deque([root])
    order = []
    while queue:
        node = queue.popleft()
        order.append(node)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return order

def dfs(root):
    if not root:
        return []

    stack = [root]
    order = []
    while stack:
        node = stack.pop()
        order.append(node)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return order

def visualize_traversal(tree_root, traversal_func):
    traversal_order = traversal_func(tree_root)
    colors = generate_colors(len(traversal_order))
    for i, node in enumerate(traversal_order):
        node.color = colors[i]
    draw_tree(tree_root)

heap_list = [1, 3, 5, 7, 9, 2, 4, 34, 2, 1, 2]
root = build_heap(heap_list)[0]

print("Візуалізація обходу в ширину (BFS)")
visualize_traversal(root, bfs)

print("Візуалізація обходу в глибину (DFS)")
visualize_traversal(root, dfs)
