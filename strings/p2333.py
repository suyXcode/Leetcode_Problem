class Solution:
    def minSumSquareDiff(self, nums1, nums2, k1, k2):
        diff = [abs(a - b) for a, b in zip(nums1, nums2)]
        k = k1 + k2

        if sum(diff) <= k:
            return 0

        left, right = 0, max(diff)

        while left < right:
            mid = (left + right) // 2

            # Operations required to make every difference <= mid
            required = sum(max(0, d - mid) for d in diff)

            if required <= k:
                right = mid
            else:
                left = mid + 1

        # Reduce all differences to at most the optimal threshold
        threshold = left
        remaining = k

        for i in range(len(diff)):
            reduction = max(0, diff[i] - threshold)
            diff[i] -= reduction
            remaining -= reduction

        # Use remaining operations to reduce differences above zero
        for i in range(len(diff)):
            if remaining == 0:
                break
            if diff[i] == threshold and threshold > 0:
                diff[i] -= 1
                remaining -= 1

        return sum(d * d for d in diff)
