class Solution:
    def smallestSubsequence(self, s: str) -> str:
        # Store last occurrence of each character
        last = {c: i for i, c in enumerate(s)}

        stack = []
        visited = set()

        for i, c in enumerate(s):
            # Skip if already in the stack
            if c in visited:
                continue

            # Remove larger characters if they appear later
            while stack and stack[-1] > c and last[stack[-1]] > i:
                visited.remove(stack.pop())

            stack.append(c)
            visited.add(c)

        return "".join(stack)
