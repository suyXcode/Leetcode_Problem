class Solution:
    def numberOfSets(self, n: int, k: int) -> int:
        MOD = 10**9 + 7

        # Calculate C(n + k - 1, 2k)
        N = n + k - 1
        R = 2 * k

        # factorials
        fact = [1] * (N + 1)

        for i in range(1, N + 1):
            fact[i] = fact[i - 1] * i % MOD

        # Modular inverse using Fermat's Little Theorem
        def mod_inverse(x):
            return pow(x, MOD - 2, MOD)

        numerator = fact[N]
        denominator = fact[R] * fact[N - R] % MOD

        return numerator * mod_inverse(denominator) % MOD
