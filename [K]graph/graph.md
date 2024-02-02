# graph

## intro

- A graph is most commonly stored as a hashmap/list of adjacency lists/sets: for each vertex, store a list/set of its neighbors
    - how to build graph is important
    - often use
        - elements inside set can be tuples
        ```python
        graph = defaultdict(set)
        ```
    - notice: tree is a special graph with properties that
        - connected
        - acyclic
        - non-direction edges
        - one path between any two vertices/nodes

## graph dfs pattern

- DFS
    - time `O(|V| + |E|)`
    - space `O(|V|)` for visited hashset, and recursion stack (not counting building graph)
    - DFS is better at
        - searching for long paths
        - memorizing res for long paths
        - detecting cycles
    ```python
    # dfs

    graph = defaultdict(set)
    for p, q in edges:
        graph[p].add(q)

    visited = set()
    
    def dfs(node):
        visited.add(node)
        print('V:', node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(neighbor)

    dfs(start)
    ``` 

## graph bfs pattern

- BFS
    - time `O(|V| + |E|)`
    - space `O(|V|)` for visited hashset, and queue (not counting building graph)
    - tips
        - shortest distance of a to b is equal to the distance of b to a
        - sometimes can use topological sort’s idea
        - we can use hashmap or nested list or variable to help us to record some res
        - queue
            - start with single source or multi sources
            - can put tuple as element to include more info
            - can implement bfs queue by hashset sometimes
                - eg. when perform bfs on string (modifying char) might generate duplicate new string
        - visited
            - use hashset
    - BFS is better at
        - finding the shortest distance between two vertices
        - searching in graph of unknown size
        - creating a topological sort of a DAG (kahn algorithm)
    ```python
    # bfs

    graph = defaultdict(set)
    for p, q in edges:
        graph[p].add(q)

    visited = set()
    queue = deque([start])
    visited.add(start)

    while queue:
        node = queue.popleft()
        print('V:', node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)
    ```
    - patterns
        - bfs with single source
        - bfs with multiple sources
        - bfs with hashset as queue

## graph union find pattern

- Union Find
    - can use when problems involve **Union**, **Find**, or **Transitive Relation**
    - operations
        - init
        - find
        - union
        - is_connected
        - get_count
        - special ops
            - maintain the size of each components
            - give each component weight to represent the relation between itself to it’s parent

```python
class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0 for _ in range(n)]
        self.count = n
    
    # path compression
    def find(self, p):
        while p != self.parent[p]:
            self.parent[p] = self.parent[self.parent[p]]
            p = self.parent[p]
        return p

    # union by rank
    def union(self, p, q):
        root_p = self.find(p)
        root_q = self.find(q)
        if root_p == root_q:
            return
        if self.rank[root_p] > self.rank[root_q]:
            self.parent[root_q] = root_p
        elif self.rank[root_p] < self.rank[root_q]:
            self.parent[root_p] = root_q
        else:
            self.parent[root_p] = root_q
            self.rank[root_q] += 1
        self.count -= 1
        return
    
    def is_connected(self, p, q):
        return self.find(p) == self.find(q)

    def get_count(self):
        return self.count

# time near O(1) for find/union if path compression and union by rank
# space O(V), due to building uf
'''
the logic of path compression is keep checking the cur node equal to its parent or not
if yes, found the right parent, else change its parent to orginal parent's parent
and let this new parent become the cur node
then keep checking
(every round, will let cur node become at same layer with its original parent)
'''
```

## graph kahn pattern

- ****Kahn****
    - Topological sort
    - A **Directed Acyclic Graph** is a linear ordering of its vertices such that for every directed edge *pq* from vertex *p* to vertex *q*, *p* comes before *q* in the ordering
    - ****Kahn's Algorithm (like bfs)****
        1. building graph if need
        2. count every node’s in-degree
        3. put node whose in-degree is 0 inside queue
        4. pop out node and add to res list, and minus its neighbor node’s in-degree by 1
        5. if neighbor node’s in-degree is 0 put inside queue
        6. check length of res list equal to number of nodes or not (which is detecting acyclic or not)
        7. res list is a DAG when valid
    - when to use
        - determining the order in which elements should be placed to adhere to dependency constraints
- time `O(|V| + |E|)`
- space `O(|V| + |E|)`, if building graph

```python
from collections import deque
def getDAG(n, edges):
    graph = [[] for _ in range(n)]
    indegrees = [0 for _ in range(n)]
    for p, q in edges:
        graph[p].append(q)
        indegrees[q] += 1

    queue = deque([])
    for i, indegree in enumerate(indegrees):
        if indegree == 0:
            queue.append(i)
    
    res = []
    while queue:
        node = queue.popleft()
        res.append(node)
        for neighbor in graph[node]:
            indegrees[neighbor] -= 1
            if indegrees[neighbor] == 0:
                queue.append(neighbor)
                
    return res if len(res) == n else []

# time O(V+E)
# space O(V+E), due to building graph
# using graph and kahn and topological sort
```

