# Graph
# It is a network of nodes(vertexes) connected by edges.

# 1. Directed (or) Undirected
# Directed = A -> B != B -> A (A points to B doesn't mean B points to A)
# Undirected = A -> B == B -> A (A and B points to each other)

# 2. Weighted (or) Unweighted
# Edges can have values assigned to them (Weighted). No edge values = Unweighted.

# 3. Cyclic (or) Acyclic
# If there is a path where a node can reach itself -> Cyclic. If not -> Acyclic

#################################################################################

# This implementation is a Undirected, Unweighted Graph.
# Could be Cyclic or Acyclic depending on how the nodes are connected.


class Graph:

    def __init__(self):
        self.adjacent_list = {}
        self.number_of_nodes = 0

    def add_vertex(self, node):
        """Adds a vertex to the graph"""
        self.adjacent_list[node] = []
        self.number_of_nodes += 1

    def add_edge(self, node1, node2):
        """Add edges between two nodes"""
        # connect node 1 to node 2
        node1_list = self.adjacent_list[node1]
        node1_list.append(node2)
        # connect node 2 to node 1
        node2_list = self.adjacent_list[node2]
        node2_list.append(node1)

    def print(self):
        for key, value in self.adjacent_list.items():
            print(key,"->",value)


# --- Comment these out --- #

# # New Max Binary Heap
# graph = Graph()
#
# # add vertex
# graph.add_vertex('0')
# graph.add_vertex('1')
# graph.add_vertex('2')
# graph.add_vertex('3')
# graph.add_vertex('4')
# graph.add_vertex('5')
# graph.add_vertex('6')
#
# # add edges
# graph.add_edge('3','1')
# graph.add_edge('3','4')
# graph.add_edge('4','2')
# graph.add_edge('4','5')
# graph.add_edge('1','2')
# graph.add_edge('1','0')
# graph.add_edge('0','2')
# graph.add_edge('6','5')
#
# # print graph
# graph.print()
