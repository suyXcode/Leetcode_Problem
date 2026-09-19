class Solution:
    def checkOverlap(self, radius, xCenter, yCenter, x1, y1, x2, y2):
        # Find the closest x-coordinate on the rectangle
        if xCenter < x1:
            closest_x = x1
        elif xCenter > x2:
            closest_x = x2
        else:
            closest_x = xCenter

        # Find the closest y-coordinate on the rectangle
        if yCenter < y1:
            closest_y = y1
        elif yCenter > y2:
            closest_y = y2
        else:
            closest_y = yCenter

        # Distance between circle center and closest rectangle point
        dx = xCenter - closest_x
        dy = yCenter - closest_y

        # Compare squared distances to avoid sqrt()
        return dx * dx + dy * dy <= radius * radius
