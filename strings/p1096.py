class Solution(object):
    def braceExpansionII(self, expression):
        """
        :type expression: str
        :rtype: List[str]
        """
        n = len(expression)

        def multiply(A, B):
            return {a + b for a in A for b in B}

        def parse_expr(i):
            """
            Parse an expression until '}' or end.
            Handles union using ','.
            """
            result = set()

            while i < n and expression[i] != '}':
                current, i = parse_term(i)

                result |= current

                if i < n and expression[i] == ',':
                    i += 1

            return result, i

        def parse_term(i):
            """
            Parse concatenated terms.
            Example:
            a{b,c}d
            """
            result = {""}

            while i < n and expression[i] not in '},':
                if expression[i] == '{':
                    # Parse inside braces
                    current, i = parse_expr(i + 1)

                    # Skip '}'
                    i += 1
                else:
                    current = {expression[i]}
                    i += 1

                result = multiply(result, current)

            return result, i

        result, _ = parse_expr(0)

        return sorted(result)

