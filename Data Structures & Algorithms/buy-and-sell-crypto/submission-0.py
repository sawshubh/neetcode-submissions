class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        for i in range(len(prices)):
            for j in range(i + 1, len(prices)):
                # print("i: ", prices[i], "j: ", prices[j])
                if prices[i] < prices[j]:
                    profit = prices[j] - prices[i] 
                    max_profit = max(max_profit, profit)
        
        return max_profit