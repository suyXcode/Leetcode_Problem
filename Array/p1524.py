class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        MOD = 10**9 + 7

        even = 0
        odd = 0
        ans = 0

        for num in arr:
            if num % 2 == 1:
                even, odd = odd, even + 1
            else:
                even += 1

            ans = (ans + odd) % MOD

        return ans
