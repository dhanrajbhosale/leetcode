class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        d = dict()
        # to handle mod 0 case
        d[0] = -1
        
        # We iterate through the input array exactly once, keeping track of the 'running sum mod k'. If we find that a running sum value at index j has been previously seen before in some earlier index i in the array, then we know that the sub-array (i,j] contains a desired sum.
        sums = 0
        for i in range(len(nums)):
            # take running sum
            sums+=nums[i]
            if(k!=0):
                # store just a mod
                sums = sums%k
            # if mod previously seen and window is > than 2
            if(sums in d):
                if(i-d[sums]>1):
                    return(True)
            # store mod and index
            else:
                d[sums] = i
        return False