class Solution:
    def maxNumOfSubstrings(self, s):
        n = len(s)

        # First and last occurrence of every character
        first = [n] * 26
        last = [-1] * 26

        for i, ch in enumerate(s):
            idx = ord(ch) - ord('a')
            first[idx] = min(first[idx], i)
            last[idx] = i

        candidates = []

        # Try to create the smallest valid substring
        # starting from every character
        for c in range(26):
            if first[c] == n:
                continue

            left = first[c]
            right = last[c]
            i = left
            valid = True

            while i <= right:
                idx = ord(s[i]) - ord('a')

                # This character occurs before our left boundary
                if first[idx] < left:
                    valid = False
                    break

                # Expand to include all occurrences
                right = max(right, last[idx])

                i += 1

            if valid:
                candidates.append((right, left))

        # Choose intervals with earliest ending position
        candidates.sort()

        result = []
        prev_end = -1

        for right, left in candidates:
            if left > prev_end:
                result.append(s[left:right + 1])
                prev_end = right

        return result
