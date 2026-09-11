class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        count = 0

        for a in range(1, 10):          # Hundreds digit
            for b in range(10):         # Tens digit
                for c in range(0, 10, 2):  # Units digit must be even

                    required = [a, b, c]
                    available = digits.copy()

                    possible = True

                    for d in required:
                        if d in available:
                            available.remove(d)
                        else:
                            possible = False
                            break

                    if possible:
                        count += 1

        return count
