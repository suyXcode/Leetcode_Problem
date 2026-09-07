class Solution:
    def distinctSubseqII(self, s: str) -> int:
        MOD = 10**9 + 7

        dp = 1
        last = {}

        for c in s:
            new_dp = 2 * dp - last.get(c, 0)

            last[c] = dp
            dp = new_dp % MOD

        return (dp - 1) % MOD
