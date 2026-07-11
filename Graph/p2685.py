from typing import List

class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = [[] for _ in range(n)]

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = [False] * n
        ans = 0

        def dfs(node):
            visited[node] = True
            nodes = 1
            degree = len(graph[node])

            for nei in graph[node]:
                if not visited[nei]:
                    x, y = dfs(nei)
                    nodes += x
                    degree += y

            return nodes, degree

        for i in range(n):
            if not visited[i]:
                nodes, degree = dfs(i)
                edges_cnt = degree // 2

                if edges_cnt == nodes * (nodes - 1) // 2:
                    ans += 1

        return ans
