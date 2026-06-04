class Solution:
    class Node:
        def __init__(self, cnt=0, wav=0):
            self.cnt = cnt
            self.wav = wav

    def __init__(self):
        self.s = ""
        self.memo = {}
        self.vis = set()

    def dfs(self, pos, p2, p1, started, tight, length):
        if pos == len(self.s):
            return self.Node(1, 0)

        key = (pos, p2, p1, started, length if length < 2 else 2)

        if not tight and key in self.vis:
            return self.memo[key]

        limit = int(self.s[pos]) if tight else 9

        ans = self.Node(0, 0)

        for d in range(limit + 1):
            ntight = tight and (d == limit)

            if not started and d == 0:
                nxt = self.dfs(pos + 1, 10, 10, False, ntight, 0)

                ans.cnt += nxt.cnt
                ans.wav += nxt.wav

            else:
                if not started:
                    nxt = self.dfs(pos + 1, 10, d, True, ntight, 1)

                    ans.cnt += nxt.cnt
                    ans.wav += nxt.wav

                else:
                    add = 0

                    if length >= 2:
                        if ((p1 > p2 and p1 > d) or
                            (p1 < p2 and p1 < d)):
                            add = 1

                    nxt = self.dfs(
                        pos + 1,
                        p1 if length >= 1 else 10,
                        d,
                        True,
                        ntight,
                        min(length + 1, 3)
                    )

                    ans.cnt += nxt.cnt
                    ans.wav += nxt.wav + add * nxt.cnt

        if not tight:
            self.vis.add(key)
            self.memo[key] = ans

        return ans

    def solve(self, n):
        if n <= 0:
            return 0

        self.s = str(n)
        self.memo.clear()
        self.vis.clear()

        return self.dfs(0, 10, 10, False, True, 0).wav

    def totalWaviness(self, num1: int, num2: int) -> int:
        return self.solve(num2) - self.solve(num1 - 1)
