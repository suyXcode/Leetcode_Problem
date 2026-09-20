class Solution:
    def reverseDegree(self, s):
        total = 0

        for i, ch in enumerate(s, 1):
            reverse_pos = 27 - (ord(ch) - ord('a') + 1)
            total += reverse_pos * i

        return total
