class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        cache = [float("inf")] * (amount + 1)
        cache[0] = 0

        for i in range(1, amount + 1):
            
            minCoins = float("inf")
            for c in coins:
                if i - c < 0:
                    continue
                minCoins = min(minCoins, cache[i - c])

            cache[i] = 1 + minCoins
        if cache[amount] == float("inf"):
            return -1
        return cache[amount]

