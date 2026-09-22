class Solution:
    def resultArray(self, nums, k, queries):
        n = len(nums)

        # Each node:
        # [total_product_mod_k, prefix_counts]
        tree = [[1, [0] * k] for _ in range(4 * n)]

        def merge(left, right):
            left_prod, left_pref = left
            right_prod, right_pref = right

            # Product of entire combined segment
            prod = (left_prod * right_prod) % k

            pref = left_pref[:]

            # Prefixes that continue into right segment
            for r in range(k):
                new_r = (left_prod * r) % k
                pref[new_r] += right_pref[r]

            return [prod, pref]

        def build(node, l, r):
            if l == r:
                value = nums[l] % k

                tree[node][0] = value
                tree[node][1][value] = 1
                return

            mid = (l + r) // 2

            build(node * 2, l, mid)
            build(node * 2 + 1, mid + 1, r)

            tree[node] = merge(
                tree[node * 2],
                tree[node * 2 + 1]
            )

        def update(node, l, r, index, value):
            if l == r:
                value %= k

                tree[node][0] = value
                tree[node][1] = [0] * k
                tree[node][1][value] = 1
                return

            mid = (l + r) // 2

            if index <= mid:
                update(node * 2, l, mid, index, value)
            else:
                update(node * 2 + 1, mid + 1, r, index, value)

            tree[node] = merge(
                tree[node * 2],
                tree[node * 2 + 1]
            )

        def query(node, l, r, ql, qr):
            if ql <= l and r <= qr:
                return tree[node]

            mid = (l + r) // 2

            if qr <= mid:
                return query(node * 2, l, mid, ql, qr)

            if ql > mid:
                return query(node * 2 + 1, mid + 1, r, ql, qr)

            left = query(node * 2, l, mid, ql, qr)
            right = query(node * 2 + 1, mid + 1, r, ql, qr)

            return merge(left, right)

        build(1, 0, n - 1)

        ans = []

        for index, value, start, x in queries:

            # Persistent update
            update(1, 0, n - 1, index, value)

            # Get [start ... n-1]
            _, prefix_count = query(
                1, 0, n - 1,
                start, n - 1
            )

            ans.append(prefix_count[x])

        return ans
