class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        st = []

        for c in s:
        # Push opening brackets
            if c in "({[":
                st.append(c)

        # Handle closing brackets
            elif c in ")}]":
                if not st:        # No opening bracket
                    return False
            
                top = st.pop()    # Remove last opening bracket
            
                if (c == ')' and top != '(') or \
                (c == '}' and top != '{') or \
                (c == ']' and top != '['):
                    return False

    # Final check: stack must be empty
        return len(st) == 0
        
