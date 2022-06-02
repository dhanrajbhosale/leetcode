
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:   
        # we cant use sliding window or 2 pointer, need to use prefixSum
        # a,b,c,d,e,f
        # -----x ( k )
        # -----------y
        # if y-x==k then sum(x+1:y+1)=k cnt++
        # so lets find x=y-k in array and cnt++
        
        prefixSum={0:1} #base case (sum, count)
        s=0
        cnt=0
        for y in nums:
            s+=y
            cnt+=prefixSum.get(s-k,0) #if no s, it will return 0 sent
            prefixSum[s]=prefixSum.get(s,0)+1 #there might be multiple times same sum accuring (as we have -ve terms too) so incrementing prev count by 1, if any
        return cnt
            
        
        
        # Sol 1 O(n^2) with TLE Broot Force approach
        # l=len(nums)
        # res=0
        # s=0
        # for i in range(l):
        #     for j in range(i,l):
        #         s+=nums[j]
        #         if s==k:
        #             res+=1
        #     s=0
        # return res
        