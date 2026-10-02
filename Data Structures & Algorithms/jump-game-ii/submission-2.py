class Solution:
    def jump(self, nums: List[int]) -> int:

        res = 0
        current = 0
        while current < len(nums) - 1:
            curr_jump = nums[current]
            best = [-1, float("-inf")]
            while curr_jump > 0:
                if (current + curr_jump >= len(nums) - 1):
                    return res + 1
                if current + curr_jump + nums[current + curr_jump] > best[1]:
                    best = [curr_jump, current + curr_jump + nums[current + curr_jump]]
                curr_jump -= 1
            current += best[0]

            res += 1
        return res