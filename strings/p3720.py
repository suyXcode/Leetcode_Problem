class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        alphabet = "abcdefghijklmnopqrstuvwxyz"

        # Count characters in s
        cnt = [0] * 26
        for ch in s:
            cnt[ord(ch) - 97] += 1

        def make_result(prefix):
            result = prefix[:]

            for i in range(26):
                result.append(alphabet[i] * cnt[i])

            return ''.join(result)

        ans = []

        # Try to match target as much as possible
        for i in range(len(target)):
            x = ord(target[i]) - 97

            if cnt[x] > 0:
                cnt[x] -= 1
                ans.append(target[i])
            else:
                break

        # Case 1:
        # We could not match target[i].
        # Try a character greater than target[i].
        if len(ans) < len(target):
            x = ord(target[len(ans)]) - 97

            for c in range(x + 1, 26):
                if cnt[c] > 0:
                    cnt[c] -= 1
                    return make_result(ans + [alphabet[c]])

        # Case 2:
        # We matched the whole target, or
        # no larger character was available at the first mismatch.
        #
        # Backtrack and increase an earlier character.
        for i in range(len(ans) - 1, -1, -1):
            x = ord(ans[i]) - 97

            # Put this character back
            cnt[x] += 1

            # Find the smallest character greater than it
            for c in range(x + 1, 26):
                if cnt[c] > 0:
                    cnt[c] -= 1

                    return make_result(ans[:i] + [alphabet[c]])

        return ""
