class Solution:
    def minSumOfLengths(self, arr, target):
        n = len(arr)

        # best[i] = minimum length of a valid subarray
        # ending at or before index i
        best = [float('inf')] * n

        left = 0
        curr_sum = 0
        ans = float('inf')

        for right in range(n):
            curr_sum += arr[right]

            # Shrink window if sum becomes greater than target
            while curr_sum > target:
                curr_sum -= arr[left]
                left += 1

            # Found a subarray with sum == target
            if curr_sum == target:
                length = right - left + 1

                # Check if there is a previous non-overlapping subarray
                if left > 0 and best[left - 1] != float('inf'):
                    ans = min(ans, length + best[left - 1])

                # Store the shortest valid subarray ending here
                if right == 0:
                    best[right] = length
                else:
                    best[right] = min(best[right - 1], length)

            else:
                # No valid subarray ending at right,
                # carry forward the previous best
                if right > 0:
                    best[right] = best[right - 1]

        return -1 if ans == float('inf') else ans
