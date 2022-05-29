class Solution:
    
    def countSmaller(self, nums: List[int]) -> List[int]:
        
        l=len(nums)
        res=[0]*l
        enum=list(enumerate(nums)) #to store indices to track position
        self.mergeSort(0, l-1, res, enum)
        return res
    
    def mergeSort(self, l, r, res, enum):    
        if l>=r: #if only 1 element left
            return
        mid=(l+r)//2
        self.mergeSort(l,mid,res, enum)
        self.mergeSort(mid+1,r,res, enum)
        self.merge(l,mid,r,res, enum)     
    
    def merge(self, l, mid, r, res, enum):
        i, j = l, mid+1
        temp=[]
        
        while i<=mid and j<=r: #sorting in descending order
            if enum[i][1]<=enum[j][1]:
                temp.append(enum[j])
                j+=1
            else: #IMP STEP 
                res[enum[i][0]]+=r-j+1 # it is in descending order & it is in right half, so all at right would be counted
                temp.append(enum[i])
                i+=1
        
        while i <= mid:
            temp.append(enum[i])
            i+= 1
        
        while j <= r:
            temp.append(enum[j])
            j+= 1
            
        enum[l:r+1] = temp  #swap enum with the sorted segement, to ensure the merge() function in the next level is also dealing with a sorted array