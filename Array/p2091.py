class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n = len(nums)

        min_idx = nums.index(min(nums))
        max_idx = nums.index(max(nums))

        left = min(min_idx, max_idx)
        right = max(min_idx, max_idx)

        remove_from_front = right + 1
        remove_from_back = n - left
        remove_from_both = (left + 1) + (n - right)

        return min(
            remove_from_front,
            remove_from_back,
            remove_from_both
        )
