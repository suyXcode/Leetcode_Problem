
class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:

        grid = [['#'] * n for _ in range(m)]

        # Create one path: move right across the first row
          for j in range(n):
              grid[0][j] = '.'

        # Move down along the last column
          for i in range(m):
              grid[i][n - 1] = '.'

          return [''.join(row) for row in grid]
