# O(1) space 2*O(m*n) time
class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        col0, rows, cols = 1, len(matrix), len(matrix[0])

        for i in range(0, rows):
            if matrix[i][0] == 0:
                col0 = 0
            for j in range(1, cols):
                if matrix[i][j] == 0:
                    matrix[i][0] = matrix[0][j] = 0

        for i in range(rows-1, -1, -1):
            for j in range(1, cols):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
            if col0 == 0:
                matrix[i][0] = 0

# #Solution 2 O(m*n) space 2*O(m*n) time
# class Solution(object):
#     def setZeroes(self, matrix):
#         """
#         :type matrix: List[List[int]]
#         :rtype: None Do not return anything, modify matrix in-place instead.
#         """
        
#         index=[]
#         for x in matrix:
#             if x.count(0)>0:
#                 i=matrix.index(x)
#                 for y in range(len(x)):
#                     if x[y]==0:
#                         j=y
#                         index.append([i,j])
#         for [i,j] in index:
#             for x in range(len(matrix[0])):
#                 matrix[i][x]=0
#             for y in range(len(matrix)):
#                 matrix[y][j]=0
        
        