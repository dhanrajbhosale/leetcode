class Solution:
    def hammingWeight(self, n: int) -> int:
        #Sol1: with build in function
        # return bin(n).count('1')
        
        # Sol2: shift all 32 bits (need iterate all 32 times) to right and take out right most bit
        # ones = 0
        # while n:
        #     ones+=(n&1)
        #     n = n>>1
        # return ones
        
        # Sol3: only iterate as number of 1s
        # each time you use K & (K-1), the rightmost bit with value 1 (and only that bit) will be set to 0
        c = 0
        while n:
            n &= n - 1
            c += 1
        return c