class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0

        left = 0
        while left < len(prices)-1 and prices[left] > prices[left + 1]:
            left += 1

        right = left + 1
        while right < len(prices):
            profit = prices[right] - prices[left]
            maxProfit = max(maxProfit, profit)

            if profit < 0:
                left = right
            
            right += 1
        
        return maxProfit   