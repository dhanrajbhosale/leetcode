class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxOne=0
        cnt=0
        for i in nums:
            if i==1:
                cnt+=1
                maxOne=max(maxOne,cnt)
            else:
                cnt=0
        return maxOne
            