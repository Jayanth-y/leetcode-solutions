class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        self.island_count = 0
        seen = set()

        def processIsland(x, y):
            dirs = [(-1, 0), (0, -1), (0, 1), (1, 0)]
            ctc = [(x, y)]
            self.island_count += 1

            while ctc:
                cx, cy = ctc.pop()
                seen.add((cx, cy))

                for dx, dy in dirs:
                    i, j = cx+dx, cy+dy
                    if (0 <= i < m) and (0 <= j < n) and (int(grid[i][j]) == 1) and ((i, j) not in seen):
                        ctc.append((i, j))

        for i in range(m):
            for j in range(n):
                if int(grid[i][j]) == 1 and ((i, j) not in seen):
                    processIsland(i, j)

        return self.island_count

"""
Leetcode 200. Number of Islands

Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.
An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:
Input: grid = 
[
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

Example 2:
Input: grid = 
[
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
 
Constraints:
m == grid.length
n == grid[i].length
1 <= m, n <= 300
grid[i][j] is '0' or '1'.
"""
