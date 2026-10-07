class Solution:
    def removeInvalidParentheses(self, s: str):
        # Find the minimum number of left and right parentheses
        # that must be removed.
        left_remove = 0
        right_remove = 0

        for ch in s:
            if ch == '(':
                left_remove += 1
            elif ch == ')':
                if left_remove > 0:
                    left_remove -= 1
                else:
                    right_remove += 1

        result = set()

        def dfs(index, left_count, right_count, left_rem, right_rem, path):
            # End of string
            if index == len(s):
                if left_rem == 0 and right_rem == 0 and left_count == right_count:
                    result.add("".join(path))
                return

            ch = s[index]

            # Option 1: Remove current parenthesis
            if ch == '(' and left_rem > 0:
                dfs(
                    index + 1,
                    left_count,
                    right_count,
                    left_rem - 1,
                    right_rem,
                    path
                )

            elif ch == ')' and right_rem > 0:
                dfs(
                    index + 1,
                    left_count,
                    right_count,
                    left_rem,
                    right_rem - 1,
                    path
                )

            # Option 2: Keep current character
            path.append(ch)

            if ch not in "()":
                dfs(
                    index + 1,
                    left_count,
                    right_count,
                    left_rem,
                    right_rem,
                    path
                )

            elif ch == '(':
                dfs(
                    index + 1,
                    left_count + 1,
                    right_count,
                    left_rem,
                    right_rem,
                    path
                )

            elif ch == ')' and right_count < left_count:
                dfs(
                    index + 1,
                    left_count,
                    right_count + 1,
                    left_rem,
                    right_rem,
                    path
                )

            path.pop()

        dfs(0, 0, 0, left_remove, right_remove, [])

        return list(result)
