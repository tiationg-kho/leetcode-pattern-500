"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""
from collections import deque
class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        id_employee = {}
        for e in employees:
            id_employee[e.id] = e

        res = 0
        queue = deque([id_employee[id]])
        while queue:
            node = queue.popleft()
            res += node.importance
            for subordinate in node.subordinates:
                queue.append(id_employee[subordinate])
        return res
        
# time O(n)
# space O(n)
# using tree and bfs and tree's idea and building graph