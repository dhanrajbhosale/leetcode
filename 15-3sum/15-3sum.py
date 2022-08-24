class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # using 2 pointer apporach
        res=[]
        #sort to apply l & r logic.. if sum less l++ if sum more r-- as sorted
        nums.sort()
        for i in range(len(nums)-2):
            if i>0 and nums[i]==nums[i-1]: # if i is same as last, skip
                continue
            remain = 0 - nums[i] # apply two pointer approach 
            l, r = i+1, len(nums)-1
            while l<r:
                if remain >nums[l]+nums[r]: # if sum is less, move left ahead to increase sum
                    l+=1
                elif remain <nums[l]+nums[r]:# if sum is more, move right behind to decrease sum
                    r-=1
                else:
                    res+=[[nums[i],nums[l],nums[r]]]
                    while l<r and nums[l]==nums[l+1]: l+=1 # skip duplicates
                    while l<r and nums[r]==nums[r-1]: r-=1
                    l+=1
                    r-=1
        return res
                