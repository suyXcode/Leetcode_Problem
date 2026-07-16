class Solution(object):
    def gcd(self, a, b):
        while b:
            a, b = b, a % b
        return a

    def gcdSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        prefix_gcd = []
        mx = 0

        for x in nums:
            if x > mx:
                mx = x
            prefix_gcd.append(self.gcd(x, mx))

        prefix_gcd.sort()

        ans = 0
        i, j = 0, len(prefix_gcd) - 1

        while i < j:
            ans += self.gcd(prefix_gcd[i], prefix_gcd[j])
            i += 1
            j -= 1

        return ans
