class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        profit = 0
        N = len(prices)
        buy = float('inf')
        for i in range(N):
            # if got less value, buy
            buy = min(buy, prices[i])
            # if got more value covering fee, sell
            if prices[i]> buy + fee:
                profit += prices[i] - buy - fee
            #  if there is a better (higher) selling price compared to the previously selling price, to cancel out the transaction fee and merge two transactions to one.
            buy = max(buy, prices[i] - fee)

        return profit   