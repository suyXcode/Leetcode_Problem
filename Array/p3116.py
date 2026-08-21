from math import gcd


class Solution:
    def findKthSmallest(self, coins, k):
        n = len(coins)

        # lcm(a, b)
        def lcm(a, b):
            return a // gcd(a, b) * b

        # Store LCM for every subset
        subset_lcm = [1] * (1 << n)
        subset_bits = [0] * (1 << n)

        for mask in range(1, 1 << n):
            # Get one set bit
            bit = mask & -mask
            i = bit.bit_length() - 1

            prev = mask ^ bit

            if prev == 0:
                subset_lcm[mask] = coins[i]
            else:
                subset_lcm[mask] = lcm(subset_lcm[prev], coins[i])

                # If LCM becomes larger than our useful range,
                # it can be ignored during counting.
            
            subset_bits[mask] = subset_bits[prev] + 1

        def count(x):
            total = 0

            for mask in range(1, 1 << n):
                L = subset_lcm[mask]

                if L > x:
                    continue

                multiples = x // L

                if subset_bits[mask] % 2 == 1:
                    total += multiples
                else:
                    total -= multiples

            return total

        # Smallest possible answer
        left = 1

        # Since coin 1 <= 25, the smallest coin gives
        # at least k multiples by coin_min * k.
        right = min(coins) * k

        while left < right:
            mid = (left + right) // 2

            if count(mid) >= k:
                right = mid
            else:
                left = mid + 1

        return left
