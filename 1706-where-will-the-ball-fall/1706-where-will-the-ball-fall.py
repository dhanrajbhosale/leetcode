class Solution:
    
    def findBall(self, grid: List[List[int]]) -> List[int]:
        nrows = len(grid)
        ncols = len(grid[0])
        
        # i = row, j= ball pos
        def candrop(i,j):
            if i == nrows: return j # Ball falls out of bottom
            if j == ncols-1 and grid[i][j] == 1: return -1 # Ball hits right wall due to a l2r-leaning slat
            if j == 0 and grid[i][j] == -1: return -1 # Ball hits left wall due to a r2l-leaning slat
            if grid[i][j] == 1 and grid[i][j+1] == -1: return -1 # Ball lands in a V after rolling right
            if grid[i][j] == -1 and grid[i][j-1] == 1: return -1 # Ball lands in a V after rolling left
            return candrop(i+1,j+grid[i][j]) # No end case, continue by increasing y-coord by one and x-coord by 1 or -1 depending on roll direction.
        
        return [candrop(0,j) for j in range(ncols)]

    
    
    
# 61 / 64 test cases passed.
#     def findBall(self, grid: List[List[int]]) -> List[int]:
#         m, n = len(grid), len(grid[0])
#         ballPos = [i for i in range(n)]
        
#         # update ball pos for each row
#         for i in range(m):
#             print(ballPos)
#             for j in range(n):
#                 # check if it's stuck
                
#                 if ballPos[j]>0 and ballPos[j]<n-1 and ((grid[i][ballPos[j]]==1 and grid[i][ballPos[j]+1]==-1) or (grid[i][ballPos[j]]==-1 and grid[i][ballPos[j]-1]==1)):
#                     print(i, ballPos[j])
#                     ballPos[j]=-1
#                 # skip if ball stucked
#                 if ballPos[j]== -1: continue
                
#                 # update ball pos
#                 ballPos[j] = ballPos[j] + grid[i][ballPos[j]]
#                 # if pos out of grid, mark -1
#                 if ballPos[j]<0 or ballPos[j]>=n:
#                     ballPos[j]=-1
#         return ballPos