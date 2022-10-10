# BFS
# class Solution:
#     def numIslands(self, grid: List[List[str]]) -> int:
#         r, c = len(grid), len(grid[0])
#         vis = [[0 for i in range(c)] for j in range(r)]
#         res=0
#         for i in range(r):
#             for j in range(c):
#                 if not vis[i][j] and grid[i][j]=="1":
#                     self.bfs(i, j, grid, vis)
#                     res+=1
#         return res
            
#     def bfs(self, i, j, grid, vis):
#         q= collections.deque()
#         vis[i][j] = 1
#         q.append((i, j))
#         while q:
#             row, col = q.popleft()
#             # go on all 4 directions
#             directions = [[0,1],[1,0],[-1,0],[0,-1]]
#             for dr, dc in directions:
#                 r, c = row + dr, col + dc
#                 if r in range (len(grid)) and c in range (len(grid[0])) and grid[r][c]=="1" and not vis[r][c]:
#                     q.append((r, c))
#                     self.bfs(i+dr, j+dc, grid, vis)                
#         return

# DFS
class Solution:
    def numIslands(self, grid):
        if not grid:
            return 0        
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    self.dfs(grid, i, j)
                    count += 1
        return count

    def dfs(self, grid, i, j):
        if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]) or grid[i][j] != '1':
            return
        grid[i][j] = '#'
        self.dfs(grid, i+1, j)
        self.dfs(grid, i-1, j)
        self.dfs(grid, i, j+1)
        self.dfs(grid, i, j-1)
        