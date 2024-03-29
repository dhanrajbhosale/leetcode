import numpy as np

class Solution:
    # Sol 1 recusrssive with dp
    
    # def findPath(self, i, j, m, n, cnt)-> int:
    #     if i==m or j==n: return 1
    #     if cnt[i][j]!=0: return cnt[i][j]            
    #     cnt[i][j]=self.findPath(i+1,j,m,n, cnt)+self.findPath(i,j+1,m,n, cnt)
    #     return cnt[i][j]
        
    # def uniquePaths(self, m: int, n: int) -> int:
    #     cnt=np.zeros((m,n),dtype=int)
    #     return self.findPath(0,0,m-1,n-1, cnt)
    
    # Sol 2 Mathematical 
    #     m-1 + n-1 total steps = m+n-2
    #     M-1 steps must be down
    #     N-1 steps must be to right 
    # So total ways, select m-1 down steps position from total steps
    
    # def uniquePaths(self, m: int, n: int) -> int:
    #     return math.comb(m + n - 2, m - 1)
        
    # Sol 3 
    
    def uniquePaths(self, m: int, n: int) -> int: 
        dp = [[1] * m for _ in range(n)] # border will have only 1 way
        for i in reversed(range(n - 1)):
            for j in reversed(range(m - 1)):
                dp[i][j] = dp[i + 1][j] + dp[i][j + 1]
        return dp[0][0]
        
        
        