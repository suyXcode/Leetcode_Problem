class Solution:
    def palindromePathQueries(self, n, edges, s, queries):
        graph = [[] for _ in range(n)]

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        LOG = n.bit_length()
        parent = [[0] * n for _ in range(LOG)]
        depth = [0] * n
        tin = [0] * n
        tout = [0] * n
        timer = 0

        # Iterative DFS: calculate Euler tour and parents
        stack = [(0, -1, 0)]

        while stack:
            u, p, state = stack.pop()

            if state == 0:
                tin[u] = timer
                timer += 1
                parent[0][u] = u if p == -1 else p

                stack.append((u, p, 1))

                for v in reversed(graph[u]):
                    if v != p:
                        depth[v] = depth[u] + 1
                        stack.append((v, u, 0))
            else:
                tout[u] = timer

        # Binary lifting for LCA
        for k in range(1, LOG):
            for u in range(n):
                parent[k][u] = parent[k - 1][parent[k - 1][u]]

        def is_ancestor(u, v):
            return tin[u] <= tin[v] < tout[u]

        def lca(u, v):
            if is_ancestor(u, v):
                return u
            if is_ancestor(v, u):
                return v

            for k in range(LOG - 1, -1, -1):
                anc = parent[k][u]
                if not is_ancestor(anc, v):
                    u = anc

            return parent[0][u]

        # Fenwick tree for range XOR updates and point queries
        bit = [0] * (n + 2)

        def add(pos, val):
            i = pos + 1
            while i <= n + 1:
                bit[i] ^= val
                i += i & -i

        def prefix(pos):
            result = 0
            i = pos
            while i > 0:
                result ^= bit[i]
                i -= i & -i
            return result

        def range_xor(left, right, val):
            add(left, val)
            add(right, val)

        def root_xor(u):
            return prefix(tin[u] + 1)

        chars = list(s)

        # Each character contributes to every node in its subtree.
        for u in range(n):
            mask = 1 << (ord(chars[u]) - ord('a'))
            range_xor(tin[u], tout[u], mask)

        ans = []

        for q in queries:
            parts = q.split()

            if parts[0] == "update":
                u = int(parts[1])
                c = parts[2]

                old_mask = 1 << (ord(chars[u]) - ord('a'))
                new_mask = 1 << (ord(c) - ord('a'))

                if old_mask != new_mask:
                    range_xor(
                        tin[u],
                        tout[u],
                        old_mask ^ new_mask
                    )
                    chars[u] = c

            else:
                u = int(parts[1])
                v = int(parts[2])

                w = lca(u, v)

                mask = (
                    root_xor(u)
                    ^ root_xor(v)
                    ^ (1 << (ord(chars[w]) - ord('a')))
                )

                ans.append((mask & (mask - 1)) == 0)

        return ans
