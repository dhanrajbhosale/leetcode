class Solution:
    def hammingWeight(self, n: int) -> int:
        # with build in function
        # return bin(n).count('1')
        ones = 0
        while n:
            ones+=(n&1)
            n = n>>1
        return ones