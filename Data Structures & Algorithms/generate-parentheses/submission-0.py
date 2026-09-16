class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        parentheses = []
        def dfs(word, l, r):
            if len(word) > n*2 or l > n or r > l:
                return
            dfs(word + "(", l + 1, r)
            dfs(word + ")", l, r + 1)
            if len(word) == n*2:
                parentheses.append(word)
        dfs("", 0, 0)

        return parentheses

    def validateParenthesis(self, item: str):
        stack = []
        for val in item:
            if val == '(':
                stack.append(val)
            else:
                if (len(stack) == 0):
                    return False
                stack.pop()
        return len(stack) == 0
            

