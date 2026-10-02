class Solution:
    def getSum(self, a: int, b: int) -> int:
        
        total = 1
        carry = 0

        a &= 0xFFFFFFFF
        b &= 0xFFFFFFFF
        bits = 0
        while a != 0 or b != 0:
            bits += 1
            bit1 = a & 1
            bit2 = b & 1
            a >>= 1
            b >>= 1
            
            bit_total = (bit1 ^ bit2) ^ carry
            total <<= 1
            total ^= bit_total

            if (bit1 & bit2) | ((bit1 ^ bit2) & carry):
                carry = 1
            else:
                carry = 0
        if bits < 32 and carry:
            total <<= 1
            total ^= 1

        # reversing bits
        res = 0
        while total != 1:
            bit = total & 1
            total >>= 1

            res <<= 1
            res ^= bit
        if res & 0b10000000000000000000000000000000:
            res -= 0b100000000000000000000000000000000
        return res            



            
