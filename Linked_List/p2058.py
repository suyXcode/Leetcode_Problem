class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        prev = head
        curr = head.next
        index = 1

        first = -1
        prev_critical = -1
        min_dist = float('inf')

        while curr.next:
            nxt = curr.next

            # Check if curr is a critical point
            if (
                (curr.val > prev.val and curr.val > nxt.val) or
                (curr.val < prev.val and curr.val < nxt.val)
            ):
                if first == -1:
                    first = index
                else:
                    min_dist = min(
                        min_dist,
                        index - prev_critical
                    )

                prev_critical = index

            prev = curr
            curr = nxt
            index += 1

        # Fewer than 2 critical points
        if min_dist == float('inf'):
            return [-1, -1]

        max_dist = prev_critical - first

        return [min_dist, max_dist]
