class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # brute force t: O(n2) s:O(1)
        # max_profit = 0
        # for i in range(len(prices)):
        #     for j in range(i + 1, len(prices)):
        #         # print("i: ", prices[i], "j: ", prices[j])
        #         if prices[i] < prices[j]:
        #             profit = prices[j] - prices[i] 
        #             max_profit = max(max_profit, profit)
        
        # return max_profit

        # two pointer t: O(n), s: O(1) 
        # l = 0
        # r = 1
        # max_profit = 0
        # while r < len(prices):
        #     if prices[l] < prices[r]:
        #         profit = prices[r] - prices[l] 
        #         max_profit = max(max_profit, profit)
        #     else:
        #         l = r
        #     r += 1
        # return max_profit

        # DP t: O(n), s: O(1)
        maxP = 0
        minBuy = prices[0]

        for sell in range(1, len(prices)):
            maxP = max(maxP, prices[sell] - minBuy)
            minBuy = min(minBuy, prices[sell])
        return maxP
