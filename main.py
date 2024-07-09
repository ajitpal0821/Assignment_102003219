
### 2. `main.py`

###python
"""
Assignment: Implement the most efficient algorithm to solve the given problem.

Problem Statement:
You are given a Directed Acyclic Graph (DAG) with `n` nodes, numbered from `0` to `n-1`.
The graph is represented as an adjacency list where `graph[i]` is a list of tuples `(j, w)`,
representing an edge from node `i` to node `j` with weight `w`. Your task is to find the longest
path in the graph starting from any node.

Function Signature:
def longest_path(graph: list) -> int:

Parameters:
- graph (list): A list of lists, where `graph[i]` contains tuples `(j, w)` representing an edge
  from node `i` to node `j` with weight `w`.

Returns:
- int: The length of the longest path in the graph.

Example:
>>> graph = [
...     [(1, 3), (2, 2)],
...     [(3, 4)],
...     [(3, 1)],
...     []
... ]
>>> longest_path(graph)
7
"""

def longest_path(graph: list) -> int:
    # Your implementation goes 
    topo_order=topological_sort(graph)
    return calculate_longest_path(graph,topo_order)
    
    

# Helper function to perform topological sort
def topological_sort(graph):
    # Your implementation goes here
    visited=[False]*len(graph)
    stack=[]

    # dfs function for traversing graph
    def dfs(v):
        visited[v]=True
        if len(graph[v])==0:
            return
        for neighbor,_ in graph[v]:
            if not visited[neighbor]:
                dfs(neighbor)

        stack.append(v)
    


    for i in range(len(graph)):
        if not visited[i]:
            dfs(i)

    #returning reversed stack
    return stack[::-1]

    

# Function to calculate longest path using topological sort
def calculate_longest_path(graph, topo_order):
    
    # declare dist with minimum value as we need longest/maximum path
    dist =[-float('inf')]*len(graph)

    #make start node distance as zero
    dist[topo_order[0]]=0

    for u in topo_order:
        if dist[u]!=-float('inf'):
            for v,weight in graph[u]:
                if dist[v]<dist[u]+weight:
                    dist[v]=dist[u]+weight
    
    return max(dist)
    
