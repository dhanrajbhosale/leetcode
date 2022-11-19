class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        self.solve(board)
    
    def solve(self, board: List[List[str]])->bool:
        for r in range(len(board[0])):
            for c in range(len(board)):
                if board[r][c]==".":
                    for i in range(1,10): 
                        if self.isValid(str(i), r, c, board):
                            board[r][c]= str(i)
                            if self.solve(board):
                                return True
                            else:
                                board[r][c]="."
                    return False            
        return True
            
    def isValid(self, n:str, r:int, c:int, board: List[List[str]])->bool:
        for i in range(9):
            if board[r][i]==n or board[i][c]==n or board[3*(r//3)+(i//3)][3*(c//3)+(i%3)]==n:
                return False
        return True