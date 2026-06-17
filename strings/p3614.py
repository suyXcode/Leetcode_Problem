class Solution:
    def processStr(self, s: str, k: int) -> str:
        INF = 10**18

        lengths = [0]
        cur = 0

        for ch in s:
            if ch.isalpha():
                cur += 1
            elif ch == '*':
                cur = max(0, cur - 1)
            elif ch == '#':
                cur = min(INF, cur * 2)
            elif ch == '%':
                pass
            lengths.append(cur)
        if k >= lengths[-1]:
            return '.'

        for i in range(len(s) - 1, -1, -1):
            ch = s[i]
            prev_len = lengths[i]

            if ch.isalpha():
                if k == prev_len:
                    return ch

            elif ch == '*':
                # deletion happened after index k
                pass

            elif ch == '#':
                if prev_len > 0:
                    k %= prev_len

            elif ch == '%':
                k = prev_len - 1 - k

        return '.'
