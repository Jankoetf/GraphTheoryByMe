import numpy as np
from collections import deque
import networkx as nx
import matplotlib.pyplot as plt


class Directed_Graph:
    def __init__(self, graph = {'a':['b', 'c', 'e'], 'b':['d'], 'c':['e'], 'd':['f'], 'e':[], 'f':[]}):
        self.graph = graph
        
    """Practice:"""
    
    def plot_graph(self, layout = 'c'):
        graph = nx.DiGraph(self.graph)
        fig, ax = plt.subplots(figsize=(7, 7))
        
        if layout == 'c':
            pos = nx.circular_layout(graph)
        elif layout == 'k':
            pos = nx.kamada_kawai_layout(graph)
        elif layout == 's':
            pos = nx.spectral_layout(graph)
        else:
            pos = nx.shell_layout(graph)
            
        nx.draw(graph, pos, ax=ax, with_labels=True, node_size=1200,\
                node_color='skyblue', font_size=30, arrows=True)
        plt.show()
        
    def print_graph(self):
        print(self.graph)
        
    #acyclic graphs
    def dfs_iterative_print_acyclic_directed_graph(self, root):
        rez = []
        stack = []
        if root:
            stack.append(root)
        
        while(stack):
            popped = stack.pop()
            rez.append(popped)
            for neighbor in self.graph[popped]:
                stack.append(neighbor)
        print("Iterative dfs for acyclic graph: ",",".join(rez))
                
    def dfs_recursive_print_acyclic_directed_graph(self, root):
        self.rez = []
        def dfs(root):
            self.rez.append(root)
            for neighbor in self.graph[root]:
                dfs(neighbor)
        dfs(root)

        print("Recursive dfs for acyclic graph: ", ",".join(self.rez))
    
    def bfs_print_acyclic_directed_graph(self, root):
        rez = []
        dq = deque()
        if root:
            dq.append(root)
        
        while(dq):
            popped = dq.popleft()
            rez.append(popped)
            for neighbor in self.graph[popped]:
                dq.append(neighbor)
        print("Iterative bfs for acyclic graph: ",",".join(rez))
        
        
    #cyclic graphs
    def dfs_iterative_print_cyclic_directed_graph(self, root):
        rez = []
        stack = []
        visited = set()
        
        if root:
            stack.append(root)
        
        while(stack):
            popped = stack.pop()
            rez.append(popped)
            visited.add(popped)
            for neighbor in self.graph[popped]:
                if neighbor not in visited:
                    stack.append(neighbor)
        print("Iterative dfs for cyclic graph: ",",".join(rez))
                
    def dfs_recursive_print_cyclic_directed_graph(self, root):
        self.rez = []
        visited = set()
        def dfs(root):
            self.rez.append(root)
            visited.add(root)
            for neighbor in self.graph[root]:
                if neighbor not in visited:
                    dfs(neighbor)
        dfs(root)

        print("Recursive dfs for cyclic graph: ", ",".join(self.rez))
    
    def bfs_print_cyclic_directed_graph(self, root):
        rez = []
        visited = set()
        dq = deque()
        if root:
            dq.append(root)
        
        while(dq):
            popped = dq.popleft()
            if popped in visited:
                continue
            rez.append(popped)
            visited.add(popped)
            for neighbor in self.graph[popped]:
                if neighbor not in visited:
                    dq.append(neighbor)
        print("Iterative bfs for cyclic graph: ",",".join(rez))
    
    """Examples"""
    """1: has path"""
    def has_path(self, root, end):
        dq = deque()
        dq.append(root)
        visited = set()
        rez = []
        while(dq):
            popped = dq.popleft()
            if popped in visited:
                continue
            rez.append(popped)
            if popped == end:
                print("rezult: ", ",".join(rez))
                return
            visited.add(popped)
            for neighbor in self.graph[popped]:
                if not neighbor in visited:
                    dq.append(neighbor)
        
        return print("rezult not found: ", ",".join(rez))
    
    
    """2. has cycle"""
    def has_cycle_dfs(self):
        visited = set()
        
        for key in self.graph:
            if key in visited:
                continue
            
            pathVisited = set()
            stack = [key]
            
            while(stack):
                popped = stack.pop()
                if popped in pathVisited:
                    print("Ima bajo petljica ono mala")
                    return
                visited.add(popped)
                pathVisited.add(popped)
                
                for neighbor in self.graph[popped]:
                    if neighbor not in visited:
                        stack.append(neighbor)
                
                pathVisited.remove(popped)
                
        print("Nema petlja liče")
        return 
    
       
        
       
        
       
