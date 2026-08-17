from typing import List


class Solution:
    def stoneGameV(self, stoneValue: List[int]) -> int:
        n = len(stoneValue)

        # Prefix sums
        prefix = [0] * (n + 1)

        for i in range(n):
            prefix[i + 1] = prefix[i] + stoneValue[i]

        # dp[l][r] = maximum score obtainable from l...r
        dp = [[0] * n for _ in range(n)]

        # For every left boundary l:
        # p[l] = largest split k currently satisfying
        #        leftSum <= rightSum
        p = [-1] * n

        # Best candidate from the left side
        best_left = [0] * n

        # For every right boundary r:
        # q[r] = smallest split k currently satisfying
        #        rightSum <= leftSum
        q = [0] * n

        # Best candidate from the right side
        best_right = [0] * n

        # Process r from left to right.
        # For each r, process l from right to left.
        for r in range(n):
            q[r] = r

            for l in range(r - 1, -1, -1):

                total = prefix[r + 1] - prefix[l]

                # -------------------------------------------------
                # LEFT SIDE:
                # leftSum <= rightSum
                #
                # 2 * leftSum <= total
                # -------------------------------------------------
                while (
                    p[l] + 1 <= r - 1
                    and 2 * (prefix[p[l] + 2] - prefix[l]) <= total
                ):
                    p[l] += 1
                    k = p[l]

                    left_sum = prefix[k + 1] - prefix[l]

                    best_left[l] = max(
                        best_left[l],
                        left_sum + dp[l][k]
                    )

                # -------------------------------------------------
                # RIGHT SIDE:
                # rightSum <= leftSum
                #
                # 2 * rightSum <= total
                # -------------------------------------------------
                while (
                    q[r] - 1 >= l
                    and 2 * (prefix[r + 1] - prefix[q[r]]) <= total
                ):
                    q[r] -= 1
                    k = q[r]

                    right_sum = prefix[r + 1] - prefix[k + 1]

                    best_right[r] = max(
                        best_right[r],
                        right_sum + dp[k + 1][r]
                    )

                # Best valid choice
                dp[l][r] = max(
                    best_left[l],
                    best_right[r]
                )

        return dp[0][n - 1]
