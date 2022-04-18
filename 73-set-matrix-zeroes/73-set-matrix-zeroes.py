class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        index=[]
        for x in matrix:
            if x.count(0)>0:
                i=matrix.index(x)
                for y in range(len(x)):
                    if x[y]==0:
                        j=y
                        index.append([i,j])
        for [i,j] in index:
            for x in range(len(matrix[0])):
                matrix[i][x]=0
            for y in range(len(matrix)):
                matrix[y][j]=0
        
        