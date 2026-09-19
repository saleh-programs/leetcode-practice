class Solution:
    def countBits(self, n: int) -> List[int]:
        res = [0 for _ in range(n + 1)]

        for i in range(n + 1):
            val = i
            while val != 0:
                res[i] += (val % 2)
                val >>= 1
        return res