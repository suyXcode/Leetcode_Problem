class Solution:
    def pivotArray(self, nums: list[int], pivot: int) -> list[int]:
        smaller = []
        equal = []
        greater = []

        for num in nums:
            if num < pivot:
                smaller.append(num)
            elif num == pivot:
                equal.append(num)
            else:
                greater.append(num)

        return smaller + equal + greater
