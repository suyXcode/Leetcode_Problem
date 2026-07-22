from typing import List

class SparseTable:
    def __init__(self, nums: List[int]):
        n = len(nums)
        if n == 0:
            self.st = []
            return
        
        K = n.bit_length()
        self.st = [[0] * n for _ in range(K)]
        self.st[0] = nums[:]
        
        for j in range(1, K):
            length = 1 << (j - 1)
            for i in range(n - (1 << j) + 1):
                self.st[j][i] = max(self.st[j - 1][i], self.st[j - 1][i + length])

    def query(self, L: int, R: int) -> int:
        if L > R or not self.st:
            return 0
        j = (R - L + 1).bit_length() - 1
        return max(self.st[j][L], self.st[j][R - (1 << j) + 1])


class Solution:
    def maxActiveSectionsAfterTrade(self, s: str, queries: List[List[int]]) -> List[int]:
        n = len(s)
        total_ones = s.count('1')

        # 1. Segment contiguous '0' blocks
        zero_groups = []
        zero_group_idx = [-1] * n

        for i, char in enumerate(s):
            if char == '0':
                if i > 0 and s[i - 1] == '0':
                    zero_groups[-1]['length'] += 1
                else:
                    zero_groups.append({'start': i, 'length': 1})
                zero_group_idx[i] = len(zero_groups) - 1
            else:
                zero_group_idx[i] = len(zero_groups) - 1 if zero_groups else -1

        num_groups = len(zero_groups)

        # 2. Precompute merge lengths for adjacent 0-groups
        zero_merge_lengths = [
            zero_groups[i]['length'] + zero_groups[i + 1]['length']
            for i in range(num_groups - 1)
        ]

        # 3. Build Sparse Table for O(1) RMQ
        st = SparseTable(zero_merge_lengths)

        ans = []

        # 4. Process each query in O(1) time
        for l, r in queries:
            g_l = zero_group_idx[l]
            g_r = zero_group_idx[r]

            # Length of left '0' segment inside [l, r]
            left_len = (
                zero_groups[g_l]['length'] - (l - zero_groups[g_l]['start'])
                if g_l != -1 and s[l] == '0'
                else -1
            )

            # Length of right '0' segment inside [l, r]
            right_len = (
                r - zero_groups[g_r]['start'] + 1
                if g_r != -1 and s[r] == '0'
                else -1
            )

            # Map boundary indices to fully contained adjacent zero-group merges
            start_adj = g_l + 1
            end_adj = g_r if s[r] == '1' else g_r - 1

            start_merge_idx = start_adj
            end_merge_idx = end_adj - 1

            best_active = total_ones

            # Case 1: Left and Right boundaries fall in adjacent groups separated by a '1'
            if s[l] == '0' and s[r] == '0' and g_l + 1 == g_r:
                best_active = max(best_active, total_ones + left_len + right_len)

            # Case 2: Fully contained adjacent group pairs inside [l, r]
            if start_merge_idx <= end_merge_idx:
                best_active = max(best_active, total_ones + st.query(start_merge_idx, end_merge_idx))

            # Case 3: Partial left boundary zero-group + full next zero-group
            if s[l] == '0':
                max_next = g_r if s[r] == '1' else g_r - 1
                if g_l + 1 <= max_next:
                    best_active = max(best_active, total_ones + left_len + zero_groups[g_l + 1]['length'])

            # Case 4: Full previous zero-group + partial right boundary zero-group
            if s[r] == '0':
                if g_l < g_r - 1:
                    best_active = max(best_active, total_ones + right_len + zero_groups[g_r - 1]['length'])

            ans.append(best_active)

        return ans
