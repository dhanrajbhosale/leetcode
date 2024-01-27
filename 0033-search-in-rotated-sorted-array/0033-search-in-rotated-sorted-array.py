# Approach 1, two times binary search
# 	1. Find pivot
# 	2. Apply binary in sortedpart
# first find pivotal element by finding leftmist smallest or equal to last element
# class Solution:
#     def search(self, nums: List[int], target: int) -> int:
#         N = len(nums)
#         l, r = 0, N-1
        
#         while l<=r:
#             mid = (l+r)//2
#             if nums[mid]>nums[-1]:
#                 l = mid+1
#             else:
#                 r = mid-1
#         mid = l
        
#         # now binary search in both parts
#         if target>nums[-1]:
#             l, r = 0, mid-1
#         else:
#             l, r = mid, N-1 
        
#         while l<=r:
#             mid = (l+r)//2
#             if target==nums[mid]:
#                 return mid
#             elif target<nums[mid]:
#                 r=mid-1
#             else:
#                 l=mid+1
        
#         return -1


# Approach 2: In one binary
# Divide array in 3 parts. 
# L to mid-1 | mid | mid+1 to r
# Figure out which part is sorted and if elemen present in it, keep that part other wise desard

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        left, right = 0, n - 1
        while left <= right:
            mid = (right + left) // 2
            
            # Case 1: find target
            if nums[mid] == target:
                return mid
            
            # Case 2: subarray on mid's left is sorted
            elif nums[mid] >= nums[left]:
                if target >= nums[left] and target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
                    
            # Case 3: subarray on mid's right is sorted.
            else:
                if target <= nums[right] and target > nums[mid]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1