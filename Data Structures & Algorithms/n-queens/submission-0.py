class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        results = []
        matrix = [["."] * n for _ in range(n)]
        count = 0
        visited = set()


        def dfs(matrix, index, row):
            nonlocal count
            y = row + 1
            x = index + 1
            pslope = y - x
            nslope = (y + x) - 1
            visited.add(f"+{pslope}")
            visited.add(f"-{nslope}")
            visited.add(index)

            matrix[row][index] = "Q"

            # print(row, index)
            # print("".join(["".join(matrix[i]) for i in range(n)]))

            if row == n-1:
                count += 1
                results.append(["".join(matrix[i]) for i in range(n)])
                visited.remove(f"+{pslope}")
                visited.remove(f"-{nslope}")
                visited.remove(index)
                matrix[row][index] = "."
                return 

            for i in range(n):
                temp_pslope = (row + 2) - (i + 1)
                temp_nslope = ((row + 2) + (i + 1)) - 1
                if (i in visited) or (f"+{temp_pslope}" in visited) or (f"-{temp_nslope}" in visited):
                    continue
                dfs(matrix, i, row + 1)


            visited.remove(f"+{pslope}")
            visited.remove(f"-{nslope}")
            visited.remove(index)
            matrix[row][index] = "."

        for i in range(n):
            dfs(matrix, i, 0)
            print(visited)



        return results

    