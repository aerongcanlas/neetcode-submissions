class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        res = 0
        def markVisited(r, c):
            grid[r][c] = '*'

        def dfs(r, c):
            if r < 0 or c < 0 or r == ROWS or c == COLS or grid[r][c] == '*' or grid[r][c] == '0':
                return

            markVisited(r, c)
            dfs(r, c+1)
            dfs(r, c-1)
            dfs(r-1, c)
            dfs(r+1, c)

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == '0':
                    markVisited(r, c)
                elif grid[r][c] == '1':
                    res += 1
                    dfs(r, c)
                
        return res
            
        