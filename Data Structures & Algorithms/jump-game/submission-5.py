class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) <= 1:
            return True
        visited = set()
        stack = []
        i = 0
        stack.append([i, nums[i]])
        while stack:
            curr_i, curr_jump = stack[-1]
            if curr_jump <= 0:
                stack.pop()
                if stack:
                    stack[-1][1] -= 1
                continue
            
            if curr_i + curr_jump  >= len(nums) - 1:
                return True
            if nums[curr_i + curr_jump] > 0 and curr_i + curr_jump not in visited:
                visited.add(curr_i + curr_jump)
                stack.append([curr_i + curr_jump, nums[curr_i + curr_jump]])
            else: 
                visited.add(curr_i + curr_jump)
                stack[-1][1] -= 1
        return False
