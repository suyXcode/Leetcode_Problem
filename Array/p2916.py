from typing import List

class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)

        tree = [0] * (4 * n)
        lazy = [0] * (4 * n)
        sq = [0] * (4 * n)

        def push(node, l, r):
            if lazy[node] == 0:
                return

            val = lazy[node]
            mid = (l + r) // 2
            left = node * 2
            right = left + 1

            len_left = mid - l + 1
            len_right = r - mid

            sq[left] = (
                sq[left] + 2 * val * tree[left]
                + val * val * len_left
            ) % MOD

            sq[right] = (
                sq[right] + 2 * val * tree[right]
                + val * val * len_right
            ) % MOD

            tree[left] = (tree[left] + val * len_left) % MOD
            tree[right] = (tree[right] + val * len_right) % MOD

            lazy[left] = (lazy[left] + val) % MOD
            lazy[right] = (lazy[right] + val) % MOD
            lazy[node] = 0

        def update(node, l, r, ql, qr, val):
            if ql <= l and r <= qr:
                sq[node] = (
                    sq[node] + 2 * val * tree[node]
                    + val * val * (r - l + 1)
                ) % MOD

                tree[node] = (
                    tree[node] + val * (r - l + 1)
                ) % MOD

                lazy[node] = (lazy[node] + val) % MOD
                return

            push(node, l, r)
            mid = (l + r) // 2

            if ql <= mid:
                update(node * 2, l, mid, ql, qr, val)

            if qr > mid:
                update(node * 2 + 1, mid + 1, r, ql, qr, val)

            tree[node] = (tree[node * 2] + tree[node * 2 + 1]) % MOD
            sq[node] = (sq[node * 2] + sq[node * 2 + 1]) % MOD

        last = {}
        ans = 0

        for i, x in enumerate(nums):
            prev = last.get(x, -1)

            update(1, 0, n - 1, prev + 1, i, 1)

            ans = (ans + sq[1]) % MOD
            last[x] = i

        return ans
