class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[int]:
        arr = sorted((v, i) for i, v in enumerate(nums))

        pos = [0] * n
        vals = [0] * n
        for i, (v, idx) in enumerate(arr):
            vals[i] = v
            pos[idx] = i

        # next jump (furthest right within maxDiff)
        nxt = [0] * n
        r = 0
        for l in range(n):
            while r + 1 < n and vals[r + 1] - vals[l] <= maxDiff:
                r += 1
            nxt[l] = r

        # previous jump (furthest left within maxDiff)
        prv = [0] * n
        l = 0
        for r in range(n):
            while vals[r] - vals[l] > maxDiff:
                l += 1
            prv[r] = l

        LOG = n.bit_length()

        upR = [nxt[:]]
        upL = [prv[:]]

        for _ in range(LOG - 1):
            last = upR[-1]
            upR.append([last[last[i]] for i in range(n)])

            last = upL[-1]
            upL.append([last[last[i]] for i in range(n)])

        ans = []

        for u, v in queries:
            a = pos[u]
            b = pos[v]

            if a == b:
                ans.append(0)
                continue

            if a < b:
                cur = a
                steps = 0

                for k in range(LOG - 1, -1, -1):
                    nxtPos = upR[k][cur]
                    if nxtPos < b:
                        cur = nxtPos
                        steps += 1 << k

                if nxt[cur] < b:
                    ans.append(-1)
                else:
                    ans.append(steps + 1)

            else:
                cur = a
                steps = 0

                for k in range(LOG - 1, -1, -1):
                    nxtPos = upL[k][cur]
                    if nxtPos > b:
                        cur = nxtPos
                        steps += 1 << k

                if prv[cur] > b:
                    ans.append(-1)
                else:
                    ans.append(steps + 1)

        return ans
