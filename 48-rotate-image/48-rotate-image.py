import numpy as np

class Solution(object):
    def rotate(self, A):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        #do reverse and then transpose
        
        #method 1
        A.reverse()
        for i in range(len(A)):
            for j in range(i):
                A[i][j], A[j][i] = A[j][i], A[i][j]
        
        #method 2
        # A[:] = zip(*A[::-1])
                