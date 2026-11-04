from typing import List

class FenwickTree:
    def __init__(self, n):
        self.n = n
        self.bit = [0] * (n + 1)

    def update(self, i, delta):
        i += 1
        while i <= self.n:
            self.bit[i] += delta
            i += i & -i

    def query(self, i):
        # Prefix sum [0, i)
        result = 0
        while i > 0:
            result += self.bit[i]
            i -= i & -i
        return result

    def kth(self, k):
        # Find index of kth smallest element (1-indexed)
        idx = 0
        bit_mask = 1 << (self.n.bit_length() - 1)

        while bit_mask:
            nxt = idx + bit_mask

            if nxt <= self.n and self.bit[nxt] < k:
                idx = nxt
                k -= self.bit[nxt]

            bit_mask >>= 1

        return idx


class Solution:
    def minOperations(self, nums: List[int], x: int, k: int) -> int:

        n = len(nums)

        # Step 1: Coordinate Compression
        vals = sorted(set(nums))
        m = len(vals)

        rank = {v: i for i, v in enumerate(vals)}

        arr = [rank[v] for v in nums]

        # Step 2: Fenwick Trees
        countBIT = FenwickTree(m)
        sumBIT = FenwickTree(m)

        def add(idx, value):
            countBIT.update(idx, value)
            sumBIT.update(idx, value * vals[idx])

        # Insert first window
        for i in range(x):
            add(arr[i], 1)

        costs = []

        # Step 3: Sliding Window + Median
        for i in range(n - x + 1):

            # Find median (lower median for even x)
            median_idx = countBIT.kth((x + 1) // 2)
            median = vals[median_idx]

            # Left side: values <= median
            left_count = countBIT.query(median_idx + 1)
            left_sum = sumBIT.query(median_idx + 1)

            # Right side: values > median
            right_count = x - left_count
            right_sum = sumBIT.query(m) - left_sum

            # Calculate minimum operations
            cost = (
                median * left_count - left_sum
                + right_sum - median * right_count
            )

            costs.append(cost)

            # Slide window
            if i < n - x:
                add(arr[i], -1)
                add(arr[i + x], 1)

        # Step 4: Dynamic Programming
        prev = [0] * (n + 1)

        for j in range(1, k + 1):

            curr = [float('inf')] * (n + 1)

            for i in range(1, n + 1):

                # Option 1: Skip current element
                curr[i] = curr[i - 1]

                # Option 2: Select a window of size x
                if i >= x:
                    start = i - x

                    curr[i] = min(
                        curr[i],
                        prev[start] + costs[start]
                    )

            prev = curr

        return prev[n]
