class StockSpanner:

    def __init__(self):
        self.stack = [] # pair or (price, span)

    def next(self, price: int) -> int:
        span = 1
        # while pop is less than price pop it and increment span
        # as we dont need to consider these elements as we are storing their span
        while self.stack and self.stack[-1][0]<=price:
            span += self.stack[-1][1]
            self.stack.pop()
        # even if price will be less, we need to return 1
        self.stack.append([price, span])
        
        return span

# Your StockSpanner object will be instantiate  d and called as such:

