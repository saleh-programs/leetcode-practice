class Solution:
    def reverseBits(self, n: int) -> int:
        
        reversed = 1
        for i in range(32):
            reversed <<= 1
            if n % 2 != 0:
                reversed += 1
            n >>= 1
        reversed -= 2**32
        return reversed