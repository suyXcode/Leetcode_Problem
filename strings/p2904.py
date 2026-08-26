class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        n = len(s)
        left = 0
        ones = 0
        ans = ""

        for right in range(n):
            if s[right] == '1':
                ones += 1

            # Too many 1s -> move left
            while ones > k:
                if s[left] == '1':
                    ones -= 1
                left += 1

            # Exactly k ones
            if ones == k:
                # Remove leading zeroes
                while left <= right and s[left] == '0':
                    left += 1

                current = s[left:right + 1]

                # Shorter is better.
                # If same length, lexicographically smaller is better.
                if (ans == "" or
                    len(current) < len(ans) or
                    (len(current) == len(ans) and current < ans)):
                    ans = current

        return ans
