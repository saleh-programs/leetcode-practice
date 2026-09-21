class Solution:
    def rob(self, nums: List[int]) -> int:
        arr = [0] * len(nums)

        if len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums[0], nums[1])
        elif len(nums) == 3:
            return max(nums[0] + nums[2], nums[1])
            
        arr[2] = nums[0]
        for i in range(3, len(nums)):
            arr[i] = max(arr[i-3] + nums[i-3], arr[i-2] + nums[i-2])
        return max(arr[-2] + nums[-2], arr[-1] + nums[-1])