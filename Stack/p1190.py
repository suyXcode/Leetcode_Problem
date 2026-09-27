class Solution:
    def reverseParentheses(self, s):
        stack = [""]

        for ch in s:
            if ch == '(':
                # Start a new level
                stack.append("")

            elif ch == ')':
                # Reverse current substring
                current = stack.pop()[::-1]

                # Add it to the previous level
                stack[-1] += current

            else:
                # Add character to current substring
                stack[-1] += ch

        return stack[0]
