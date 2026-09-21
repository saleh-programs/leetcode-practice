class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        arr = [0] * len(cost)
        if len(cost) == 2:
            return min(cost[0], cost[1])

        for i in range(2, len(cost)):
            arr[i] = min(arr[i - 2] + cost[i - 2], arr[i - 1] + cost[i-1])

        return min(arr[-2] + cost[-2], arr[-1] + cost[-1])
