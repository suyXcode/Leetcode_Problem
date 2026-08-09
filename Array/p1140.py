class Solution:
    def stoneGameII(self, piles):
        n = len(piles)

        # suffix[i] = sum of piles[i:]
        suffix = piles[:]

        for i in range(n - 2, -1, -1):
            suffix[i] += suffix[i + 1]

        # mem[i][M]
        mem = [[0] * (n + 1) for _ in range(n)]

        return self._stoneGameII(suffix, 0, 1, mem)

    def _stoneGameII(self, suffix, i, M, mem):
        # Can take all remaining piles
        if i + 2 * M >= len(mem):
            return suffix[i]

        # Already calculated
        if mem[i][M] > 0:
            return mem[i][M]

        # Assume opponent takes all remaining stones
        opponent = suffix[i]

        # Try every possible number of piles X
        for X in range(1, 2 * M + 1):
            opponent = min(
                opponent,
                self._stoneGameII(
                    suffix,
                    i + X,
                    max(M, X),
                    mem
                )
            )

        # Current player gets everything except
        # what the opponent can get
        mem[i][M] = suffix[i] - opponent

        return mem[i][M]
