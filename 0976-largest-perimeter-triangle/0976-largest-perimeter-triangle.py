class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        for i in range(2,len(nums)):
            if nums[i-2]<nums[i-1]+nums[i]:
                return sum(nums[i-2:i+1])
        return 0
            
        