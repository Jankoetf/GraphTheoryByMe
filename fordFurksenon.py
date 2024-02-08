from collections import deque
import heapq
import numpy as np
import matplotlib.pyplot as plt
import networkx as nx

class Bipartie_Graph:
    input_memory = {0:(["Dzon", "Bob", "Tsu", "Tate"],[["Job1", "Job2"],\
                    ["Job2", "Job3"], ["Job3", "Job4"], ["Job4", "Job1"]]),
                    1:(["Dzon", "Bob", "Tsu"],[["Job1", "Job2"],\
                    ["Job2", "Job3"], ["Job3", "Job4"]]),
                    2:(["Dzon", "Bob", "Tsu"],[["Job1", "Job2"],\
                    ["Job2", "Job3"], ["Job2"]]),
                    3:(["Dzon", "Bob", "Tsu"],[["Job2"],\
                    ["Job1", "Job2", "Job3"], ["Job2"]])    }
        
    
    def __init__(self, workers, jobs):
        self.all_workers = workers
        self.all_jobs = set()
        for jobs_list in jobs:
            for job in jobs_list:
                self.all_jobs.add(job)
        
        
        #from S to Workers
        self.rezidual_graph = {'S':[(1, name) for name in self.all_workers]}
        self.rezidual_graph.update({name:[(0, 'S')] for name in self.all_workers})
        
        #from workers to Jobs
        for i, name in enumerate(self.all_workers):
            for job in jobs[i]:
                self.rezidual_graph[name].append((1, job))
                self.rezidual_graph[job] = self.rezidual_graph.get(job, []) + [(0, name)]
        
        #from jobs to Sink
        for job in self.all_jobs:
            self.rezidual_graph[job].append((1, 'T'))
            self.rezidual_graph['T'] = self.rezidual_graph.get('T', []) + [(0, job)]
        
        
    def get_edges_for_plot(self):
        self.edges = []
        for key in self.rezidual_graph:
            for value in self.rezidual_graph[key]:
                if value[0] == 1:
                    self.edges.append((key, value[1], value[0]))
        #print(self.edges)
        
    
    def print_graph(self):
        print(f"Workers: {self.all_workers}")
        print(f"Jobs: {self.all_jobs}")
        print(self.rezidual_graph)
        
        
    def plot_weighted_graph(self):
        self.nx_graph = nx.DiGraph()
        self.get_edges_for_plot() #adjacency to edge
        self.nx_graph.add_weighted_edges_from(self.edges)
        
        fig, ax = plt.subplots(figsize=(7, 7))

        #manual positioning
        names_y_pos = np.linspace(2, 0, len(self.all_workers))
        jobes_y_pos = np.linspace(2, 0, len(self.all_jobs))
        pos = {
            'S': (-1, 1), 
            **{worker: (0, names_y_pos[i]) for i, worker in enumerate(self.all_workers)},
            **{worker: (1, jobes_y_pos[i]) for i, worker in enumerate(self.all_jobs)},
            'T': (2, 1)
        }

        #labels = {node: f'{node}({self.vertices_values[node]})' for node in graph.nodes()}
        nx.draw(self.nx_graph, pos, ax=ax, with_labels=True, node_size=1400,\
                node_color='skyblue', font_size=10, arrows=True, arrowsize=20)
        edge_labels = nx.get_edge_attributes(self.nx_graph, 'weight')
        nx.draw_networkx_edge_labels(self.nx_graph, pos, edge_labels=edge_labels, font_size=15)
        plt.show()
        
        
        
    def prepare_for_dfs(self):
        self.max_depth = float('inf')
        self.result = []
        
        
    def dfs_path(self, source, sink, visited, current_depth):
        if current_depth >= self.max_depth:
            return
        
        visited.append(source)
        
        if source == sink:
            self.max_depth = current_depth
            self.result = visited[::]
            #print(self.result)
            visited.pop()
            return
        
        for weight, neighbor in self.rezidual_graph[source]:
            if weight == 1 and neighbor not in visited and current_depth+1 < self.max_depth:
                self.dfs_path(neighbor, sink, visited, current_depth+1)

        visited.pop()
        
    
    
        
    def maximum_matching_manual(self):
        while(1):
            self.prepare_for_dfs()
            self.dfs_path('S', 'T', [], 0)
            
            path = self.result
            print(path)
            
            if not path:
                print("kraj")
                break
            else:
                for i in range(1, len(path)):
                    for j, (weight, node) in enumerate(self.rezidual_graph[path[i-1]]):
                        if node == path[i]:
                            self.rezidual_graph[path[i-1]][j] = (0 if weight else 1, node)
                            
                self.plot_weighted_graph()
                
            
                path = path[::-1]
                print(path)
                for i in range(1, len(path)):
                    for j, (weight, node) in enumerate(self.rezidual_graph[path[i-1]]):
                        if node == path[i]:
                            self.rezidual_graph[path[i-1]][j] = (0 if weight else 1, node)
                    
                self.plot_weighted_graph()
        
        result = 0
        print(f"there is {len(self.all_workers)} workers?")
        
        for weight, node in self.rezidual_graph['S']:
            if weight == 0:
                result+=1
                
        print(f"{result} of them got job!")
        
    
    """
    def maximum_mathing_networks(self):
        graph = nx.Graph(self.adjacency) #this needs only adjacecny between workers and jobs - no 'S' and 'T' and reverse edges

        # Find the maximum matching
        matching = nx.bipartite.maximum_matching(graph)
        
        # Check if there is a perfect matching
        is_perfect_matching = len(matching) // 2 == len(self.adjacency.keys())
        print("Is there a perfect matching?", is_perfect_matching)
        
    def plot_graph(self):
        graph = nx.DiGraph(self.adjacency)
        fig, ax = plt.subplots(figsize=(7, 7))
        
        #this is for bipartie graph
        pos = nx.bipartite_layout(graph, list(self.adjacency.keys()))
        
        nx.draw(graph, pos, ax=ax, with_labels=True, node_size=1200,\
                node_color='skyblue', font_size=15, arrows=True, arrowsize = 35)
        plt.show()
        
    def plot_residual(self):
        graph = nx.DiGraph(self.flow_graph)
        
        
        positions = {
            'S': (-1, 1), 
            'Dzon': (0, 2), 'Bob': (0, 1), 'Tsu': (0, 0), 
            'Job1': (1, 1.5), 'Job2': (1, 0.5), 
            'T': (2, 1)
        }
        
        # Plotting the graph
        fig, ax = plt.subplots(figsize=(7, 7))
        nx.draw(graph, positions, ax=ax, with_labels=True, node_size=1200, node_color='lightblue', font_size=10, arrows=True, arrowsize=20)
        plt.title("Flow Graph")
        plt.show()
    """
        
B1 = Bipartie_Graph(*Bipartie_Graph.input_memory[3])
#B1.plot_graph()
B1.plot_weighted_graph()
B1.print_graph()
B1.get_edges_for_plot()
B1.maximum_matching_manual()
#B1.maximum_mathing_networks()

        
        