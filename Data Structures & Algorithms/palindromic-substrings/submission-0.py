class Solution:
    def countSubstrings(self, s: str) -> int:
        
        res = 0
        for i in range(len(s)):
            res += 1
            if i > 0 and s[i] == s[i-1]: 
                res += 1

                l = i - 2
                r = i + 1
                while l >= 0 and r < len(s) and s[l] == s[r]:
                    res += 1

                    l -= 1
                    r += 1
            if i > 1 and s[i] == s[i-2]:
                res += 1

                l = i - 3
                r = i + 1
                while l >= 0 and r < len(s) and s[l] == s[r]:
                    res += 1

                    l -= 1
                    r += 1
        return res
