# Total Degree of graph = 2 * number of edges
# In a Directed Graph, there are two more terms: Indegree & Outdegree

# Generally we're given n(total nodes) and m(total edges) and an edge list

# How can we store Graph?
# 2 ways: (a)Matrix and (b)List

# Matrix means an Adjecncy Matrix

n = 8
A = [[0, 1], [1, 2], [0, 3], [3, 4], [3, 6], [3, 7], [4, 2], [4, 5], [5, 2]] # [Start, End]

# Convert Array of Edges -> Adjecency Matrix        (Method 1)    - Space: O(n*n)

# Initialize adjacency matrix with zeros
graph = [[0 for _ in range(n)] for _ in range(n)]
# print(graph)

# function to add edge
def add_edge(u,v):
   graph[u][v] = 1
   graph[v][u] = 1   # remove this line if graph is Directed

# add_edge(0,1)
# add_edge(1,2)
# add_edge(0,3)
# or 
for u, v in A:
   # graph[u][v] = 1
   add_edge(u,v)

print("Adjecency Matrix:")
for row in graph:
   print(row)

#       [[0, 1, 0, 1, 0, 0, 0, 0],
#        [0, 0, 1, 0, 0, 0, 0, 0],
#        [0, 0, 0, 0, 0, 0, 0, 0],
#        [0, 0, 0, 0, 1, 0, 1, 1],
#        [0, 0, 1, 0, 0, 1, 0, 0],
#        [0, 0, 1, 0, 0, 0, 0, 0],
#        [0, 0, 0, 0, 0, 0, 0, 0],
#        [0, 0, 0, 0, 0, 0, 0, 0]]


# Convert Array of Edges -> Adjecency List        (Method 2)    - Space: O(2E) - Optimized

from collections import defaultdict
D = defaultdict(list)

def add_edge_optimized(u,v):
   D[u].append(v)
   D[v].append(u)    # remmove this if the graph is Directed

# add_edge_optimized(0,1)
# add_edge_optimized(1,2)
# add_edge_optimized(0,3)
# or 
for u,v in A:
   D[u].append(v)

# print(D)    #    {0: [1, 3], 1: [2], 3: [4, 6, 7], 4: [2, 5], 5: [2]}
# print(D[3])     #   [4, 6, 7]



# How to store Weighted Graph?

# Adjecency Matrix
# here we store the weight instead of 1
def add_weighted_edge(u, v, weight):
    graph[u][v] = weight
    graph[v][u] = weight  # remove this line if directed graph

add_weighted_edge(0, 1, 10)
add_weighted_edge(0, 2, 6)
add_weighted_edge(1, 3, 5)


# Adjecency List
# here we have to store in pair like {0: [(1,2), (3,6)], 1: [(2,4)]} - { node : [(node, weight)] }


def add_weighted_edge_optimized(u, v, w):
    graph[u].append((v, w))
    graph[v].append((u, w))  # remove for directed

add_weighted_edge_optimized(0, 1, 10)
add_weighted_edge_optimized(0, 2, 6)
add_weighted_edge_optimized(1, 3, 5)


# Connected Components
# Visited Array