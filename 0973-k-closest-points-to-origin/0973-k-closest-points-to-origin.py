class Solution:
    # with sorting TC(nlog(n)), with Heap TC(klog(n))
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap, res = [], []
        
        for x, y in points:
            dist = x**2+y**2    
            minHeap.append([dist, [x, y]])
            
        # python by default take first value as key to heapify
        heapq.heapify(minHeap)

        while k>0: # k
            dist, coordinates = heapq.heappop(minHeap) # log(n)
            res.append(coordinates)
            k-=1
        
        return res
        