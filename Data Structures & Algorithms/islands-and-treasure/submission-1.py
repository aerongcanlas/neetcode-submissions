class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        q = collections.deque()
        steps = 1

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r,c))

        directions = [[1,0], [-1, 0], [0, 1], [0, -1]]
        while q:
            n = len(q)

            for i in range(n):
                r, c = q.popleft()

                for dr, dc in directions:
                    row, col = r + dr, c + dc
                    if (row in range(ROWS) and col in range(COLS)
                        and grid[row][col] > steps):
                        grid[row][col] = steps
                        q.append((row, col))

            steps += 1

