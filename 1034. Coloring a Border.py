class Solution:
    def colorBorder(self, grid: List[List[int]], r: int, c: int, bc: int) -> List[List[int]]:
        m , n = len(grid), len(grid[0])
        ctc = [(r, c)]
        cc = grid[r][c]

        dirs = [(-1, 0), (0, -1), (0, 1), (1, 0)]
        seen = set()
        bcc = set()

        def isBorderCell(i, j):
            cells = 4
            if i > 0 and grid[i-1][j] == cc: cells -= 1
            if j > 0 and grid[i][j-1] == cc: cells -= 1
            if i < m-1 and grid[i+1][j] == cc: cells -= 1
            if j < n-1 and grid[i][j+1] == cc: cells -= 1
            return True if (cells != 0) else False

        while ctc:
            x, y = ctc.pop()
            seen.add((x, y))

            if isBorderCell(x, y) == True: 
                bcc.add((x, y))

            for (dx, dy) in dirs:
                    i, j = x+dx, y+dy
                    if (0 <= i < m) and (0 <= j < n) and (grid[i][j] == cc) and ((i, j) not in seen):
                        ctc.append((i, j))
        
        for (i, j) in bcc:
            grid[i][j] = bc
        
        return grid
      
"""
Leetcode 1034. Coloring a Border

You are given an m x n integer matrix grid, and three integers row, col, and color. Each value in the grid represents the color of the grid square at that location.
Two squares are called adjacent if they are next to each other in any of the 4 directions.
Two squares belong to the same connected component if they have the same color and they are adjacent.
The border of a connected component is all the squares in the connected component that are either adjacent to (at least) a square not in the component, or on the boundary of the grid (the first or last row or column).
You should color the border of the connected component that contains the square grid[row][col] with color.
Return the final grid.

Example 1:
Input: grid = [[1,1],[1,2]], row = 0, col = 0, color = 3
Output: [[3,3],[3,2]]

Example 2:
Input: grid = [[1,2,2],[2,3,2]], row = 0, col = 1, color = 3
Output: [[1,3,3],[2,3,3]]

Example 3:
Input: grid = [[1,1,1],[1,1,1],[1,1,1]], row = 1, col = 1, color = 2
Output: [[2,2,2],[2,1,2],[2,2,2]]
 
Constraints:
m == grid.length
n == grid[i].length
1 <= m, n <= 50
1 <= grid[i][j], color <= 1000
0 <= row < m
0 <= col < n
"""
