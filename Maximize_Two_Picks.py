"""            1. choose at max two projects to maximaze value        """
import networkx as nx
import matplotlib.pyplot as plt

class Graph:
    def __init__(self, vertices):
        self.adjecency = {v:[] for v in range(len(vertices))}
        self.vertices_values = vertices
        self.independent_nodes = set()
        self.number_of_independent_nodes = 0
        
    def add_edges_from_indexes_of_vertices(self, A, B):
        for i in range(len(A)):
            self.adjecency[B[i]] = \
                self.adjecency.get(B[i], []) + [A[i]]
        
                
    def find_independent_nodes(self):
        for v in self.adjecency:
            if not self.adjecency[v]:
                self.independent_nodes.add(v)
                self.number_of_independent_nodes += 1
        
        
    def print_independent_nodes(self):
        print(self.independent_nodes)
        
        
    def print_graph(self):
        print(self.adjecency)
        
        
    def plot_graph(self):
        graph = nx.DiGraph(self.adjecency)
        fig, ax = plt.subplots(figsize=(7, 7))
        
        pos = nx.circular_layout(graph)

        labels = {node: f'{node}({self.vertices_values[node]})' for node in graph.nodes()}
        nx.draw(graph, pos, ax=ax,labels=labels, with_labels=True, node_size=1200,\
                node_color='skyblue', font_size=25, arrows=True, arrowsize=40)
        plt.show()
        
        
    @staticmethod
    def two_bigest_update(current, first, second):
        if current>=first:
            first, second = current, first
        elif current > second:
            second = current        
        return first, second
    
    def bigest_sum_of_2_projects(self):
        if not self.number_of_independent_nodes:
            return None
        bigest_single = second_bigest_single = bigest_pair = float('-inf')
        for v in self.adjecency:
            if not self.adjecency[v]:
                bigest_single, second_bigest_single = \
                    self.two_bigest_update(self.vertices_values[v], bigest_single, second_bigest_single)
            elif len(self.adjecency[v]) == 1 and self.adjecency[v][0] in self.independent_nodes:
                new_pair = self.vertices_values[v] + self.vertices_values[self.adjecency[v][0]]
                bigest_pair = max(bigest_pair, new_pair)
        
        return max(bigest_single, bigest_single + second_bigest_single, bigest_pair) 
            

def test_code1():
    G1 = Graph([5,6,6,7,-10])
    #G1.print_graph()
    G1.plot_graph()
    G1.add_edges_from_indexes_of_vertices([0,0,0,1,2,3], [1,2,3,3,1,2])
    G1.find_independent_nodes()
    G1.print_independent_nodes()
    G1.plot_graph()
    G1.print_graph()
    print(G1.bigest_sum_of_2_projects())
test_code1()
























    