class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        

        from collections import Counter
        
        n = len(s)
        m = n // 2
        counts = Counter(s)
        
        # Check palindrome feasibility
        odd_chars = [c for c, count in counts.items() if count % 2 == 1]
        if len(odd_chars) > 1:
            return ""
        
        mid_char = odd_chars[0] if odd_chars else ""
        half_counts = {c: counts[c] // 2 for c in counts if counts[c] // 2 > 0}
        
        # Helper function to construct the full palindrome from the first half
        def make_palindrome(first_half: list) -> str:
            fh = "".join(first_half)
            return fh + mid_char + fh[::-1]

        # Case 1: Check if the exact prefix of target can form a valid strictly greater palindrome
        can_match_prefix = True
        temp_counts = half_counts.copy()
        for i in range(m):
            c = target[i]
            if temp_counts.get(c, 0) > 0:
                temp_counts[c] -= 1
            else:
                can_match_prefix = False
                break
                
        if can_match_prefix:
            candidate = make_palindrome(list(target[:m]))
            if candidate > target:
                return candidate

        # Case 2: Find the longest prefix match where we can make P[i] > target[i]
        # First, precompute character counts available up to each prefix length
        prefix_valid = True
        prefix_counts = [None] * (m + 1)
        curr_counts = half_counts.copy()
        prefix_counts[0] = curr_counts.copy()
        
        for i in range(m):
            c = target[i]
            if curr_counts.get(c, 0) > 0:
                curr_counts[c] -= 1
                prefix_counts[i + 1] = curr_counts.copy()
            else:
                break

        for i in range(m - 1, -1, -1):
            if prefix_counts[i] is None:
                continue
            
            avail = prefix_counts[i]
            # Try to pick the smallest character strictly greater than target[i]
            for c_code in range(ord(target[i]) + 1, ord('z') + 1):
                c = chr(c_code)
                if avail.get(c, 0) > 0:
                    # Construct the first half
                    first_half = list(target[:i]) + [c]
                    rem_avail = avail.copy()
                    rem_avail[c] -= 1
                    
                    # Fill the rest with the smallest characters available
                    for fill_code in range(ord('a'), ord('z') + 1):
                        fill_c = chr(fill_code)
                        cnt = rem_avail.get(fill_c, 0)
                        if cnt > 0:
                            first_half.extend([fill_c] * cnt)
                            
                    return make_palindrome(first_half)
                    
        return ""
