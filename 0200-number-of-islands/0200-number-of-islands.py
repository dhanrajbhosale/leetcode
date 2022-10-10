class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        r, c = len(grid), len(grid[0])
        vis = [[0 for i in range(c)] for j in range(r)]
        res=0
        for i in range(r):
            for j in range(c):
                if not vis[i][j] and grid[i][j]=="1":
                    self.bfs(i, j, grid, vis)
                    res+=1
        return res
            
    def bfs(self, i, j, grid, vis):
        q= collections.deque()
        vis[i][j] = 1
        q.append((i, j))
        while q:
            row, col = q.popleft()
            # go on all 4 directions
            directions = [[0,1],[1,0],[-1,0],[0,-1]]
            for dr, dc in directions:
                r, c = row + dr, col + dc
                if r in range (len(grid)) and c in range (len(grid[0])) and grid[r][c]=="1" and not vis[r][c]:
                    q.append((r, c))
                    self.bfs(i+dr, j+dc, grid, vis)                
        return
        