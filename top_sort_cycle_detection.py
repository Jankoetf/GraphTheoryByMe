from collections import deque
import heapq
import numpy as np
import matplotlib.pyplot as plt
import networkx as nx

class Directed_Graph:
    def __init__(self, edges = []):
        self.edges = edges
        self.vertexes = []
        
        for edge in edges:
            self.vertexes.extend([edge[0], edge[1]])
        self.vertexes = list(set(self.vertexes))
            
        self.adjacency = {c:[] for c in self.vertexes}
        for start, end in self.edges:
            self.adjacency[start].append(end)
            
       
    def prepare(self):
        self.visited = set()
        
    def analize(self):
        pass
        
    def plot_graph(self, layout = 'c'):
        graph = nx.DiGraph(self.adjacency)
        fig, ax = plt.subplots(figsize=(7, 7))
        
        pos = nx.circular_layout(graph)
        
        nx.draw(graph, pos, ax=ax, with_labels=True, node_size=1200,\
                node_color='skyblue', font_size=20, arrows=True, arrowsize = 20)
        plt.show()
        
    def dfs_recursive_trust_me_bro(self, start):
        print(start)
        for neighbor in self.adjacency[start]:
            self.dfs_recursive_trust_me_bro(neighbor)
            
    def dfs_recursive_tour(self, start, visited):
        print(start)
        visited.add(start)
        print(visited)
        for neighbor in self.adjacency[start]:
            if neighbor not in visited:
                self.dfs_recursive_tour(neighbor, visited)
    
    def dfs_recursive(self, start, visited):
        print(start)
        visited.add(start)
        print(visited)
        for neighbor in self.adjacency[start]:
            if neighbor not in visited:
                self.dfs_recursive(neighbor, visited)
                
        visited.remove(start)
        
    def dfs_cycle_detection(self, start, visited):
        visited.add(start)
        for neighbor in self.adjacency[start]:
            if neighbor not in visited:
                if self.dfs_cycle_detection(neighbor, visited): return True
            else:
                return True
                
        visited.remove(start)
        
    def topological_sort(self, start, global_Visited, pathVisited, result):
        if self.adjacency[start] == []:
            result.append(start)
            global_Visited.add(start)
            return
            
        pathVisited.add(start)
        global_Visited.add(start)
        
        for neighbor in self.adjacency[start]:
            if neighbor not in pathVisited:
                if neighbor not in global_Visited:
                    if self.topological_sort(neighbor, global_Visited, pathVisited, result): return True
            else:
                return True
            
        pathVisited.remove(start)
        result.append(start)
        
        
            
    def print_graph(self):
        print(self.adjacency)
            
    
    
    
    
TopG1 = Directed_Graph([['a', 'b'], ['a', 'c'], ['b', 'd'], ['d', 'c'], ['b', 'n']])
#TopG1 = Directed_Graph([['a', 'b'], ['a', 'c'], ['b', 'd']])
TopG1.plot_graph()
TopG1.prepare()
#if TopG1.dfs_cycle_detection('a', set()): print("cycle")

#topSort
result = []
if TopG1.topological_sort('a', set(), set(), result): print("cycle")
print(result)

    
    

            
            
        
    

            