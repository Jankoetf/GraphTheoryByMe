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
        self.globalVisited = set()
        self.pathVisited = set()
        self.result = []
        self.max_depth = float('inf')
        
    def analize(self):
        print(self.result)
        
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
        
    def topological_sort(self, start):
        if self.adjacency[start] == []:
            self.result.append(start)
            self.globalVisited.add(start)
            return False
            
        self.pathVisited.add(start)
        self.globalVisited.add(start)
        
        for neighbor in self.adjacency[start]:
            if neighbor in self.pathVisited:
                return True
            elif neighbor not in self.globalVisited:
                if self.topological_sort(neighbor): return True
            
        self.pathVisited.remove(start)
        self.result.append(start)
        #self.adjacency[start] = [] #optimization
        return False
    
    def dfs_path(self, source, sink, visited, current_depth):
        if current_depth >= self.max_depth:
            return
        
        visited.append(source)
        
        if source == sink:
            self.max_depth = current_depth
            self.result = visited[::]
            print(self.result)
            visited.pop()
            return
        
        for neighbor in self.adjacency[source]:
            if neighbor not in visited and current_depth+1 < self.max_depth:
                self.dfs_path(neighbor, sink, visited, current_depth+1)

        visited.pop()

            
    def print_graph(self):
        print(self.adjacency)
        
        
    """Bfs path"""
    def which_path_bfs(self, start, target):
        visited = set()
        
        queue=deque([start])
        all_paths = {start:'END'}
        
        while(queue):
            popped = queue.popleft()
            visited.add(popped)
            if popped == target:
                path_found = True
                break
            
            for neighbor in self.adjacency[popped]:
                if neighbor not in visited:
                    queue.append(neighbor)
                    if neighbor not in all_paths:
                        all_paths[neighbor] = popped
                    
                    
        if path_found:
            path = [target]
            while(path[-1] != 'END'):
                path.append(all_paths[path[-1]])
                
            print(f"path from {start} to {target} is: {path[::-1][1:]}")
            
        else:
            print(f"there is no path from {start} to {target}")
        
                    
        
        
        
        
    
    
TopG1 = Directed_Graph([['a', 'b'], ['b', 'd'], ['b', 'c'], ['c', 'd'], ['d', 'm'], ['m', 'c'], ['a', 'c']])
#TopG1 = Directed_Graph([['a', 'b'], ['a', 'c'], ['b', 'd']])
TopG1.plot_graph()
TopG1.prepare()
#path_bfs
TopG1.which_path_bfs('a', 'm')

#path_dfs
#TopG1.dfs_path('a', 'c', [], 0)
#TopG1.analize()



    
    

            
            
        
    

            