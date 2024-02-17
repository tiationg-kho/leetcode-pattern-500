class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0 for _ in range(n)]

    def find(self, p):
        while p != self.parent[p]:
            self.parent[p] = self.parent[self.parent[p]]
            p = self.parent[p]
        return p
    
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

    def is_connected(self, p, q):
        return self.find(p) == self.find(q)

class Solution:
    def areSentencesSimilarTwo(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        if len(sentence1) != len(sentence2):
            return False
        id = 0
        word_id = {}
        for w1, w2 in zip(sentence1, sentence2):
            if w1 not in word_id:
                word_id[w1] = id
                id += 1
            if w2 not in word_id:
                word_id[w2] = id
                id += 1
        for w1, w2 in similarPairs:
            if w1 not in word_id:
                word_id[w1] = id
                id += 1
            if w2 not in word_id:
                word_id[w2] = id
                id += 1
        uf = UnionFind(id)
        for w1, w2 in similarPairs:
            uf.union(word_id[w1], word_id[w2])
        for w1, w2 in zip(sentence1, sentence2):
            if not uf.is_connected(word_id[w1], word_id[w2]):
                return False
        return True
            
# time O(n + P)
# space O(n + P)
# using graph and union find and hashmap