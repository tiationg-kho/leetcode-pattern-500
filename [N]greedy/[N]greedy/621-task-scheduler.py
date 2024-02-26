from collections import defaultdict
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_freq = defaultdict(int)
        for t in tasks:
            task_freq[t] += 1
        max_freq = max(task_freq.values())
        tasks_with_max_freq = []
        for t, f in task_freq.items():
            if f == max_freq:
                tasks_with_max_freq.append(t)
        
        h = max_freq - 1
        w = n + 1
        res = h * w + len(tasks_with_max_freq)
        return res if res > len(tasks) else len(tasks)

# time O(n)
# space O(1), due to task's category
# using greedy and hashmap