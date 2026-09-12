from typing import List
from bisect import bisect_right


class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)

        # Store [left, right, weight, original_index]
        arr = [
            [l, r, w, i]
            for i, (l, r, w) in enumerate(intervals)
        ]

        # Sort by left endpoint
        arr.sort()

        # All left endpoints, used for binary search
        starts = [x[0] for x in arr]

        # next_idx[i] = first interval with left > arr[i].right
        next_idx = [n] * n

        for i in range(n):
            r = arr[i][1]
            next_idx[i] = bisect_right(starts, r)

        # dp[k][i] = best result using at most k intervals
        # from indices i ... n-1
        #
        # Each value is (maximum_weight, tuple_of_original_indices)
        dp = [[(0, ()) for _ in range(n + 1)] for _ in range(5)]

        for k in range(1, 5):
            for i in range(n - 1, -1, -1):

                # Option 1: don't take this interval
                skip_weight, skip_indices = dp[k][i + 1]

                # Option 2: take this interval
                j = next_idx[i]

                take_weight = arr[i][2]
                take_indices = (arr[i][3],)

                if j < n:
                    rest_weight, rest_indices = dp[k - 1][j]
                    take_weight += rest_weight
                    take_indices += rest_indices

                # Choose the better option:
                # 1. Larger weight
                # 2. If equal, lexicographically smaller indices
                if take_weight > skip_weight:
                    dp[k][i] = (take_weight, take_indices)
                elif take_weight < skip_weight:
                    dp[k][i] = (skip_weight, skip_indices)
                else:
                    dp[k][i] = min(
                        (take_weight, take_indices),
                        (skip_weight, skip_indices),
                        key=lambda x: x[1]
                    )

        return list(dp[4][0][1])
