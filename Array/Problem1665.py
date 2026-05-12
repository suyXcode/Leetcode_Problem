class Solution:
    def minimumEffort(self, tasks):
        
        # Sort by (minimum - actual) in descending order
        tasks.sort(key=lambda x: (x[1] - x[0]), reverse=True)

        energy = 0
        ans = 0

        for actual, minimum in tasks:

            # Add extra energy if needed
            if energy < minimum:
                ans += (minimum - energy)
                energy = minimum

            # Complete the task
            energy -= actual

        return ans
