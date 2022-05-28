class Solution(object):
    

    
    def merge(self, A):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        res=[]    
        for a in sorted(A,key=lambda i:i[0]): #sorting ensures everything in middle is in range 
            if res and res[-1][1]>=a[0]:  #check if list is not empty, and check overlaping condition - current item start is less than last added item's end
                res[-1][1]=max(res[-1][1],a[1]) #update end of range with max ending       
            else:
                res+=[a] #add items which are not in the range
        return res
                    
        