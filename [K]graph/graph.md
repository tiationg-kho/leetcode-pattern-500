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
        - get_component_weight
        - special ops
            - give each component weight to represent the relation between itself to it’s parent

```python
class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0 for _ in range(n)]
        self.weight = [1 for _ in range(n)]
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
            self.weight[root_p] += self.weight[root_q]
            self.weight[root_q] = 0
        elif self.rank[root_p] < self.rank[root_q]:
            self.parent[root_p] = root_q
            self.weight[root_q] += self.weight[root_p]
            self.weight[root_p] = 0
        else:
            self.parent[root_p] = root_q
            self.rank[root_q] += 1
            self.weight[root_q] += self.weight[root_p]
            self.weight[root_p] = 0
        self.count -= 1
        return
    
    def is_connected(self, p, q):
        return self.find(p) == self.find(q)

    def get_count(self):
        return self.count

    def get_component_weight(self, p):
        return self.weight[self.find(p)]

# time near O(1) for find/union if path compression and union by rank
# space O(V), due to building uf
# using graph and union find
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
    node_dist[src] = 0

    heap = [(0, src)]
    heapify(heap)

    visited = set()

    while heap:
        prev, node = heappop(heap)
        if node in visited:
            continue
        visited.add(node)
        for next_node, weight in graph[node]:
            d = prev + weight
            if d < node_dist[next_node]:
                heappush(heap, (d, next_node))
                node_dist[next_node] = d
    return node_dist

# time O(V + E + ElogE), ElogE -> Elog(V**2) -> ElogV
# space O(V+E)
# using graph and dijkstra
'''
1. init graph
2. init node_dist dict/array (and set val for start node)
3. init heap with start node
4. init visited set
5. keep heappop the most promising edge/node
6. if already visited just skip, else set as visited
7. relax each edge with this node
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
# based on dp
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
# using graph and bellman ford
'''
1. build graph
2. init node_dist dict/array (and set val for start node)
3. relax/update all edges in every iteration
   - will have V - 1 times iteration, 
   if we want only have k iter then we need temp_node_dist for each iter,
   to guarantee the result come from last iteration and record cur iteration only
   - the logic of relax is that if you can go to u node, 
   and have a better distance to v node by using u-v edge, 
   then upddate distance for v node
4. if still have any edge can relax, then there must be a negative cycle
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
# using graph and floyd warshall
'''
1. init distance dp table (set val for each edge and each node itself)
2. thrice for loop (mid point, start node, end node) and relax
   - the logic is we want to fill in a mid node to any two nodes
   - try to know this mid node can benefit for shortest path bewteen that two nodes or not
3. detect negative cycle: re-run step 2, if still get better res then exists a negative cycle
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
# using graph and kruskal and union find
'''
1. sort edges
2. init union find for all nodes
3. keep adding lowest-weighted edge to mst that connects two components withnot forming cycle by union
4. check mst's size (if size is n - 1 then the mst is valid)
'''
```

## graph tarjan pattern

- **Tarjan**
    - can find SCC in directed graph
        - strongly connected
            - a directed graph is strongly connected if there is a path between all pairs of vertices
        - strongly connected component (SCC)
            - a SCC of a directed graph is the maximal strongly connected subgraph
        - low link value
            - low link value of a node is the smallest index of any node reachable from that node, including itself
    - can find critical edges in undirected graph
        - critical edges [p, q]
            - if low[q] > ids[p]
    - tarjan is based on dfs

