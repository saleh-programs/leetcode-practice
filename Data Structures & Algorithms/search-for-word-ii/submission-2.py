class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class PrefixTree:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.endOfWord = True

    def search(self, word: str) -> bool:
        cur = self.root
        for c in word:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return cur.endOfWord

    def startsWith(self, prefix: str, start=None) -> tuple[bool,TrieNode]:
        cur = start if start is not None else self.root
        for c in prefix:
            if c not in cur.children:
                return False, cur
            cur = cur.children[c]
        return True, cur



class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        results = set()
        trie = PrefixTree()
        for wd in words:
            trie.insert(wd)
        current = trie.root
        def dfs(i, j, currword, visited):
            nonlocal current

            prev = current
            visited.add(f"{i}-{j}")
            neighbors = [
                (j + 1, i),
                (j, i + 1),
                (j - 1, i),
                (j, i - 1)
            ]
            for nbr in neighbors:
                if nbr[0] < 0 or nbr[1] < 0 or nbr[0] >= len(board[0]) or nbr[1] >= len(board):
                    continue
                if f"{nbr[1]}-{nbr[0]}" in visited:
                    continue
                nextWord = currword + board[nbr[1]][nbr[0]]
                foundResult = trie.startsWith(board[nbr[1]][nbr[0]], current)
                if foundResult[0]:
                    if foundResult[1].endOfWord:
                        results.add(nextWord)
                    current = foundResult[1]
                    dfs(nbr[1], nbr[0], nextWord, visited)
                current = prev
            visited.remove(f"{i}-{j}")

        for i in range(len(board)):
            for j in range(len(board[0])):
                currword = board[i][j]
                foundResult = trie.startsWith(currword, None)
                current = foundResult[1]
                if not foundResult[0]:
                    continue
                if foundResult[1].endOfWord:
                    results.add(currword)
                dfs(i, j, currword, set())


        
        return list(results)





