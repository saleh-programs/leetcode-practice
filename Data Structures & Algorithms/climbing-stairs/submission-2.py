class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2: 
            return n
        one_ago = 2
        two_ago = 1     
        for i in range(2, n):
            temp = one_ago + two_ago
            two_ago = one_ago
            one_ago = temp
        return one_ago