```python
# tarjan
from collections import defaultdict
class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)
        self.time = 0
        self.scc = 0

    def addEdges(self, edges):
        for p, q in edges:
            self.graph[p].append(q)

    def tarjan(self):
        ids = [- 1 for _ in range(self.V)]
        low = [- 1 for _ in range(self.V)]
        on_stack = [False for _ in range(self.V)]
        stack = []

        for i in range(self.V):
            if ids[i] == - 1:
                self.dfs(i, ids, low, on_stack, stack)
        print("low: ", low)
        return low

    def dfs(self, node, ids, low, on_stack, stack):
        ids[node] = self.time
        low[node] = self.time
        self.time += 1
        on_stack[node] = True
        stack.append(node)

        for neighbor in self.graph[node]:
            if ids[neighbor] == - 1:
                self.dfs(neighbor, ids, low, on_stack, stack)
                low[node] = min(low[node], low[neighbor])

            elif on_stack[neighbor]:
                low[node] = min(low[node], ids[neighbor])

        if low[node] == ids[node]:
            component = []
            while stack:
                stack_node = stack.pop()
                on_stack[stack_node] = False
                component.append(stack_node)
                if stack_node == node:
                    self.scc += 1
                    print("SCC: ", component)
                    break
            
g = Graph(8)
edges = [(1, 0),(1, 2),(2, 3),(3, 1),(1, 4),(4, 1),(3, 5),(4, 5),(4, 7),(5, 7),(5, 6),(6, 5)]
g.addEdges(edges)
g.tarjan()
'''
SCC:  [0]
SCC:  [7]
SCC:  [6, 5]
SCC:  [4, 3, 2, 1]
low:  [0, 1, 1, 1, 1, 4, 4, 5]

0 ← 1 ⇆ 4 → 7
    ↓ ↖     ↑
    2 → 3 → 5
            ⇅
            6
'''
# time O(V + E)
# space O(V)
# using graph and tarjan
'''
1. start DFS from every node that hasn't been visited
2. if the neighbor hasn't been visited, call dfs to visit the neighbor. update the low link val for cur node (to the minimum of its cur low link val and the low link val of the neighbor)
3. if the neighbor is in the stack, it's a back edge (means cycle exists). update the low link val for cur node (to the minimum of its cur low link val and the neighbor's id)
4. after visiting all neighbors, if the cur node's id is equal to its low link val, it's the root of an SCC
'''
```

## graph hierholzer pattern

- **Hierholzer**
    - can find an Eulerian path or circuit in a connected graph
        - Eulerian path is a path that visits every edge of a graph exactly once
        - Eulerian circuit is an Eulerian path that starts and ends on the same node
    - is based on dfs

|                  | Eulerian Circuit                              | Eulerian Path                                                                                                                                                     |
| ---------------- | --------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Undirected Graph | **even** degree for every vertex              | **even** degree for every vertex. or **odd** degree for two vertices (will be start and end nodes) and rest is **even** degree                                    |
| Directed Graph   | equal indegree and outdegree for every vertex | equal indegree and outdegree for every vertex. or one vertex (out == in + 1) (start node) and one vertex(in == out + 1) (end node) and rest has equal (in == out) |

```python
# hierholzer
from collections import defaultdict
def hierholzer(n, edges):
    E = len(edges)
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)

    indegrees = [0 for _ in range(n)]
    outdegrees = [0 for _ in range(n)]
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
        print(path)
        return path
    return []
            
edges = [(0, 1),(1, 2),(2, 0),(1, 3),(3, 4),(4, 1),(2, 4),(4, 5),(5, 2)]
hierholzer(6, edges)
'''
[5, 2, 4, 1, 2, 0, 1, 3, 4, 5]

 ↙ 0 ↖
1  →  2
↓ ↖ ↙ ↑
3 →4→ 5
'''
# time O(V + E)
# space O(V + E)
# using graph and hierholzer
'''
1. build graph, and count all nodes' in/out degree

2. check eulerian path exist or not

3. find start node, and perform modified dfs (which will delete edge when visiting)

    1. in dfs, if node has unvisited outgoing edge, call another dfs
    
    2. once node is stuck (no unvisited outgoing edge), add node to stack

4. start node is the first node pop out from stack
'''
```

## graph matrix pattern

- Matrix
    - tips
        - hashset for recording visited or not
        - cur ptr moving direction
        - swap based on certain line across the matrix
        - additional sign variables for storing
        - use first row and first col to store sign
    - elements
        - row
        - col
        - diag
            - row - col
            - row == col (main diag)
        - anti_diag
            - row + col
            - row + col == row - 1 == col - 1 (main anti_diag)
