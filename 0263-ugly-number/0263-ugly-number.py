class Solution:
    def isUgly(self, num: int) -> bool:
        if num ==1: return True
        for d in [2,3,5]:
            while num:
                q, r = divmod(num, d)
                if q==1 and not r:
                    return True
                if r:
                    break
                num = q
        return False
                    
                
