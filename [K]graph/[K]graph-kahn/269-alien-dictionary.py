from collections import deque
class Solution:
    def alienOrder(self, words: List[str]) -> str:
        graph = {}
        indegrees = {}
        for word in words:
            for c in word:
                graph[c] = set()
                indegrees[c] = 0

        for i in range(1, len(words)):
            w1 = words[i - 1]
            w2 = words[i]
            diff = False
            for j in range(min(len(w1), len(w2))):
                c1 = w1[j]
                c2 = w2[j]
                if c1 != c2:
                    if c2 not in graph[c1]:
                        graph[c1].add(c2)
                        indegrees[c2] += 1
                    diff = True
                    break
            if not diff and len(w1) > len(w2):
                return ''
        
        queue = deque([])
        for i, indegree in indegrees.items():
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
        return ''.join(res) if len(res) == len(indegrees) else ''
    
# time O(nL)
# space O(nL), due to building graph
# using graph and kahn and topological sort