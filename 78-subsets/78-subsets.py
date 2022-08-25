# substring by power set apporach (bit manipulation)
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # [1/0,1/0,1/0] represents given nums [1,2,3] - to take or not to take 
        res=[]
        l=len(nums)
        for i in range(1<<l): # 2 POWER l combinations
            tmp=[]
            for j in range(l): # bit for all elements in given nums list
                if i & (1<<j): # checking if i th bit is set
                    tmp.append(nums[j]) # making 1 combination
            res.append(tmp) # adding one combination in list
        return res
       