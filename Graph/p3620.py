from collections import deque
from typing import List

class Solution:
    def findMaxPathScore(self, edges: List[List[int]], online: List[bool], k: int) -> int:
        n = len(online)

        graph = [[] for _ in range(n)]
        indegree = [0] * n
        weights = []

        for u, v, w in edges:
            graph[u].append((v, w))
            indegree[v] += 1
            weights.append(w)

        # Topological Sort
        q = deque()
        for i in range(n):
            if indegree[i] == 0:
                q.append(i)

        topo = []
        while q:
            u = q.popleft()
            topo.append(u)
            for v, _ in graph[u]:
                indegree[v] -= 1
                if indegree[v] == 0:
                    q.append(v)

        weights = sorted(set(weights))

        INF = float('inf')

        def check(limit):
            dist = [INF] * n
            dist[0] = 0

            for u in topo:
                if dist[u] == INF:
                    continue

                if u != 0 and u != n - 1 and not online[u]:
                    continue

                for v, w in graph[u]:
                    if w < limit:
                        continue
                    if v != 0 and v != n - 1 and not online[v]:
                        continue
                    if dist[u] + w < dist[v]:
                        dist[v] = dist[u] + w

            return dist[n - 1] <= k

        if not weights or not check(weights[0]):
            return -1

        lo, hi = 0, len(weights) - 1
        ans = -1

        while lo <= hi:
            mid = (lo + hi) // 2
            if check(weights[mid]):
                ans = weights[mid]
                lo = mid + 1
            else:
                hi = mid - 1

        return ans
