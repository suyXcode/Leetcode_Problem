from collections import deque

class Solution:
    def minMoves(self, classroom: list[str], energy: int) -> int:
        m = len(classroom)
        n = len(classroom[0])

        # Find start and assign each litter an index
        start = None
        litter = {}

        for r in range(m):
            for c in range(n):
                if classroom[r][c] == 'S':
                    start = (r, c)
                elif classroom[r][c] == 'L':
                    litter[(r, c)] = len(litter)

        total_litter = len(litter)
        target_mask = (1 << total_litter) - 1

        # BFS state:
        # (row, col, collected_mask, remaining_energy)
        q = deque()
        q.append((start[0], start[1], 0, energy, 0))

        # visited[row][col][mask][energy]
        visited = set()
        visited.add((start[0], start[1], 0, energy))

        directions = [
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1)
        ]

        while q:
            r, c, mask, e, moves = q.popleft()

            # All litter collected
            if mask == target_mask:
                return moves

            # Cannot move with no energy
            if e == 0:
                continue

            for dr, dc in directions:
                nr = r + dr
                nc = c + dc

                # Outside grid
                if not (0 <= nr < m and 0 <= nc < n):
                    continue

                # Obstacle
                if classroom[nr][nc] == 'X':
                    continue

                new_energy = e - 1
                new_mask = mask

                # Collect litter
                if classroom[nr][nc] == 'L':
                    idx = litter[(nr, nc)]
                    new_mask |= (1 << idx)

                # Reset energy
                if classroom[nr][nc] == 'R':
                    new_energy = energy

                state = (nr, nc, new_mask, new_energy)

                if state not in visited:
                    visited.add(state)
                    q.append((
                        nr,
                        nc,
                        new_mask,
                        new_energy,
                        moves + 1
                    ))

        return -1
