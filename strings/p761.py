class Solution:
    def makeLargestSpecial(self, s: str) -> str:
        def solve(s):
            parts = []
            count = 0
            start = 0

            for i, ch in enumerate(s):
                if ch == '1':
                    count += 1
                else:
                    count -= 1

                # Found one complete special substring
                if count == 0:
                    # Remove outer 1 and 0
                    inner = s[start + 1:i]

                    # Recursively maximize the inside
                    inner = solve(inner)

                    # Restore outer 1 and 0
                    parts.append('1' + inner + '0')

                    start = i + 1

            # Put largest special substrings first
            parts.sort(reverse=True)

            return ''.join(parts)

        return solve(s)
