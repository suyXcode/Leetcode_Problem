class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        t = "1" + s + "1"

        # Initial active sections
        ones = s.count('1')

        # Run-length encoding of t
        blocks = []
        for ch in t:
            if not blocks or blocks[-1][0] != ch:
                blocks.append([ch, 1])
            else:
                blocks[-1][1] += 1

        ans = ones

        # Check every removable block of 1's
        for i in range(1, len(blocks) - 1):
            if (
                blocks[i][0] == '1' and
                blocks[i - 1][0] == '0' and
                blocks[i + 1][0] == '0'
            ):
                gain = blocks[i - 1][1] + blocks[i + 1][1]
                ans = max(ans, ones + gain)

        return ans
