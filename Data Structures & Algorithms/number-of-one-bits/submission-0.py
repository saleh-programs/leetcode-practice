class Solution:
    def hammingWeight(self, n: int) -> int:
        initial = n
        res = 0
        while initial != 0:
            if initial & 1 == 1:
                res += 1
            initial >>= 1
        return res