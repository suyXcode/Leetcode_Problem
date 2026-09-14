class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        x1, y1, x2, y2 = rec1
        a1, b1, a2, b2 = rec2

        return x1 < a2 and a1 < x2 and y1 < b2 and b1 < y2
