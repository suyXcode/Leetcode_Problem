
from collections import defaultdict

class Solution:
    def countServers(self, n, logs, x, queries):
        logs.sort(key=lambda log: log[1])

        sorted_queries = sorted(
            (q, i) for i, q in enumerate(queries)
        )

        freq = defaultdict(int)
        ans = [0] * len(queries)

        left = 0
        right = 0
        m = len(logs)

        for q, idx in sorted_queries:

            # Add logs with time <= q
            while right < m and logs[right][1] <= q:
                server = logs[right][0]
                freq[server] += 1
                right += 1

            # Remove logs with time < q - x
            while left < right and logs[left][1] < q - x:
                server = logs[left][0]

                freq[server] -= 1

                if freq[server] == 0:
                    del freq[server]

                left += 1

            # Servers with no requests
            ans[idx] = n - len(freq)

        return ans
