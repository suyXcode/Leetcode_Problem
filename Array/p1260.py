from typing import List

class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        total = m * n
        k %= total

        ans = [[0] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                idx = i * n + j
                new_idx = (idx + k) % total
                ni = new_idx // n
                nj = new_idx % n
                ans[ni][nj] = grid[i][j]

        return ans
