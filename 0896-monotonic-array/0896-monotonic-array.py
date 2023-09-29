class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        N = len(nums)
        inc, dc, cm = 0,0,0
        for i in range(1, N):
            if nums[i-1]<nums[i]:
                inc+=1
            elif nums[i-1]>nums[i]:
                dc+=1
            else:
                cm+=1
        return (inc+cm==N-1) or (dc+cm==N-1)