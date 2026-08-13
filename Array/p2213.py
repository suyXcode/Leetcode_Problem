class Solution:
    def longestRepeating(self, s, queryCharacters, queryIndices):
        n = len(s)

        # Each node:
        # [left_char, right_char, left_len, right_len, max_len, length]
        tree = [None] * (4 * n)

        def merge(a, b):
            if a is None:
                return b
            if b is None:
                return a

            left_char = a[0]
            right_char = b[1]

            left_len = a[2]
            right_len = b[3]
            max_len = max(a[4], b[4])

            # Prefix can extend into right segment
            if a[2] == a[5] and a[1] == b[0]:
                left_len = a[5] + b[2]

            # Suffix can extend into left segment
            if b[3] == b[5] and a[1] == b[0]:
                right_len = b[5] + a[3]

            # A repeating substring can cross the boundary
            if a[1] == b[0]:
                max_len = max(max_len, a[3] + b[2])

            return [
                left_char,
                right_char,
                left_len,
                right_len,
                max_len,
                a[5] + b[5]
            ]

        def build(node, start, end):
            if start == end:
                c = s[start]
                tree[node] = [c, c, 1, 1, 1, 1]
                return

            mid = (start + end) // 2

            build(node * 2, start, mid)
            build(node * 2 + 1, mid + 1, end)

            tree[node] = merge(
                tree[node * 2],
                tree[node * 2 + 1]
            )

        def update(node, start, end, idx, char):
            if start == end:
                tree[node] = [char, char, 1, 1, 1, 1]
                return

            mid = (start + end) // 2

            if idx <= mid:
                update(node * 2, start, mid, idx, char)
            else:
                update(node * 2 + 1, mid + 1, end, idx, char)

            tree[node] = merge(
                tree[node * 2],
                tree[node * 2 + 1]
            )

        build(1, 0, n - 1)

        ans = []

        for char, idx in zip(queryCharacters, queryIndices):
            update(1, 0, n - 1, idx, char)
            ans.append(tree[1][4])

        return ans
