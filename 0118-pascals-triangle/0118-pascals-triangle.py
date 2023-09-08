class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]
        if numRows == 1:
            return res
        
        def add_two_array(a, b):
            s = []
            for i in range(len(a)):
                s.append(a[i]+b[i])
            return s
        
        for i in range(1, numRows):
            t1 = res[-1] + [0]
            t2 = [0] + res[-1]
            res.append(add_two_array(t1, t2))
        
        return res
            
        