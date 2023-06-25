# normal TC is exponcial & SC is O(N) auxillary sapce
# using DP.. TC will be O(N*2*3) and SC O(N*2*3) + O(N)

class Solution:
    
    def get_profit_recc(self, buy, day, cap, prices, mem):
        if day == len(prices) or cap==0:
            return 0
        
        if (buy, day, cap) in mem: # DP LINE 1
            return mem[(buy, day, cap)]
        
        if buy:  # (buy, not buy)
            mem[(buy, day, cap)] = max(-prices[day] + self.get_profit_recc(0, day+1, cap, prices, mem), self.get_profit_recc(1, day+1, cap, prices, mem))
        else:  # (sell, not sell)
            mem[(buy, day, cap)] = max(prices[day] + self.get_profit_recc(1, day+1, cap-1, prices, mem), self.get_profit_recc(0, day+1, cap, prices, mem))
            
        return mem[(buy, day, cap)]

    def maxProfit(self, prices: List[int]) -> int:
        return self.get_profit_recc(1, 0, 2, prices, {})