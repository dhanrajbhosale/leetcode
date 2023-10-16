class Solution:
    def findIndices(self, nums: List[int], indexDifference: int, valueDifference: int) -> List[int]:
        N = len(nums)
        min_max_indices=[[0,0] for i in range(N)]
        # calc all min and max for every index
        min_, max_ = float('inf'), float('-inf')
        for i in range(N):
            if i-1>=0:
                min_max_indices[i][0]=min_max_indices[i-1][0]
                min_max_indices[i][1]=min_max_indices[i-1][1]
            if min_>nums[i]:
                min_ = nums[i]
                min_max_indices[i][0]=i
            if max_<nums[i]:
                max_ = nums[i]
                min_max_indices[i][1]=i
        

        for i in range(indexDifference,N):
            check = i-indexDifference
            if nums[i]-nums[min_max_indices[check][0]]>=valueDifference:
                return [min_max_indices[check][0], i]
            if nums[min_max_indices[check][1]]-nums[i]>=valueDifference:
                return [min_max_indices[check][1], i]

        return [-1,-1]
