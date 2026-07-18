class Solution:
    def findGCD(self, nums):
        smallest = min(nums)
        largest = max(nums)

        while smallest != 0:
            largest, smallest = smallest, largest % smallest

        return largest
