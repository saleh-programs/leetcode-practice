class Solution:
    def canJump(self, nums: List[int]) -> bool:

        # attempting a stronger solution. modify in place. subtract from 
        # max right after jumping

        if len(nums) <= 1:
            return True
        
        i = 0
        while i > -1:
            if i >= len(nums) - 1:
                return True
            if nums[i] == 0:
                i -= 1
                continue
            nums[i] -= 1
            i += nums[i] + 1
        return False

            