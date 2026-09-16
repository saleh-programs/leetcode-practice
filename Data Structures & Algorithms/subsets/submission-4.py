class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        subsets = [[]]
        def dfs(index, subset):
            if index >= len(nums):
                return

            new_subset = subset.copy()
            new_subset.append(nums[index])

            subsets.append(new_subset)
            dfs(index + 1, new_subset)
            dfs(index + 1, subset)

        dfs(0, [])
        return subsets
