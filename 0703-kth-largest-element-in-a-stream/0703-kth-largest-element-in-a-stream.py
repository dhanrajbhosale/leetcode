class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.minHeap = nums
        heapq.heapify(self.minHeap)
        
        while len(self.minHeap)>k:
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        if self.minHeap and self.minHeap[0]>=val and len(self.minHeap)>=self.k:
            return self.minHeap[0]
        heapq.heappush(self.minHeap, val)
        if len(self.minHeap)>self.k:
            heapq.heappop(self.minHeap)
        
        return self.minHeap[0]
                


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)