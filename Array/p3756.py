from typing import List

class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        MOD = 10**9 + 7

        m = len(s)

        # Prefix count of non-zero digits
        pref_cnt = [0] * (m + 1)

        nz = []
        for i, ch in enumerate(s):
            pref_cnt[i + 1] = pref_cnt[i]
            if ch != '0':
                pref_cnt[i + 1] += 1
                nz.append(int(ch))

        n = len(nz)

        # Powers of 10 modulo MOD
        pow10 = [1] * (n + 1)
        for i in range(1, n + 1):
            pow10[i] = (pow10[i - 1] * 10) % MOD

        # Prefix concatenated values
        pref_num = [0] * (n + 1)
        for i in range(n):
            pref_num[i + 1] = (pref_num[i] * 10 + nz[i]) % MOD

        # Prefix digit sums
        pref_sum = [0] * (n + 1)
        for i in range(n):
            pref_sum[i + 1] = pref_sum[i] + nz[i]

        ans = []

        for l, r in queries:
            left = pref_cnt[l]
            right = pref_cnt[r + 1]

            if left == right:
                ans.append(0)
                continue

            length = right - left

            x = (pref_num[right] - pref_num[left] * pow10[length]) % MOD
            digit_sum = pref_sum[right] - pref_sum[left]

            ans.append((x * digit_sum) % MOD)

        return ans
