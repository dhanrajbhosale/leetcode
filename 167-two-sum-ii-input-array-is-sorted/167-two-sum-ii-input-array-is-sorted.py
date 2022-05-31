class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen={}
        for i, value in enumerate(nums):
            if value in seen:
                return [seen[value]+1,i+1]
            else:
                seen[target-value]=i