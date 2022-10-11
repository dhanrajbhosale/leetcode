class Solution:
    # BFS
    def jump(self, nums: List[int]) -> int:
        
        farthest, steps = 0, 0
        # window to define level - which elements are reachable from current index
        l, r = 0, 0
        while r<len(nums)-1: # check till second last index
            # check for that window
            for i in range(l, r+1):
                farthest = max(farthest, i + nums[i])
            l = r + 1
            r = farthest
            steps+=1
        return steps

        