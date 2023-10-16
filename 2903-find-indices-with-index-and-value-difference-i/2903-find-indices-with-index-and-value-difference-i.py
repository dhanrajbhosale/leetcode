class Solution:
    def findIndices(self, nums: List[int], indexDifference: int, valueDifference: int) -> List[int]:
        N = len(nums)
        for diff in range(indexDifference, N):
            for i in range(N-diff):
                if abs(nums[i]-nums[i+diff])>=valueDifference:
                    return [i, i+diff]
        return [-1,-1]