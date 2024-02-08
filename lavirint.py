import numpy as np
from collections import deque
import heapq

class labyrinth:
    #inputs
    input_memory_obsticles = {    
        0:([2,1,4], [0,1,3], [2,3,4], [2,1,3]),
        1:([0,3], [2,0], [2,4], [4,1]),
        2:([0,4,1,4,1,1,5,5,3], [1,1,7,7,2,5,2,5,3],\
           [2,5,2,6,1,1,5,5,3], [1,1,7,7,3,6,3,6,5]),
        3:([2,2], [0, 3], [2, 2], [1, 4]),
        4:([],[],[],[])
        }
    input_memory_dimensions = {
        0:(4,6),
        1:(5,5),
        2:(9,7),
        3:(5,6), 
        4:(4,6)
        }
    
    def __init__(self, N, M):
        #labyrinth
        self.N = N #number of rows
        self.M = M #number of columns
        self.labyrinth = np.zeros((N, M))
        self.labyrinth[0][0] = 304 #start
        self.labyrinth[N-1][M-1] = 707 #end
        
        #search
        self.directions = [(1, 0), (0, 1), (0, -1), (-1, 0)]
        
    def prepare(self):
        self.visited = set()
        self.rezult = float('inf')
        self.search_tree = []
        self.number_of_squeres_visited = 0
    
    def analysis(self):
        print(f"Result is: {self.rezult}")
        #print(f"Searched: {self.search_tree}")
        print(f"Number of searched squares: {self.number_of_squeres_visited}")
    
    def add_obsticles(self, X1, Y1, X2, Y2):
        for i in range(len(X1)):
            self.labyrinth[Y1[i]:Y2[i]+1, X1[i]:X2[i]+1] = 1.0
    
    def print_labyrinth(self):
        print(self.labyrinth)
        
    def dfs_recursive_pruning(self, current, path):
        if current[0] == -1 or current[1] == -1 or current[0] == self.N or current[1] == self.M\
            or self.labyrinth[current] == 1 or current in self.visited or path > self.rezult:
            return
        
        
        self.visited.add(current)
        self.number_of_squeres_visited += 1
        
        
        if current == (self.N-1, self.M-1):
            self.rezult = min(self.rezult, path)
        
        for dx, dy in self.directions:
            self.dfs_recursive_pruning((current[0] + dx, current[1] + dy), path+1)
            
        self.visited.remove(current)
        
        
    def bfs(self, current, path):
        dq = deque()
        dq.append((current, path))
        
        while(dq):
            current, path = dq.popleft()
            
            self.number_of_squeres_visited += 1
            self.visited.add(current)
            
            if self.labyrinth[current[0]][current[1]] == 707:
                self.rezult = path
                return
            
            for dx, dy in self.directions:
                if current[0]+dx == -1 or current[1]+dy == -1 or current[0]+dx == self.N or current[1]+dy == self.M\
                    or self.labyrinth[current[0]+dx][current[1]+dy] == 1 or (current[0] + dx, current[1] + dy) in self.visited:
                    continue
                dq.append(((current[0]+dx, current[1]+dy), path+1))
        
        
    def A_star_Manhattan(self, current, path):
        heap = [(self.N + self.M - 2, self.N + self.M - 2, current, path)]
        heapq.heapify(heap)
        
        while(heap):
            cost, manhattan, current, path = heapq.heappop(heap)
            
            self.number_of_squeres_visited += 1
            self.visited.add(current)
            
            if self.labyrinth[current] == 707:
                self.rezult = path
                return
            
            for dx, dy in self.directions:
                if current[0]+dx == -1 or current[1]+dy == -1 or current[0]+dx == self.N or current[1]+dy == self.M\
                    or self.labyrinth[current[0]+dx][current[1]+dy] == 1 or (current[0] + dx, current[1] + dy) in self.visited:
                    continue
                heapq.heappush(heap, (path + 1 + manhattan - dx - dy, manhattan - dx - dy , (current[0]+dx, current[1]+dy), path+1))
        
    
L1 = labyrinth(*labyrinth.input_memory_dimensions[4])
L1.add_obsticles(*labyrinth.input_memory_obsticles[4])
L1.print_labyrinth()
L1.prepare()
L1.A_star_Manhattan((0,0), 0)
L1.analysis()










    
        

