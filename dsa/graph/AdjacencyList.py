from collections import deque

class Graph:
    def __init__(self):
        self.adjList={}

    def add_vertex(self, vertex):
        if vertex not in self.adjList:
            self.adjList[vertex]=[]

    def addEdge(self,src, dest):
        self.add_vertex(src)
        self.add_vertex(dest)

        self.adjList[src].append(dest)
        self.adjList[dest].append(src)

    def dfs(self, src):
        visited = [False] * self.size
        stack = [src]

        while stack:
            v = stack.pop()

            if(visited[v] == False):
                print(v, end="->")
                visited[v] = True

            for i in range(self.size):
                if(self.mat[v][i] ==1 and visited[i] == False):
                    stack.append(i)

    def bfs(self, src):
        visited = [False] * self.size
        queue = deque([src])
        visited[src] = True

        while queue:
            v = queue.popleft()
            print(v, end="->")

            for i in range(self.size):
                if(self.mat[v][i] == 1 and visited[i] == False):
                    visited[i] = True
                    queue.append(i)


    def printGraph(self):
        for vertex in self.adjList:
            print(vertex, " -> ", self.adjList[vertex] , end="\n")

g = Graph()
g.addEdge(1,2)
g.addEdge(2,3)
g.addEdge(1,4)
g.addEdge(4,3)
g.addEdge(2,4)
g.addEdge(4,5)
g.addEdge(3,5)

g.printGraph()