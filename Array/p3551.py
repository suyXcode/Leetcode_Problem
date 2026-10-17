class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        def digit_sum(n):
            total = 0
            while n:
                total += n % 10
                n //= 10
            return total

        n = len(nums)

        # Sort by digit sum, then by number
        sorted_nums = sorted(nums, key=lambda x: (digit_sum(x), x))

        # Map each number to its target index
        target = {num: i for i, num in enumerate(sorted_nums)}

        visited = [False] * n
        swaps = 0

        # Count cycles in the permutation
        for i in range(n):
            if visited[i] or target[nums[i]] == i:
                continue

            cycle_size = 0
            j = i

            while not visited[j]:
                visited[j] = True
                j = target[nums[j]]
                cycle_size += 1

            swaps += cycle_size - 1

        return swaps
