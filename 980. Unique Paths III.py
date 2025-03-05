class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        
        def findUPIII(i: int, j: int, remaining: int) -> None:
            nonlocal ans
            
            # Step 6: If we reach the end position, check if all empty squares are visited
            if (i, j) == end:
                if remaining == 0: ans += 1  # Valid path found
                return

            # Step 7: Mark current cell as visited
            grid[i][j] = -1  

            # Step 8: Move in four possible directions
            for (dx, dy) in dirs:
                x, y = i+dx, j+dy
                if 0 <= x < m and 0 <= y < n and grid[x][y] in {0, 2}:
                    findUPIII(x, y, remaining-1)

            # Step 9: Backtrack - Restore cell to its original value
            grid[i][j] = 0  

        # Step 1: Initialize dimensions, directions, and answer counter
        m, n = len(grid), len(grid[0])
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        ans = 0
        empty_squares = 0

        # Step 2 & 3: Locate start, end, and count empty squares
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    start = (i, j)
                elif grid[i][j] == 2:
                    end = (i, j)
                if grid[i][j] == 0:
                    empty_squares += 1

        # Step 4: Start DFS with total required steps (including start square)
        findUPIII(start[0], start[1], empty_squares+1)
        
        # Step 10: Return the number of valid paths found
        return ans
"""
Leetcode 980: Unique Paths III (https://leetcode.com/problems/unique-paths-iii/)

You are given an m x n integer array grid where grid[i][j] could be:
  a. 1 representing the starting square. There is exactly one starting square.
  b. 2 representing the ending square. There is exactly one ending square.
  c. 0 representing empty squares we can walk over.
  d. -1 representing obstacles that we cannot walk over.
Return the number of 4-directional walks from the starting square to the ending square, that walk over every non-obstacle square exactly once.

Example 1:
Input: grid = [[1,0,0,0],[0,0,0,0],[0,0,2,-1]]
Output: 2
Explanation: We have the following two paths: 
1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2)
2. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2)

Example 2:
Input: grid = [[1,0,0,0],[0,0,0,0],[0,0,0,2]]
Output: 4
Explanation: We have the following four paths: 
1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2),(2,3)
2. (0,0),(0,1),(1,1),(1,0),(2,0),(2,1),(2,2),(1,2),(0,2),(0,3),(1,3),(2,3)
3. (0,0),(1,0),(2,0),(2,1),(2,2),(1,2),(1,1),(0,1),(0,2),(0,3),(1,3),(2,3)
4. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2),(2,3)

Example 3:
Input: grid = [[0,1],[2,0]]
Output: 0
Explanation: There is no path that walks over every empty square exactly once.
Note that the starting and ending square can be anywhere in the grid.
 
Constraints:
m == grid.length
n == grid[i].length
1 <= m, n <= 20
1 <= m * n <= 20
-1 <= grid[i][j] <= 2
There is exactly one starting cell and one ending cell.

Approach: 
1. Find the starting position (1) and ending position (2) in the grid.
2. Count the number of empty squares (0), which must be visited exactly once before reaching the ending square.
3. Use backtracking with DFS to explore all possible paths from the start position to the end position.
4. Mark the current cell as visited (-1) before exploring its neighbors to prevent revisiting.
5. Try moving in four directions (up, down, left, right) and continue recursion if the new cell is not an obstacle (-1) and within bounds.
6. If we reach the end position and all empty squares have been visited (remaining == 0), count this as a valid path.
7. Backtrack by restoring the cell value to 0 after recursion to allow other paths to be explored.
8. Return the total count of valid paths.
"""
