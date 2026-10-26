#3619. Count Islands With Total Value Divisible by K

class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        count = 0

        def dfs(r, c):
            if r < 0 or r >= m or c < 0 or c >= n or grid[r][c] == 0:
                return 0

            value = grid[r][c]
            grid[r][c] = 0  # Mark as visited

            value += dfs(r + 1, c)
            value += dfs(r - 1, c)
            value += dfs(r, c + 1)
            value += dfs(r, c - 1)

            return value

        for r in range(m):
            for c in range(n):
                if grid[r][c] > 0:
                    island_sum = dfs(r, c)

                    if island_sum % k == 0:
                        count += 1

        return count
