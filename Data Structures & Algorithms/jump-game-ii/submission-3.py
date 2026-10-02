class Solution:
    def jump(self, nums: List[int]) -> int:

        res = 0
        prev_current = None
        current = 0

        dp_best = None

        while current < len(nums) - 1:
            curr_jump = 1
            best = [-1, float("-inf")]

            if dp_best and dp_best[0] > current:
                curr_jump = (prev_current + nums[prev_current] + 1) - (current - prev_current) 
                best = [dp_best[0] - (current - prev_current), dp_best[1]]

            while curr_jump <= nums[current]:
                if (current + curr_jump >= len(nums) - 1):
                    return res + 1

                if current + curr_jump + nums[current + curr_jump] > best[1]:
                    best = [curr_jump, current + curr_jump + nums[current + curr_jump]]
                dp_best = [current + curr_jump, current + curr_jump + nums[current + curr_jump]]
                curr_jump += 1
            prev_current = current
            current += best[0]

            res += 1
        return res