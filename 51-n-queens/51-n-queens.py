class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col = set()
        posDiag = set() # r+c
        negDiag = set() # r-c
        
        board = [ ["."]*n for row in range(n)]
        res=[]
        
        def backtracking(r): # for each row
            if r==n: # GOAL
                copy = ["".join(row) for row in board]
                res.append(copy)
                return
            
            for c in range(n): # try to place in diff columns in given row
                if c in col or (r+c) in posDiag or (r-c) in negDiag: # CONSTRAIN
                    continue
                # place Q and update sets
                col.add(c) # CHOICE
                posDiag.add(r+c)
                negDiag.add(r-c)
                board[r][c] = "Q"
                
                backtracking(r+1) # search for next row
                
                # back track
                col.remove(c) # UNDO CHOICE
                posDiag.remove(r+c)
                negDiag.remove(r-c)
                board[r][c] = "."
        backtracking(0)
        return res