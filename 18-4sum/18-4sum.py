class Solution:
    
    #Sol 1 sort list O(nlogn), take 3 pointer O(n^3), and binary search O(logn) in right part for reminder 
    #TC: O(n^3logn + nlogn) 
    
    #sol 2 sort list, take two pointer, and apply twoSum algo to right half for reminder as target
    def twoSum(self, l, r, i, j, target, res, nums):
        while l<r:
            if target==nums[l]+nums[r]:
                lt, rt=nums[l], nums[r]
                res.add(tuple([nums[i],nums[j],nums[l],nums[r]]))
                while l<r and rt==nums[r]: r-=1
                while l<r and lt==nums[l]:
                    l+=1
                    print(l)

            elif target>nums[l]+nums[r]: l+=1
            else: r-=1
    
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:    
        res=set()
        n=len(nums)
        nums.sort()
        #two pointers i, j
        for i in range(n):
            for j in range(i+1,n):
                rem=target-nums[i]-nums[j] #cal remainder 
                self.twoSum(j+1, n-1, i, j, rem, res, nums) #apply TwoSum algo on right half
                while j+1<n and nums[j]==nums[j+1]: j+=1 #avoid duplicates
            while i+1<n and nums[i]==nums[i+1]: i+=1
        return res