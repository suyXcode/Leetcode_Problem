# class Solution:
#     def mirrorDistance(self, n):
#         rev = 0
#         temp = n
        
#         while temp > 0:
#             digit = temp % 10
#             rev = rev * 10 + digit
#             temp //= 10
        
#         return abs(n - rev)

class Solution(object):
    def mirrorDistance(self, n):
        """
        :type n: int
        :rtype: int
        """
        return abs(int(str(n)[::-1]) - n)
