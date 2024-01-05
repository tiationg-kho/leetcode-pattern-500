from collections import defaultdict
class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        user_visits = defaultdict(list)
        for u, t, w in zip(username, timestamp, website):
            user_visits[u].append((t, w))

        pattern_freq = defaultdict(int)
        for u, visits in user_visits.items():
            sort_visits = sorted(visits)
            pattern_set = set()
            for i in range(len(sort_visits) - 2):
                for j in range(i + 1, len(sort_visits) - 1):
                    for k in range(j + 1, len(sort_visits)):
                        pattern = (sort_visits[i][1], sort_visits[j][1], sort_visits[k][1])
                        if pattern in pattern_set:
                            continue
                        pattern_set.add(pattern)
                        pattern_freq[pattern] += 1
        
        res = []
        max_freq = max(pattern_freq.values())
        for p, f in pattern_freq.items():
            if f == max_freq:
                res.append(p)
        res.sort()
        
        return list(res[0])
                        
# time O(m * n**3), m is the number of users and n is the number of websites, not count sorting the potential res
# space O(m * n**3), due to combinations
# using hashmap and store sth’s freq and sort and combinations
'''
1. same user can only contribute to one pattern once
'''