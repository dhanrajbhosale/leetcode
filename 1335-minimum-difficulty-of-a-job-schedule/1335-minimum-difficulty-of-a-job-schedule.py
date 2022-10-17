class Solution:

    def minDifficulty(self, A, d):
        n = len(A)
        if n < d: return -1
        
        dp=[[-1 for _ in range(n)] for _ in range(d+1)]
        
        # @cache
        # @functools.lru_cache()
        def dfs(i, d):
            if d == 1:
                return max(A[i:])
            if dp[d][i]!=-1:
                return dp[d][i]
            res, maxd = float('inf'), 0
            for j in range(i, n - d + 1):
                maxd = max(maxd, A[j])
                res = min(res, maxd + dfs(j + 1, d - 1))
            dp[d][i]=res
            return res
        return dfs(0, d)