class Solution:
    def findRow(self,A, l, r, target )->int: #returns row number with target range
        if l>=r: return l
        mid=(l+r)//2
        index=0
        if target<A[mid][0]: #if target in first half
            index=self.findRow(A,l,mid-1,target) #move right to previous row
        if target>=A[mid][0]: #if target in second half
            if target<=A[mid][-1]: #check end of row
                return mid
            index=self.findRow(A,mid+1,r,target) #move left to next row
        return index
        
    
    def searchMatrix(self, A: List[List[int]], target: int) -> bool:
        rows=len(A)
        i=self.findRow(A,0, rows-1, target)
        return A[i].count(target)>0 #see if row contains target
    
    
        # solution no 2
        # return any(target in row for row in matrix)
        
        #Solution 3 Considering as 2D sorted array
#         if not matrix or target is None:
#             return False

#         rows, cols = len(matrix), len(matrix[0])
#         low, high = 0, rows * cols - 1 #start from first and last matrix
        
#         while low <= high:
#             mid = (low + high) / 2
#             num = matrix[mid / cols][mid % cols] #finding index of mid

#             if num == target:
#                 return True
#             elif num < target:
#                 low = mid + 1
#             else:
#                 high = mid - 1
        
#         return False