## graph dijkstra pattern

- **Dijkstra**

```python
# dijkstra
# single source shortest path algorithm (only handle positive weight edge)
# can get shortest path from one node to all other nodes
# based on bfs and greedy

from heapq import *
from collections import defaultdict
def dijkstra(edges, V, src):
    graph = defaultdict(list)
    for u, v, w in edges:
        graph[u].append((v, w))

    node_dist = defaultdict(int)
    for i in range(V):
        node_dist[i] = float('inf')

    heap = [(0, src)]
    node_dist[src] = 0
    visited = set()
    while heap:
        prev, node = heappop(heap)
        if node in visited:
            continue
        visited.add(node)
        for next_node, weight in graph[node]:
            if prev + weight < node_dist[next_node]:
                d = prev + weight
                heappush(heap, (d, next_node))
                node_dist[next_node] = d
    return node_dist

# time O(V + E + ElogE), ElogE -> Elog(V**2) -> ElogV
# space O(V+E)
# using dijkstra
'''
1. build graph
2. init node_dist dict/array
3. init visited set
4. set init val for start node (in the node_dist)
5. init heap with start node
6. keep heappop the most promising edge/node
7. if already visited just skip, else set as visited
8. relax each edge with this node
'''
```

## graph bellman ford pattern

- **Bellman-Ford**

```python
# bellman ford
# single source shortest path algorithm (can handle negative weight edge)
# can get shortest path from one node to all other nodes
# can use it to solve shortest path problem with limited moves (O(VE) will become O(kE))
# can detect negative cycle
'''
if there is no negative cycle, 
P node to Q node's shortest path is at most V nodes and V - 1 edges, 
otherwise means this path pass same node twice (there is a negative cycle)
'''

def bellman_ford(src, dst, edges, V):
    node_dist = [float("inf") for _ in range(V)]
    node_dist[src] = 0

    for _ in range(V - 1):
        for u, v, w in edges:
            if node_dist[u] != float("inf") and node_dist[u] + w < node_dist[v]:
                node_dist[v] = node_dist[u] + w

    for u, v, w in edges:
        if node_dist[u] != float("inf") and node_dist[u] + w < node_dist[v]:
            print("contains negative cycle")
            return

    return node_dist[dst] if node_dist[dst] != float('inf') else - 1

# time O(VE)
# space O(V)
# using bellman ford
'''
1. build graph
2. init node_dist dict/array
3. set init val for start node (in the node_dist)
4. relax/update all edges in every iteration
   - will have V - 1 times iteration, 
   if we want only k iter then we need temp_node_dist for each iter,
   to guarantee the result come from last iteration
   - the logic of relax is that if you can go to u node, 
   and have a better distance to v node by using u-v edge, 
   then upddate distance for v node
5. if still have any edge can relax, then there must be a negative cycle
'''
```

## graph floyd warshall pattern

- **Floyd-Warshall**

```python
# floyd warshall
# shortest path algorithm (can handle negative weight edge)
# can get all shortest path between all pairs of nodes
# can detect negative cycle
# based on dp
# idea: go through all possible intermediate node

def floyd_warshall(edges, V):
  dist = [[float('inf') for _ in range(V)] for _ in range(V)]

  for start, end, weight in edges:
    dist[start][end] = weight
      
  for i in range(V):
      dist[i][i] = 0
      
  for mid in range(V):
      for start in range(V):
          for end in range(V):
              if dist[start][mid] + dist[mid][end] < dist[start][end]:
                  dist[start][end] = dist[start][mid] + dist[mid][end]
  return dist

# time O(V**3)
# space O(V**2)
# using floyd warshall
'''
1. init distance's dp table (every dist is float('inf'))
2. put every edges weight inside table (u to v)
3. put every node to itself distance(0) in table too
4. thrice for loop (mid point, start node, end node) and relax
   the logic is we want to fill in a mid node to any two nodes
   try to know this mid node can benefit for shortest path bewteen that two nodes or not
   notice the idx of iter, also represent cur shortest path's intermediate node's number (of any two nodes)
5. detect negative cycle: re-run step 4, if still get better res then exists a negative cycle
'''
```

## graph kruskal pattern

- **Kruskal**

