class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        MOD = 10**9 + 7
        m = r - l + 1

        if n == 1:
            return m

        size = 2 * m

        # state for length = 2
        base = [0] * size

        for v in range(m):
            base[v] = v                 # up[v]
            base[m + v] = m - v - 1     # down[v]

        if n == 2:
            return sum(base) % MOD

        # transition matrix
        T = [[0] * size for _ in range(size)]

        # up[v] <- down[u], u < v
        for v in range(m):
            for u in range(v):
                T[v][m + u] = 1

        # down[v] <- up[u], u > v
        for v in range(m):
            for u in range(v + 1, m):
                T[m + v][u] = 1

        def mat_mul(A, B):
            n1 = len(A)
            n2 = len(B[0])
            k = len(B)

            C = [[0] * n2 for _ in range(n1)]

            for i in range(n1):
                for t in range(k):
                    if A[i][t] == 0:
                        continue
                    a = A[i][t]
                    for j in range(n2):
                        C[i][j] = (C[i][j] + a * B[t][j]) % MOD

            return C

        def mat_pow(M, p):
            sz = len(M)

            R = [[0] * sz for _ in range(sz)]
            for i in range(sz):
                R[i][i] = 1

            while p:
                if p & 1:
                    R = mat_mul(R, M)

                M = mat_mul(M, M)
                p >>= 1

            return R

        P = mat_pow(T, n - 2)

        ans = 0
        for i in range(size):
            cur = 0
            for j in range(size):
                cur = (cur + P[i][j] * base[j]) % MOD
            ans = (ans + cur) % MOD

        return ans
