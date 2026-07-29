from collections import Counter

class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:
        cnt = Counter(s)
        
        half = {}
        middle = ""
        
        # Build half counts and middle character
        for ch in sorted(cnt):
            half[ch] = cnt[ch] // 2
            if cnt[ch] % 2:
                middle = ch

        MAX_K = k + 1  # Cap to prevent unbounded huge integer math

        def combinations(n, r):
            """Returns C(n, r) capped at MAX_K."""
            if r < 0 or r > n:
                return 0
            r = min(r, n - r)
            res = 1
            for i in range(1, r + 1):
                res = res * (n - i + 1) // i
                if res >= MAX_K:
                    return MAX_K
            return res

        def count_ways(freqs):
            """Calculates total unique permutations of freqs, capped at MAX_K."""
            total = sum(freqs.values())
            ans = 1
            for v in freqs.values():
                if v == 0:
                    continue
                ans *= combinations(total, v)
                if ans >= MAX_K:
                    return MAX_K
                total -= v
            return ans

        # Check if k-th palindrome exists
        if count_ways(half) < k:
            return ""

        left = []
        total_len = sum(half.values())

        # Construct left half character by character
        for _ in range(total_len):
            for ch in sorted(half):
                if half[ch] == 0:
                    continue

                half[ch] -= 1
                w = count_ways(half)

                if w >= k:
                    left.append(ch)
                    break
                
                k -= w
                half[ch] += 1

        left_str = "".join(left)
        return left_str + middle + left_str[::-1]
