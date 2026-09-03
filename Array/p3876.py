class Solution:
    def uniformArray(self, nums1: List[int]) -> bool:
        has_odd = False
        has_even = False
        minimum = min(nums1)

        for num in nums1:
            if num % 2 == 0:
                has_even = True
            else:
                has_odd = True

        # Already all odd or all even
        if not has_odd or not has_even:
            return True

        # Mixed parity is possible only if the minimum is odd
        return minimum % 2 == 1
