class Solution:
    # precompute product of prefixes and suffixes
    # similar to 238. Product of Array Except Self
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        N, M = len(grid), len(grid[0])
        prefix_prod = [1]*(N*M)
        suffix_prod = [1]*(N*M)
        preProd = 1        
        for i in range(N):
            for j in range(M):
                k = i*M+j
                prefix_prod[k] = preProd 
                preProd = (preProd*grid[i][j])%12345
        preProd = 1    
        for i in reversed(range(N)):
            for j in reversed(range(M)):
                k = i*M+j
                suffix_prod[k] = preProd 
                preProd = (preProd*grid[i][j])%12345
        
        for i in range(N):
            for j in range(M):
                k = i*M+j
                grid[i][j]=prefix_prod[k]*suffix_prod[k]%12345
        return grid