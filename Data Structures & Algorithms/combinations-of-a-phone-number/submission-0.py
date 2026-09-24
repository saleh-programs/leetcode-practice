class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        if digits == "":
            return []
        letterDict = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        res = []
        
        def dfs(digitInd, letterInd, s):
            letter = letterDict[digits[digitInd]][letterInd]
            s.append(letter)  
            if digitInd == len(digits) - 1:
                res.append("".join(s))
                s.pop()
                return

            nextDigit = digits[digitInd + 1]

            i = 0
            for l in letterDict[nextDigit]:
                dfs(digitInd + 1, i, s)
                i += 1
            s.pop()
        for i in range(len(letterDict[digits[0]])):
            dfs(0, i, [])
        return res
            



