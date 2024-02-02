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
        
from collections import defaultdict
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        n = len(accounts)
        uf = UnionFind(n)
        email_id = {}
        for i, info in enumerate(accounts):
            for j in range(1, len(info)):
                if info[j] in email_id:
                    uf.union(i, email_id[info[j]])
                else:
                    email_id[info[j]] = i

        id_emails = defaultdict(set)
        for email, id in email_id.items():
            id_emails[uf.find(id)].add(email)
        
        res = []
        for id, emails in id_emails.items():
            info = [accounts[id][0]]
            info.extend(sorted(emails))
            res.append(info)
        return res
    
# time O(mlogm + n + m), due to sort
# space O(m+n), due to hashmap, m is the number of mails, n is the number of accounts
# using graph and union find and sort