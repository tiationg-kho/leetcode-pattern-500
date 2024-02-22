class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        jobs = jobDifficulty
        n = len(jobs)
        if n < d:
            return - 1
        if n == d:
            return sum(jobs)

        dp = [[float('inf') for _ in range(d + 1)] for _ in range(n)]
        max_job = jobs[0]
        for i in range(n):
            if jobs[i] > max_job:
                max_job = jobs[i]
            dp[i][1] = max_job
        
        for end in range(n):
            for interval in range(2, d + 1):
                max_job = jobs[end]
                for cut in range(end, interval - 2, - 1):
                    max_job = max(max_job, jobs[cut])
                    dp[end][interval] = min(dp[end][interval], dp[cut - 1][interval - 1] + max_job)
        
        return dp[n - 1][d]
    
# time O(n**2 * k)
# space O(nk)
# using dynamic programming and interval (start from one interval)