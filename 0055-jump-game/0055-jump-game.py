class Solution:
    def canJump(self, nums: List[int]) -> bool:
        jmp=0
        for i in range(len(nums)-2,-1,-1):
            jmp+=1
            if nums[i]>=jmp:
                jmp=0
        return False if jmp else True