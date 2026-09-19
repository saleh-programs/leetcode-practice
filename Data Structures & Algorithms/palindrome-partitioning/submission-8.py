class Solution:
    def partition(self, s: str) -> List[List[str]]:

        #trying a BETTER dynamic programming approach
        results = []
        palindromes = set()

        def dfs(substrings, split):
            if (split > len(s) - 1):
                pal_indices = (len(s) - len(substrings[-1]),len(s)-1)
                if (pal_indices in palindromes):
                    results.append(substrings)
                return

            last_sub = substrings[-1]
            new_subs = substrings[:-1]
            new_subs.append(last_sub[:split - (len(s) - len(last_sub))])
            new_subs.append(last_sub[split - (len(s) - len(last_sub)):])

            start_i = len(s) - len(new_subs[-1]) - len(new_subs[-2])
            pal_indices = (start_i, start_i + len(new_subs[-2]) - 1)
            # optimization: only if second to last string (it will not change) is palindrome, continue
            # processing left subtree 
            if (pal_indices in palindromes):
                dfs(new_subs, split + 1)
            dfs(substrings, split + 1)
        
        for i in range(len(s)):
            for j in range(i, len(s)):
                if self.isPalindrome(s, i, j):
                    palindromes.add((i,j))
        dfs([s], 1)
        return results


    def isPalindrome(self, s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1 
            r -= 1
        return True

