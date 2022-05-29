import numpy as np

class Solution:
    def findPath(self, i, j, m, n, cnt)-> int:
        if i==m or j==n: return 1
        if cnt[i][j]!=0: return cnt[i][j]            
        cnt[i][j]=self.findPath(i+1,j,m,n, cnt)+self.findPath(i,j+1,m,n, cnt)
        return cnt[i][j]
        
    def uniquePaths(self, m: int, n: int) -> int:
        cnt=np.zeros((m,n),dtype=int)
        return self.findPath(0,0,m-1,n-1, cnt)
        