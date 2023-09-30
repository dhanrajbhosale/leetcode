#  Remember i < j < k and nums[i] < nums[k] < nums[j]
# value tree to visualise
#  j
#  /\
# /  k
#i
class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        min_before_j = [0]*len(nums)
        min_before_j[0] =nums[0]
        stack = []

        # lets calc min_before_j for all array
        for j in range(1, len(nums)):
            min_before_j[j] = min(nums[j], min_before_j[j-1])

        # will start iterating j from last
        # as we will always compare with global minima
        # to get confidence to pop from monotonic stack after j if its value will be less than min_before_j

        for j in range(len(nums)-1, 0, -1):
            # first compare j and k (mono stack value)
            while stack and nums[j]> stack[-1]:
                # now compare i and k
                if min_before_j[j]<stack[-1]:
                    return True
                stack.pop()
            stack.append(nums[j])
        return False
