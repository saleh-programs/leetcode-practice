class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        trackSum = nums[0]
        maxSum = trackSum
        for i in range(1, len(nums)):
            if trackSum < 0:
                trackSum = 0
            trackSum += nums[i]

            maxSum = max(maxSum, trackSum)
        return maxSum

            
            




                