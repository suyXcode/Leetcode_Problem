class Solution:
    def maxProduct(self, n: int) -> int:
        # Convert the integer to a string to access individual digits
        digits = [int(d) for d in str(n)]
        
        # Sort the digits in ascending order
        digits.sort()
        
        # Multiply the two largest digits (the last two in sorted list)
        return digits[-1] * digits[-2]
