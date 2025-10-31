# BFS - (Queue-FIFO)   ---> TC: O(V+E), SC: O(N)

# Given a Starting node
# REMEMBER --> depending on the starting node the traversal will change
"""
      1
  2       6 
3   4   7   8
      5

if this is the graph and the start_node = 1,
   then 1 is at the level-0 & BFS traversal -> [1, 2, 6, 3, 4, 7, 8,5]
if this is the graph and the start_node = 6,
   then 6 is at level-0 & BFS traversal -> [6, 1, 7, 8, 2, 5, 3, 4]

"""


from collections import defaultdict, deque

# Step 1: Input the graph
V = int(input("Enter number of vertices: "))
E = int(input("Enter number of edges: "))

# adjacency list representation
graph = defaultdict(list)

print("Enter each edge as: u v (space separated)")
for _ in range(E):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)  # remove if directed graph

# Step 2: BFS function
def bfs(start, adj):
    seen = set()
    q = deque([start])
    seen.add(start)

    print("\nBFS Traversal starting from node", start, ":")
    while q:
        node = q.popleft()
        print(node, end=" -> ")
        for nei_node in adj[node]:
            if nei_node not in seen:
                seen.add(nei_node)
                q.append(nei_node)
    print("END")

# Step 3: Choose start node and run BFS
start = int(input("\nEnter starting node for BFS: "))
bfs(start, graph)
