# normal TC is exponcial & SC is O(N) auxillary sapce
# using DP.. TC will be O(N*2*3) and SC O(N*2*3) + O(N)

class Solution:
    
    def get_profit_recc(self, buy, day, cap, prices, mem):
        if day == len(prices) or cap==0:
            return 0
        
        if mem[day][buy][cap]!= -1: # DP LINE 1
            return mem[day][buy][cap]
        
        if buy:  # (buy, not buy)
            mem[day][buy][cap] = max(-prices[day] + self.get_profit_recc(0, day+1, cap, prices, mem), self.get_profit_recc(1, day+1, cap, prices, mem))
        else:  # (sell, not sell)
            mem[day][buy][cap] = max(prices[day] + self.get_profit_recc(1, day+1, cap-1, prices, mem), self.get_profit_recc(0, day+1, cap, prices, mem))
        return mem[day][buy][cap]

    def maxProfit(self, prices: List[int]) -> int:
        mem = [[[-1 for _ in range(3)] for _ in range(2)] for _ in range(len(prices))]
        return self.get_profit_recc(1, 0, 2, prices, mem)