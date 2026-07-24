class Solution:
    def uniqueXorTriplets(self, nums):
        n = len(nums)
        MAX_XOR = 2048  # since nums[i] <= 1500

        # pairXor[i][x] = True if XOR value x can be formed
        # by a pair (j, k) with i <= j <= k
        pairXor = [[False] * MAX_XOR for _ in range(n + 1)]

        for i in range(n - 1, -1, -1):
            pairXor[i] = pairXor[i + 1][:]

            # (i, i)
            pairXor[i][0] = True

            # (i, k)
            for k in range(i + 1, n):
                pairXor[i][nums[i] ^ nums[k]] = True

        seen = [False] * MAX_XOR

        for i in range(n):
            for x in range(MAX_XOR):
                if pairXor[i][x]:
                    seen[nums[i] ^ x] = True

        return sum(seen)
