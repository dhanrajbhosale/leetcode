class Solution:
    def paintWalls(self, cost: List[int], time: List[int]) -> int:
        
        memo = {}
        # we will try all possible ways. We will make decison on every ith wall, to PAINT or to SKIP.
        # so arguments are: i wall, remaining wall
        def dfs(i, remain):
            if (i, remain) in memo:
                return memo[(i, remain)]

            if remain<=0:
                return 0
            if i==len(cost): # no Solution
                return float('inf')
            
            # make 2 decisons
            paint = cost[i] + dfs(i+1, remain-1-time[i])
            skip = dfs(i+1, remain)

            memo[(i, remain)]=min(paint, skip)

            return min(paint, skip)
        
        return dfs(0, len(cost))