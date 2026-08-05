from typing import List
from collections import deque

class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        # Build graph
        graph = [[] for _ in range(n)]
        for u, v in invocations:
            graph[u].append(v)

        # Find all suspicious methods
        suspicious = [False] * n
        q = deque([k])
        suspicious[k] = True

        while q:
            node = q.popleft()
            for nei in graph[node]:
                if not suspicious[nei]:
                    suspicious[nei] = True
                    q.append(nei)

        # Check if any outside method invokes a suspicious method
        for u, v in invocations:
            if not suspicious[u] and suspicious[v]:
                return list(range(n))

        # Return remaining methods
        ans = []
        for i in range(n):
            if not suspicious[i]:
                ans.append(i)

        return ans
