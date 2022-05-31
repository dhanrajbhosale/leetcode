class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # sol 2 two pntr approach, as list is sorted
        l, r=0, len(nums)-1
        while l<r:
            if (nums[l]+nums[r])==target:
                return [l+1,r+1]
            elif (nums[l]+nums[r])>target:
                r-=1
            else:
                l+=1
        
        
        # Sol 1 Using Dictionary TC: O(n) SC: O(n)
        # seen={}
        # for i, value in enumerate(nums):
        #     if value in seen:
        #         return [seen[value]+1,i+1] #since the values in seen has always lower indices than your current number, it should come first.
        #     else:
        #         seen[target-value]=i