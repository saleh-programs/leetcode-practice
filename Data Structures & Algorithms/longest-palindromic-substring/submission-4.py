class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        if not s:
            return ""

        count = len(s)
        max_sub = [0, 0]
        for i in range(1, len(s)):
            # handles even palindromes
            if s[i] == s[i-1]:
                l = i-2
                r = i+1
                while l >= 0 and r < len(s) and s[l] == s[r]:
                    l -= 1
                    r += 1
                    count -=1
                
                l += 1
                r -= 1
                if max_sub[1] - max_sub[0] < r - l:
                    max_sub = [l, r]
            
            # handles odd palindromes. Merge if they both work
            if i > 1 and s[i-2] == s[i]:
                l = i-3
                r = i+1
                while l >= 0 and r < len(s) and s[l] == s[r]:
                    l -= 1
                    r += 1
                    count -=1

                l += 1
                r -= 1
                if max_sub[1] - max_sub[0] < r - l:
                    max_sub = [l, r]
                i = r
        return s[max_sub[0]: max_sub[1] + 1]

