class Solution:
    def get_profit(self, day, buy_flag, prices, mem):
        if day>=len(prices):
            return 0
        if (day, buy_flag) in mem:
            return mem[(day, buy_flag)]
        
        if buy_flag:
            mem[(day, buy_flag)] = max(-prices[day] + self.get_profit(day+1, False, prices, mem), self.get_profit(day+1, True, prices, mem))
        else:
            mem[(day, buy_flag)] = max(prices[day] + self.get_profit(day+2, True, prices, mem), self.get_profit(day+1, False, prices, mem))
        
        return mem[(day, buy_flag)]
        
    def maxProfit(self, prices: List[int]) -> int:
        return self.get_profit(0, True, prices, {})