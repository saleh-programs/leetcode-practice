class Solution:
    def rob(self, nums: List[int]) -> int:
        
        house1 = 0
        house2 = 0
        for i in range(len(nums)):
            temp = max(house1, house2 + nums[i])
            house2 = house1
            house1 = temp
        return house1