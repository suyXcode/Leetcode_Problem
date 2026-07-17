from collections import Counter
from bisect import bisect_right

class Solution:
    def gcdValues(self, nums, queries):
        mx = max(nums)

        # Frequency of each value
        freq = [0] * (mx + 1)
        for x in nums:
            freq[x] += 1

        # cnt[d] = numbers divisible by d
        cnt = [0] * (mx + 1)
        for d in range(1, mx + 1):
            for multiple in range(d, mx + 1, d):
                cnt[d] += freq[multiple]

        # exact[d] = number of pairs with gcd exactly d
        exact = [0] * (mx + 1)

        for d in range(mx, 0, -1):
            c = cnt[d]
            pairs = c * (c - 1) // 2

            multiple = 2 * d
            while multiple <= mx:
                pairs -= exact[multiple]
                multiple += d

            exact[d] = pairs

        # Prefix sums over gcd values
        prefix = []
        values = []
        total = 0

        for d in range(1, mx + 1):
            if exact[d]:
                total += exact[d]
                prefix.append(total)
                values.append(d)

        ans = []
        for q in queries:
            idx = bisect_right(prefix, q)
            ans.append(values[idx])

        return ans
