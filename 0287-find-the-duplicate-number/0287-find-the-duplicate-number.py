class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slowP = nums[0]
        fastP = nums[nums[0]]
        
        while slowP!=fastP:
            slowP = nums[slowP]
            fastP = nums[nums[fastP]]
        
        slowP = 0
        
        while slowP!=fastP:
            slowP = nums[slowP]
            fastP = nums[fastP]
        
        return slowP