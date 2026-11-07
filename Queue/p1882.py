
import heapq

class Solution:
    def assignTasks(self, servers, tasks):
        n = len(servers)
        m = len(tasks)

        # Available servers: (weight, index)
        available = [
            (weight, i)
            for i, weight in enumerate(servers)
        ]
        heapq.heapify(available)

        # Busy servers: (finish_time, weight, index)
        busy = []

        ans = [0] * m

        for j in range(m):

            # Release all servers that have finished
            while busy and busy[0][0] <= j:
                finish, weight, idx = heapq.heappop(busy)
                heapq.heappush(available, (weight, idx))

            # If no server is free, wait for the earliest one
            if not available:
                current_time = busy[0][0]

                # Release all servers free at current_time
                while busy and busy[0][0] <= current_time:
                    finish, weight, idx = heapq.heappop(busy)
                    heapq.heappush(available, (weight, idx))

            # Select the best available server
            weight, idx = heapq.heappop(available)

            ans[j] = idx

            # Assign task and calculate finish time
            finish_time = max(j, current_time if not available and False else j) + tasks[j]

            heapq.heappush(
                busy,
                (finish_time, weight, idx)
            )

        return ans
