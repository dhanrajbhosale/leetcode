class MedianFinder:

    def __init__(self):
        self.stack = []
        

    def addNum(self, num: int) -> None:
        def binarySearch(search_val):
            l, r = 0, len(self.stack)
            while l<r:
                m = (l+r)//2
                if search_val <= self.stack[m]:
                    r=m
                else:
                    l=m+1
            return l
        index = binarySearch(num)
        self.stack.insert(index, num)

    def findMedian(self) -> float:
        l = len(self.stack)
        m = l//2
        if l%2:
            return self.stack[m]
        else:
            return (self.stack[m-1]+self.stack[m])/2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()