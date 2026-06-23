class Solution:
    def processStr(self, s: str) -> str:
        result = ""

        for ch in s:
            if ch.islower():
                result += ch
            elif ch == '*':
                result = result[:-1]
            elif ch == '#':
                result += result
            else:  # ch == '%'
                result = result[::-1]

        return result
