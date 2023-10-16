class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex==0:
            return [1]
            
        prev = self.getRow(rowIndex-1)
        t1, t2 = [0]+prev, prev+[0]

        return list(map(lambda a,b:a+b, t1, t2))