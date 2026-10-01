class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0 or x == 1:
            return x
        if x == -1:
            if n % 2 == 0:
                return 1
            else:
                return -1

        if n < 0: 
            return 1 / self.myPow2(x, abs(n), x)
        return self.myPow2(x, abs(n), x)

    def myPow2(self, x: float, n: int, og: int) -> float:
        if n == 0:
            return 1
        if n == 1:
            return og
        l = self.myPow2(x, n // 2, og)
        if n % 2 == 0:
            return l * l
        return l * l * og
