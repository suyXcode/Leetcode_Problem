class Solution:
    def stoneGameVIII(self, stones):
        n = len(stones)

        # Build prefix sums
        prefix = [0] * n
        prefix[0] = stones[0]

        for i in range(1, n):
            prefix[i] = prefix[i - 1] + stones[i]

        # If Alice merges all stones, this is the initial result
        dp = prefix[n - 1]

        # Work backwards
        for i in range(n - 2, 0, -1):
            dp = max(dp, prefix[i] - dp)

        return dp
