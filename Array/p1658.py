class Solution(object):
    def minOperations(self, nums, x):
        """
        :type nums: List[int]
        :type x: int
        :rtype: int
        """
        total = sum(nums)
        target = total - x

        # If target is negative, impossible
        if target < 0:
            return -1

        # target = 0 means remove everything
        if target == 0:
            return len(nums)

        left = 0
        curr_sum = 0
        max_len = -1

        for right in range(len(nums)):
            curr_sum += nums[right]

            # Shrink window if sum becomes too large
            while curr_sum > target and left <= right:
                curr_sum -= nums[left]
                left += 1

            # Found a valid subarray
            if curr_sum == target:
                max_len = max(max_len, right - left + 1)

        # Operations = elements removed
        if max_len == -1:
            return -1

        return len(nums) - max_len
