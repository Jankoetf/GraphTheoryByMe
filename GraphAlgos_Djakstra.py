from collections import deque
import heapq
import numpy as np
import matplotlib.pyplot as plt
import networkx as nx


class Weighted_Directed_Graph:
    def __init__(self, edges = [('A', 'B', 1), ('A', 'C', 2), ('B', 'C', 3)]):
        self.edges = edges
        self.nodes = []
        for edg in edges:
            if edg[0] not in self.nodes:
                self.nodes.append(edg[0])
            if edg[1] not in self.nodes:
                self.nodes.append(edg[1])
        
        self.adjacency = {node:[] for node in self.nodes}
        for start, end, weight in self.edges:
            self.adjacency[start].append((weight, end))
        
        #for plotting
        self.nx_graph = nx.DiGraph()
        self.nx_graph.add_weighted_edges_from(self.edges)
        
    def plot_graph(self):
        graph = nx.DiGraph(self.nx_graph)
        fig, ax = plt.subplots(figsize=(7, 7))
        
        pos = nx.circular_layout(graph)

        #labels = {node: f'{node}({self.vertices_values[node]})' for node in graph.nodes()}
        nx.draw(graph, pos, ax=ax, with_labels=True, node_size=1400,\
                node_color='skyblue', font_size=25, arrows=True, arrowsize=40)
        edge_labels = nx.get_edge_attributes(self.nx_graph, 'weight')
        nx.draw_networkx_edge_labels(self.nx_graph, pos, edge_labels=edge_labels, font_size=25)
        plt.show()
        
    def print_graph(self):
        print(self.edges)
        print(self.nodes)
        print(self.adjacency)
    

    def Djakstra(self, start):
        distances = {node: float('inf') if node != start else 0 for node in self.nodes}
    
        # Priority queue (min-heap) for tracking minimum distance
        pq = [(0, start)]  # (distance, node)
    
        while pq:
            current_distance, current_node = heapq.heappop(pq)
    
            # If a shorter path to the current node has been found, skip processing
            if current_distance > distances[current_node]:
                continue
    
            # Explore neighbors
            for weight, neighbor in self.adjacency[current_node]:
                distance = current_distance + weight
    
                # If a shorter path to the neighbor is found
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(pq, (distance, neighbor))
            print(distances)
                    
        print(distances)
        return distances
    

def Djakstra_example():
    G1 = Weighted_Directed_Graph([('A', 'B', 1), ('A', 'C', 5), ('B', 'C', 3), ('D', 'E', 3), ('A', 'D', 1), ('D', 'C', 1)])
    G1.plot_graph()
    G1.print_graph()
    G1.Djakstra('A')
    
Djakstra_example()