class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        rows, cols = len(board), len(board[0])
        visited = [[False] * cols for _ in range(rows)]

        def dfs(r, c, i):
            if r < 0 or c < 0 or r >= rows or c >= cols:
                return False

            if visited[r][c] or board[r][c] != word[i]:
                return False

            if i == len(word) - 1:
                return True

            visited[r][c] = True

            found = (
                dfs(r - 1, c, i + 1) or
                dfs(r + 1, c, i + 1) or
                dfs(r, c - 1, i + 1) or
                dfs(r, c + 1, i + 1)
            )

            visited[r][c] = False
            return found

        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0):
                    return True

        return False
