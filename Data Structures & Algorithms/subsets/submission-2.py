class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        result.append([])
        def dfs(index):
            if index >= len(nums):
                return
            result.append([nums[index]])
            dfs(index + 1)

            coverage = 1
            curr = index + 1
            while curr + (coverage-1) < len(nums):
                result.append([nums[index]] + nums[curr:curr+coverage])
                curr += 1
                if curr + (coverage-1) >= len(nums):
                    coverage += 1
                    curr = index + 1

        dfs(0)
        return result

