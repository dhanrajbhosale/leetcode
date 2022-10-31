class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:         
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.dfs(i,j,word, board, 0):
                    return True
        return False
    
    def dfs(self, x, y, word, board, c):
        if len(word)==c:
            return True    
        if x<0 or y<0 or x>=len(board) or y>=len(board[0]) or board[x][y]!=word[c]:
            return False      
        board[x][y] = "#"
        if self.dfs(x+1, y, word, board, c+1):
            return True
        elif self.dfs(x, y+1, word, board, c+1):
            return True
        elif self.dfs(x-1, y, word, board, c+1):
            return True
        elif self.dfs(x, y-1, word, board, c+1):
            return True 
        board[x][y] = word[c]
        return False