```python
# kruskal
# can find minimum spanning tree
# based on union find and greedy
'''
A minimum spanning tree (MST) is a subset of the edges of a connected, 
edge-weighted undirected graph that connects all the vertices together, 
without any cycles and with the minimum possible total edge weight

Kruskal's algorithm generates the Minimum Spanning Tree 
by always choosing the smallest weigthed edge in the graph 
and consistently growing the tree by one edge
'''
def kruskal(n, edges):
    edges.sort(key = lambda x: x[2])
    uf = UnionFind(n)
    mst = []
    for u, v, w in edges:
        if not uf.is_connected(u, v):
            uf.union(u, v)
            mst.append((u, v, w))
    return mst if len(mst) == n - 1 else []

# time O(ElogE)
# space O(E + V)
# using kruskal and union find
'''
1. sort edges
2. init union find for all nodes
3. keep adding lowest-weighted edge to mst that connects two components withnot forming cycle
   also union these two components
   (until connected n - 1 edges)
4. check mst's size (if size is n - 1 then the mst is valid)
'''
```

## graph tarjan pattern

- **Tarjan**
    - can find SCC in directed graph (below’s code)
    - can find critical edges or critical vertices in undirected graph
        - critical edges [u, v]
            - if low[u] > ids[v]
        - critical vertices [u]
            - if low[v] >= ids[u]

```python
'''
A directed graph is strongly connected if there is a path between all pairs of vertices

A strongly connected component (SCC) of a directed graph is a maximal strongly connected subgraph

tarjan is based on dfs
'''

from collections import defaultdict
class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)
        self.time = 0
        self.scc = 0
  
    def addEdge(self, u, v):
        self.graph[u].append(v)

    def tarjan(self):
        ids = [- 1] * (self.V)
        low = [- 1] * (self.V)
        onStack = [False] * (self.V)
        stack = []
        
        for i in range(self.V):
            if ids[i] == - 1:
                self.dfs(i, ids, low, onStack, stack)
        return low
         
    def dfs(self, node, ids, low, onStack, stack):
        ids[node] = self.time
        low[node] = self.time
        self.time += 1
        onStack[node] = True
        stack.append(node)
 
        for neighbor in self.graph[node]:
            if ids[neighbor] == - 1:
                self.dfs(neighbor, ids, low, onStack, stack)
                low[node] = min(low[node], low[neighbor])
                         
            elif onStack[neighbor]:
                low[node] = min(low[node], ids[neighbor])

        while low[node] == ids[node]:
            stack_node = stack.pop()
            onStack[stack_node] = False
            if stack_node == node:
                self.scc += 1
                break

# time O(V + E)
# space O(V)
# using tarjan
```

## graph hierholzer pattern

- **Hierholzer**
    - all non zero degree nodes need to be in same connected component

|                  | Eulerian Circuit                                                                   | Eulerian Path                                                                                                                                                    |
| ---------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Undirected Graph | even degree for every vertex (can start and end at any same node)                  | even degree for every vertex, or odd degree for two vertices (will be start and end nodes) and rest is even degree                                               |
| Directed Graph   | equal indegree and outdegree for every vertex (can start and end at any same node) | equal indegree and outdegree for every vertex, or one vertex (out == in + 1) (start node) and one vertex(in == out + 1) (end node) and rest has equal(in == out) |

```python
'''
1. build graph, and count all nodes' in and out degree, 
and check eulerian path exist or not

2. find start node, and perform modified dfs

3. once node is stuck (no unvisited outgoing edge), 
add node to stack and backtrack

4. when backtracking, if node has unvisited outgoing edge, 
call dfs
'''
from collections import defaultdict
def hierholzer(n, edges):
    E = len(edges)
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)

    indegrees = [0] * n
    outdegrees = [0] * n
    for start in graph:
        for end in graph[start]:
            outdegrees[start] += 1
            indegrees[end] += 1

    start_nodes = 0
    end_nodes = 0
    for i in range(n):
        if abs(indegrees[i] - outdegrees[i]) > 1:
            return []
        elif indegrees[i] - outdegrees[i] == 1:
            end_nodes += 1
        elif outdegrees[i] - indegrees[i] == 1:
            start_nodes += 1

    if start_nodes == 0 and end_nodes == 0:
        pass
    elif start_nodes == 1 and end_nodes == 1:
        pass
    else:
        return []

    start = 0
    for i in range(n):
        if outdegrees[i] - indegrees[i] == 1:
            start = i
            break
        if outdegrees[i] > 0:
            start = i
            
    stack = []
    def dfs(node):
        while outdegrees[node]:
            neighbor = graph[node].pop()
            outdegrees[node] -= 1
            dfs(neighbor)
        stack.append(node)
        
    dfs(start)

    path = []
    while stack:
        path.append(stack.pop())

    if len(path) == E + 1:
        return path
    return []

# time O(V + E)
# space O(V + E)
# using hierholzer
```

## graph matrix pattern

- Matrix
    - tips
        - hashset for recording visited or not
        - cur ptr moving direction
        - swap based on certain line across the matrix
        - additional sign variables for storing
        - or use first row and first col to store sth
    - elements
        - row
        - col
        - diag
            - row - col
            - row == col (main diag)
        - anti_diag
            - row + col
            - row + col == row - 1 == col - 1 (main anti_diag)
