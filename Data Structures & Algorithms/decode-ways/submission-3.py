class Solution:
    def numDecodings(self, s: str) -> int:


        numS = []
        for i in range(len(s)):
            numS.append(int(s[i]))
            if numS[i] == 0 and (i == 0 or numS[i-1] == 0 or ((numS[i-1] * 10 + numS[i]) > 26)):
                    return 0
        
        singles = 1
        doubles = 0
        i = 0
        while i < len(s) - 1:
            if numS[i+1] == 0:
                doubles = singles
                singles = 0
                i += 1
                continue
            can_merge = numS[i] * 10 + numS[i + 1] <= 26
            singles += doubles
            if can_merge:
                doubles = singles - doubles
            else:
                doubles = 0
            i += 1
    
        return singles + doubles

            


