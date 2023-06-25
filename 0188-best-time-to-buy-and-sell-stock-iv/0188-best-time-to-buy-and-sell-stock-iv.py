class Solution:
    def get_profit(self, day, buy_flag, cap, prices, mem):
        if day == len(prices) or cap==0:
            return 0
        if (day, buy_flag, cap) in mem:
            return mem[(day, buy_flag, cap)]
        
        if buy_flag: # buy, not buy
            mem[(day, buy_flag, cap)] = max(- prices[day] + self.get_profit(day+1, False, cap, prices, mem), self.get_profit(day+1, True, cap, prices, mem))
        else: # sell, not sell
            mem[(day, buy_flag, cap)] = max( prices[day] + self.get_profit(day+1, True, cap-1, prices, mem), self.get_profit(day+1, False, cap, prices, mem))
        
        return mem[(day, buy_flag, cap)]
        
    def maxProfit(self, k: int, prices: List[int]) -> int:
        return self.get_profit(0, True, k, prices, {})
        