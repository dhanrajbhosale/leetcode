class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
#         solution 1 using dictionary
#         cntElm=Counter(nums)
#         res=[]
        
#         for key in cntElm.keys():
#             if cntElm[key]> len(nums)//3:
#                 res.append(key)
#         return res
    
        #solution 2 hashing TC: O(n)  SC:O(n)
#         count = {}
#         for i in nums:
#             if i in count:
#                 count[i]+=1
#             else:
#                 count[i]=1
                
#         n=len(nums)//3
#         out=[]
#         for i in count:
#             if count[i]>n:
#                 out.append(i)
#         return out

    #Solution 3, Boyer Moores Voting algo TC: O(n) SC: O(1)
        count1,cand1,count2,cand2=0,None,0,None
        if not nums: return []

        for n in nums:
            if cand1==n:
                count1+=1
            elif cand2==n:
                count2+=1
            elif count1==0:
                cand1=n
                count1+=1
            elif count2==0:
                cand2=n
                count2+=1
            else:
                count1-=1
                count2-=1
        return [c for c in [cand1, cand2] if nums.count(c) > (len(nums)//3)]
    
        