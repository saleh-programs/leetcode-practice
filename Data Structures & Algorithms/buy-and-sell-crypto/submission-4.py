class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        buy = [float("inf"), -1]
        best = float("-inf")
        for i in range(len(prices)):
            best = max(best, prices[i] - buy[0])
            if prices[i] < buy[0]:
                buy = [prices[i], i]
                continue
            

        return max(best, 0)
