# TC O(n) SC O(n)
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        s = n*(n+1)//2
        # nums 2,2,3,4
        # 1,2,3,4 - 2,3,4
        missing = s - sum(set(nums))
        # 2,2,3,4 - 2,3,4 (i.e. set(nums))
        duplicate = sum(nums) + missing -s
        return [duplicate, missing]