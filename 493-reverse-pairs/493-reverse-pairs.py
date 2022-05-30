class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        cnt=0     
        def merge(left, right):
            nonlocal cnt
            i=j=0         
            for i in range(len(left)): #note left & right are sorted ascending
                while j<len(right) and left[i]>right[j]*2: #loop till right is smaller
                        j+=1
                cnt+=j #all number before j are smaller than all numbers before i, so take next i & start from j where it left
            return sorted(left+right)                 
        
        def mergeSort(A):
            if len(A)<=1: return A #dont update cnt
            return merge(mergeSort(A[:len(A)//2]),mergeSort(A[len(A)//2:])) #divide in mid, sort, and send to merge
        mergeSort(nums)
        return cnt