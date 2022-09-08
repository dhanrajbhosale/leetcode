class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c]==".":
                    continue
                k=board[r][c]
                board[r][c]="." #remove that value to avoid validating with itself
                if self.isValidBox(board, r, c, k):
                    board[r][c]=k # restore value removed for next validations
                    continue          
                return False
        return True
                
    def isValidBox(self, board, r, c, k):
        for i in range(9):
            # check if same number present in rows, cols, box
            if board[r][i]==k or board[i][c]==k or board[3*(r//3)+(i//3)][3*(c//3)+(i%3)]==k:
                return False
        return True
            