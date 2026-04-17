# LeetCode #200 — Number of Islands
# Time: O(m * n)  — every cell visited at most once
# Space: O(min(m,n))  — BFS queue holds at most min(m,n) cells at a time

from collections import deque

class Solution:
    # Time: O(m * n) | Space: O(min(m, n))
    def numIslands(self, grid: list[list[str]]) -> int:
        if not grid:
            return 0

        m, n = len(grid), len(grid[0])
        count = 0
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    count += 1
                    grid[i][j] = '0'   # mark as visited
                    queue = deque([(i, j)])

                    while queue:
                        r, c = queue.popleft()
                        for dr, dc in directions:
                            nr, nc = r + dr, c + dc
                            if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == '1':
                                grid[nr][nc] = '0'
                                queue.append((nr, nc))

        return count
