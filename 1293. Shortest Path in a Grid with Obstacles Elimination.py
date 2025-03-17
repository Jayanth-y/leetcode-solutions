class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])

        # Step 1: Initialize BFS queue with (x, y, remaining k, moves)
        queue = deque([(0, 0, k, 0)])
        seen = set([(0, 0, k)])

        # Step 3: Define movement directions
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        # Step 4: Perform BFS
        while queue:
            x, y, rk, moves = queue.popleft()
            
            # Step 4a: If we reach the bottom-right corner, return moves
            if (x, y) == (m-1, n-1): return moves

            # Step 4b: Explore 4 possible movement directions
            for dx, dy in dirs:
                nx, ny = x+dx, y+dy
                
                # Step 4c: Check if (nx, ny) is within bounds
                if 0 <= nx < m and 0 <= ny < n:
                    next_k = rk - grid[nx][ny]  # Step 4d: Reduce k if stepping on an obstacle
                    state = (nx, ny, next_k)

                    # Step 4e: If we still have eliminations and haven't visited this state
                    if next_k >= 0 and state not in seen:
                        seen.add(state)
                        queue.append((nx, ny, next_k, moves+1))

        # Step 5: No valid path found, return -1
        return -1

"""
Leetcode 1293: Shortest Path in a Grid with Obstacles Elimination (https://leetcode.com/problems/shortest-path-in-a-grid-with-obstacles-elimination/)

You are given an m x n integer matrix grid where each cell is either 0 (empty) or 1 (obstacle). You can move up, down, left, or right from and to an empty cell in one step.
Return the minimum number of steps to walk from the upper left corner (0, 0) to the lower right corner (m - 1, n - 1) given that you can eliminate at most k obstacles. If it is not possible to find such walk return -1.

Example 1:
Input: grid = [[0,0,0],[1,1,0],[0,0,0],[0,1,1],[0,0,0]], k = 1
Output: 6
Explanation: 
The shortest path without eliminating any obstacle is 10.
The shortest path with one obstacle elimination at position (3,2) is 6. Such path is (0,0) -> (0,1) -> (0,2) -> (1,2) -> (2,2) -> (3,2) -> (4,2).

Example 2:
Input: grid = [[0,1,1],[1,1,1],[1,0,0]], k = 1
Output: -1
Explanation: We need to eliminate at least two obstacles to find such a walk.
 
Constraints:
m == grid.length
n == grid[i].length
1 <= m, n <= 40
1 <= k <= m * n
grid[i][j] is either 0 or 1.
grid[0][0] == grid[m - 1][n - 1] == 0

Approach (Step-by-Step)
1. Initialize a queue for BFS that stores (x, y, remaining k, moves), starting from (0,0,k,0).
2. Use a set seen to keep track of visited states (x, y, remaining k).
3. Define 4 possible movement directions (up, down, left, right).
4. While the queue is not empty:
   |--> Dequeue (x, y, rk, moves).
   |--> If (x, y) is the bottom-right corner (m-1, n-1), return moves as the shortest path.
   |--> Try moving in each of the 4 directions.
   |--> If the new position (nx, ny) is within bounds:
     ||--> Compute next_k = rk - grid[nx][ny] (remaining obstacle removals after stepping).
     ||--> If next_k >= 0 and the state (nx, ny, next_k) has not been visited:
      |||--> Mark it as visited and add (nx, ny, next_k, moves + 1) to the queue.
5. If the queue is exhausted without reaching (m-1, n-1), return -1.
"""
