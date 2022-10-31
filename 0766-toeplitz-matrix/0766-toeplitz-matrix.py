class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        m, n = len(matrix), len(matrix[0])
        
        # check for every index with his diagonals
        for i in range(m):
            for j in range(n):
                x, y = i, j
                curr = matrix[i][j]
                # check if curr index's diagonal elements are equal to curr
                while x<m and y<n:
                    if curr != matrix[x][y]: # if any not equal return false
                        return False
                    x+=1
                    y+=1
        return True