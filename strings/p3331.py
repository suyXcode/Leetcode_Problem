class Solution:
    def findSubtreeSizes(self, parent: list[int], s: str) -> list[int]:
        n = len(parent)

        tree = [[] for _ in range(n)]
        for i in range(1, n):
            tree[parent[i]].append(i)

        new_parent = parent[:]
        last = {}

        def dfs(u):
            ch = s[u]
            prev = last.get(ch, -1)

            if prev != -1:
                new_parent[u] = prev

            last[ch] = u

            for v in tree[u]:
                dfs(v)

            if prev == -1:
                del last[ch]
            else:
                last[ch] = prev

        dfs(0)

        # Build the modified tree
        new_tree = [[] for _ in range(n)]

        for i in range(1, n):
            new_tree[new_parent[i]].append(i)

        ans = [0] * n

        def calculate(u):
            ans[u] = 1

            for v in new_tree[u]:
                ans[u] += calculate(v)

            return ans[u]

        calculate(0)

        return ans
