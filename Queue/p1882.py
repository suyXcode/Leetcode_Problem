
import heapq

class Solution:
    def assignTasks(self, servers, tasks):
        available = [(weight, i) for i, weight in enumerate(servers)]
        heapq.heapify(available)

        busy = []

        ans = []
        time = 0

        for j, task in enumerate(tasks):

            time = max(time, j)

            # Release all servers that have finished
            while busy and busy[0][0] <= time:
                finish, weight, idx = heapq.heappop(busy)
                heapq.heappush(available, (weight, idx))

            # If no server is free, wait for the earliest completion
            if not available:
                time = busy[0][0]

                # Release every server available at this time
                while busy and busy[0][0] <= time:
                    finish, weight, idx = heapq.heappop(busy)
                    heapq.heappush(available, (weight, idx))

            # Choose the server with minimum weight and index
            weight, idx = heapq.heappop(available)

            ans.append(idx)

            # Schedule the task
            heapq.heappush(
                busy,
                (time + task, weight, idx)
            )

        return ans
