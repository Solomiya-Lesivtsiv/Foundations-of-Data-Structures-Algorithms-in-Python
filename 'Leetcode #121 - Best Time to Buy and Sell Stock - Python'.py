class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        minValueSoFar = prices[0]

        for i in range(1, len(prices)):
            profit = prices[i] - minValueSoFar
            if profit > ans:
                ans = profit
            if prices[i] < minValueSoFar:
                minValueSoFar = prices[i]

        return ans
