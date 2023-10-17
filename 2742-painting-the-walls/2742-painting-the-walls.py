class Solution:
    # Bottom-Up Dynamic Programming
    def paintWalls(self, cost: List[int], time: List[int]) -> int:
        N = len(cost)
        # iterate i from n-1 to 0
        # iterate remain from 0 to n-1
        dp = [[0]*(N+1) for _ in range(N+1)]

        for i in range(1, N + 1):
            dp[N][i] = float('inf')

        for i in reversed(range(N)):
            for remain in range(1, N+1):
                # two decison
                paint = cost[i] + dp[i+1][max(0, remain - 1 - time[i])]
                skip = dp[i+1][remain]
                dp[i][remain] = min(paint, skip)

        return dp[0][N]

    # # Top-Down Dynamic Programming
    # def paintWalls(self, cost: List[int], time: List[int]) -> int:
        
    #     memo = {}
    #     # we will try all possible ways. We will make decison on every ith wall, to PAINT or to SKIP.
    #     # so arguments are: i wall, remaining wall
    #     def dfs(i, remain):
    #         if (i, remain) in memo:
    #             return memo[(i, remain)]

    #         if remain<=0:
    #             return 0
    #         if i==len(cost): # no Solution
    #             return float('inf')
            
    #         # make 2 decisons
    #         paint = cost[i] + dfs(i+1, remain-1-time[i])
    #         skip = dfs(i+1, remain)

    #         memo[(i, remain)]=min(paint, skip)

    #         return min(paint, skip)
        
    #     return dfs(0, len(cost))