class Undirected_Graph:
    def __init__(self, graph = {'a':['b', 'c'], 'b':['d', 'a'], 'c':['a'], 'd':['b']}):
        self.graph = graph
        
    def to_adjacency(self):
        adjecency = {}
        for edge in self.graph:
            adjecency[edge[0]] = adjecency.get(edge[0], []) + [edge[1]]
            adjecency[edge[1]] = adjecency.get(edge[1], []) + [edge[0]]
        self.graph = adjecency
        
    def print_graph(self):
        print(self.graph)
        
        
    def plot_graph(self, layout = 'c'):
        graph = nx.Graph(self.graph)
        fig, ax = plt.subplots(figsize=(7, 7))
        
        if layout == 'c':
            pos = nx.circular_layout(graph)
        elif layout == 'k':
            pos = nx.kamada_kawai_layout(graph)
        elif layout == 's':
            pos = nx.spectral_layout(graph)
        else:
            pos = nx.shell_layout(graph)
            
        nx.draw(graph, pos, ax=ax, with_labels=True, node_size=1200,\
                node_color='skyblue', font_size=30)
        plt.show()
        
    """1. path between two nodes"""
    def has_path(self, root, end):
        dq = deque([root])
        rez = []
        visited = set()
        
        while(dq):
            popped = dq.popleft()
            if popped in visited:
                continue
            rez.append(popped)
            if popped == end:
                print(f"from {root} to {popped}: result is: ", ",".join(rez))
                return
            visited.add(popped)
            for neighbor in self.graph[popped]:
                if neighbor not in visited:
                    dq.append(neighbor)
        
        print(f"from {root} to {popped}: path does not exists: ", ",".join(rez))
        
    """2. Number of conected components"""
    def number_of_conected_components(self):
        dq = deque()
        rez = 0
        visited = set()
        
        for key in self.graph.keys():
            if key not in visited:
                rez +=1
                dq.append(key)
                
                while(dq):
                    popped = dq.popleft()
                    if popped in visited:
                        continue
                    visited.add(popped)
                    for neighbor in self.graph[popped]:
                        if neighbor not in visited:
                            dq.append(neighbor)
        
        print(f"number of conected components: {rez}")
        
        
    """3. Largest component"""
    def largest_component(self):
        dq = deque()
        rez = 0
        visited = set()
        
        for key in self.graph.keys():
            if key not in visited:
                dq.append(key)
                temp = 0
                
                while(dq):
                    popped = dq.popleft()
                    if popped in visited:
                        continue
                    visited.add(popped)
                    temp+=1
                    for neighbor in self.graph[popped]:
                        if neighbor not in visited:
                            dq.append(neighbor)
                rez = max(temp, rez)
        
        print(f"Largest Component: {rez}")
        
    """4. shortest path between two nodes"""
    def shortest_path(self, root, end):
        dq = deque([(root, 0)])
        visited = set()
        
        while(dq):
            popped = dq.popleft()
            if popped[0] in visited:
                continue
            if popped[0] == end:
                print(f"shortest path from {root} to {end} is: {popped[1]}")
                return
            visited.add(popped[0])
            for neighbor in self.graph[popped[0]]:
                if neighbor not in visited:
                    dq.append((neighbor, popped[1]+1))
                    
        print(f"There is no path between {root} to {end}!")
        return
    
    
    def has_cicle_dfs(self):
        visited = set()
        
        for key in self.graph.keys():
            if key in visited:
                continue
            stack = []
            stack.append(key)
            #print(stack)
            while(stack):
                popped = stack.pop()
                if popped in visited:
                    print("Ima petlja čovek brate")
                    return
                visited.add(popped)
                for neighbor in self.graph[popped]:
                    if neighbor not in visited:
                        stack.append(neighbor)
        print("Nema petlja bajo")
        return 
            
            
        
        
    
