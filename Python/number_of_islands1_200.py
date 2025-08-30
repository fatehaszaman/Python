#ONLY IF YOU IMPORT FROM COLLECTIONS AND IS FASTER PYTHON VERSION
# Leecode question number 202

from collections import deque

class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        if not grid:
            return 0

        m, n = len(grid), len(grid[0])
        count = 0

        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    count += 1
                    grid[i][j] = '0'  # mark as visited
                    queue = deque([(i, j)])

                    while queue:
                        r, c = queue.popleft()
                        for dr, dc in directions:
                            nr, nc = r + dr, c + dc
                            if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == '1':
                                grid[nr][nc] = '0'
                                queue.append((nr, nc))

        return count
