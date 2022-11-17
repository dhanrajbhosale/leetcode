class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        
        total = (ax2-ax1)*(ay2-ay1)+(bx2-bx1)*(by2-by1)
        
        # non overlapping conditions
        # ------- ---------
        if (bx1-ax2)>=0 or (ax1-bx2)>=0 or (by1-ay2)>=0 or (ay1-by2)>=0:
            return total
        x = [ax1, ax2, bx1, bx2]
        y = [ay1, ay2, by1, by2]
        x.sort()
        y.sort()
        total = total - ((x[2]-x[1])*(y[2]-y[1])) 
        return total