class Example_Directed_graph:
    def __init__(self):
        pass
        
    def acyclic_undirected_graph():
        aciclic_graph = {'a':['b', 'c'], 'b':['d'], 'c':['e'], 'd':['f'], 'e':[], 'f':[]}
        acyclic_graph = Directed_Graph(aciclic_graph)
        acyclic_graph.plot_graph('c')
        acyclic_graph.dfs_iterative_print_acyclic_directed_graph('a')
        acyclic_graph.dfs_recursive_print_acyclic_directed_graph('a')
        acyclic_graph.bfs_print_acyclic_directed_graph('a')
        
    def cyclic_undirected_graph():
        cyclic_graph = {'a':['b', 'c', 'e'], 'b':['d'], 'c':['e'], 'd':['a'], 'e':['f'], 'f':[]}
        cyclic_graph = Directed_Graph(cyclic_graph)
        cyclic_graph.plot_graph('c')
        cyclic_graph.dfs_recursive_print_cyclic_directed_graph('a')
        cyclic_graph.dfs_iterative_print_cyclic_directed_graph('a')
        cyclic_graph.bfs_print_cyclic_directed_graph('a')
        
    def path_undirected():
        cyclic_graph = {'a':['c', 'e'], 'b':['d'], 'c':['e'], 'd':['a'], 'e':['f'], 'f':[]}
        cyclic_graph = Directed_Graph(cyclic_graph)
        cyclic_graph.plot_graph('c')
        cyclic_graph.has_path('a', 'd')
        cyclic_graph.has_path('a', 'f')
        cyclic_graph.has_path('a', 'c')
        
    def has_cycle_dfs():
        cyclic_graph = {'a':['e'], 'b':['d'], 'c':['a'], 'd':['a'], 'e':['c', 'f'], 'f':[]}
        cyclic_graph = Directed_Graph(cyclic_graph)
        cyclic_graph.plot_graph()
        cyclic_graph.has_cycle_dfs()
        
        
        
        
class Example_Undirected_Graph:
    def __init__(self):
        pass
    
    """from edges to adjecency"""
    def to_adjecency():
        undirected_graph = [['a', 'b'], ['b', 'c'], ['a', 'd']]
        undirected_graph = Undirected_Graph(undirected_graph)
        undirected_graph.print_graph()
        undirected_graph.to_adjacency()
        undirected_graph.print_graph()
        undirected_graph.plot_graph()
        
    """has path"""
    def has_path():
        undirected_graph = [['a', 'b'], ['b', 'c'], ['c', 'd'], ['f', 'd'], ['f', 'a'], ['n', 'm']]
        undirected_graph = Undirected_Graph(undirected_graph)
        undirected_graph.to_adjacency()
        undirected_graph.plot_graph()
        undirected_graph.has_path('a', 'd')
        undirected_graph.has_path('m', 'a')
        
    """ number_of_conected_components """
    def number_of_conected_components():
        undirected_graph = [['a', 'b'], ['b', 'c'], ['a', 'd'], ['f', 'n'], ['c', 'd'], ['b', 'f']]
        undirected_graph = Undirected_Graph(undirected_graph)
        undirected_graph.to_adjacency()
        undirected_graph.plot_graph()
        undirected_graph.number_of_conected_components()
        
    """Largest Component in undirected graph"""
    def largest_component():
        undirected_graph = [['a', 'b'], ['b', 'c'], ['a', 'd'], ['f', 'n'], ['c', 'd']]
        undirected_graph = Undirected_Graph(undirected_graph)
        undirected_graph.to_adjacency()
        undirected_graph.plot_graph()
        undirected_graph.largest_component()
        
    def shortest_path():
        undirected_graph = [['a', 'b'], ['b', 'c'],['d', 'f'], ['f', 'n'],\
                            ['c', 'd'], ['a', 'n'], ['r', 'm']]
        undirected_graph = Undirected_Graph(undirected_graph)
        undirected_graph.to_adjacency()
        undirected_graph.plot_graph()
        undirected_graph.shortest_path('a', 'f')
        undirected_graph.shortest_path('a', 'm')
    
    def has_cycle_dfs():
        undirected_graph = [['a', 'b'], ['b', 'c'],['d', 'f'], ['f', 'n'],\
                            ['c', 'd'], ['r', 'm'], ['r', 'c']]
        undirected_graph = Undirected_Graph(undirected_graph)
        undirected_graph.to_adjacency()
        #undirected_graph.print_graph()
        undirected_graph.plot_graph()
        undirected_graph.has_cicle_dfs()
        
        

"""         Unirected Graphs            """ 
example = Example_Directed_graph
#example.path_undirected()
example.has_cycle_dfs()

"""        Directed Graphs              """
#example = Example_Undirected_Graph
#example.has_path()
#example.number_of_conected_components()
#example.largest_component()
#example.shortest_path()
#example.has_cycle_dfs()



























