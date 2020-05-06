from util import Stack

class Graph:
    def __init__(self):
        self.nodes = {}

    def add_node(self, node):
        if node not in self.nodes:
            self.nodes[node] = set()

    def add_edge(self, child, parent):
        self.nodes[child].add(parent)

    def getNeighbors(self, child):
        return self.nodes[child]


# Three steps to solve almost any graphs problem

## Describe in terms of graphs
### Nodes: people
### Edges: if they're parent-child

## Build our graph
### Build a graph class
### Don't write an adjency list or matrix, just get neighbors

## Choose a graph algorithm
### traversal or search? No node we're looking for, no node at which we'll stop, visit all
### breadth or depth? Either one since it's a traversal, depth would be better for a search for longest path

def dft(graph, starting_node):
    stack = Stack()
    stack.push((starting_node, 0))
    visited = set()

    # could build a dictionary or set or
    # track two variables as we go

    visited_pairs = set()

    while stack.size() > 0:
        current_pair = stack.pop()
        visited_pairs.add(current_pair)
        current_node = current_pair[0]
        current_distance = current_pair[1]

        if current_node not in visited:
            visited.add(current_node)

            parents = graph.getNeighbors(current_node)

            for parent in parents:
                parent_distance = current_distance + 1
                stack.push((parent, parent_distance))
    longest_distance = 0
    aged_one = -1

    for pair in visited_pairs:
        node = pair[0]
        distance = pair[1]

        if distance > longest_distance:
            longest_distance = distance
            aged_one = node

        return aged_one

def earliest_ancestor(ancestors, starting_node):

    # build our graph
    graph = Graph()
    for parent, child in ancestors:
        graph.add_node(child)
        graph.add_node(parent)
        graph.add_edge(child, parent)

    # run dft

    aged_one = dft(graph, starting_node)

    # choose the most distant ancestor

    return aged_one