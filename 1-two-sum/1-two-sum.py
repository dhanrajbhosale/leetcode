class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen ={}
        for i, value in enumerate(nums):
            if value in seen:         #check if value is required for previous element
                return[seen[value],i] #return previos elemet and current index
            else: 
                seen[target-value]=i #store required pair for ith element