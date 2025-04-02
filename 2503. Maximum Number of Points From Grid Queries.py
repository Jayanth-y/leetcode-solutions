class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        m, n = len(grid), len(grid[0])  # Grid dimensions
        seen = {(0, 0)}  # Step 1: Track visited cells
        dirs = [(0, 1), (-1, 0), (0, -1), (1, 0)]  # 4 possible directions

        squeries = sorted(list(set(queries)))  # Step 2: Unique, sorted queries
        val = defaultdict(int)  # Step 6: Map query limit to result

        self.points = 0  # Step 4: Total points collected
        self.next_queue = [(0, 0)]  # Step 1: Start from (0, 0)

        def calculatePoints(queue, limit):  # Step 3: BFS traversal
            self.next_queue = []  # Prepare for next round
            while queue:
                x, y = queue.pop()
                if grid[x][y] < limit:
                    self.points += 1  # Step 4: Collect point
                    for (dx, dy) in dirs:
                        nx, ny = (x + dx), (y + dy)
                        if 0 <= nx < m and 0 <= ny < n and (nx, ny) not in seen:
                            seen.add((nx, ny))  # Step 4: Mark as visited
                            queue.append((nx, ny))
                else:
                    self.next_queue.append((x, y))  # Not visited due to limit

            return self.points

        for limit in squeries:  # Step 5: Process in increasing order
            if limit not in val:
                val[limit] = calculatePoints(self.next_queue, limit)

        return [val[limit] for limit in queries]  # Step 6: Build final result

"""
2503. Maximum Number of Points From Grid Queries (https://leetcode.com/problems/maximum-number-of-points-from-grid-queries/description/)

You are given an m x n integer matrix grid and an array queries of size k.
Find an array answer of size k such that for each integer queries[i] you start in the top left cell of the matrix and repeat the following process:
If queries[i] is strictly greater than the value of the current cell that you are in, then you get one point if it is your first time visiting this cell.
And you can move to any adjacent cell in all 4 directions: up, down, left, and right.
Otherwise, you do not get any points, and you end this process.
After the process, answer[i] is the maximum number of points you can get. Note that for each query you are allowed to visit the same cell multiple times.
Return the resulting array answer.

Example 1:
Input: grid = [[1,2,3],[2,5,7],[3,5,1]], queries = [5,6,2]
Output: [5,8,1]
Explanation: The diagrams above show which cells we visit to get points for each query.

Example 2:
Input: grid = [[5,2,1],[1,1,2]], queries = [3]
Output: [0]
Explanation: We can not get any points because the value of the top left cell is already greater than or equal to 3.
 
Constraints:
m == grid.length
n == grid[i].length
2 <= m, n <= 1000
4 <= m * n <= 105
k == queries.length
1 <= k <= 104
1 <= grid[i][j], queries[i] <= 106

Approach: Step-by-Step (No Subpoints)
1. Start BFS from the top-left cell (0, 0) and keep track of visited cells.
2. Sort the queries and process them in increasing order.
3. For each query, run BFS and collect all cells with value less than the current query limit.
4. Maintain a count of visited points and avoid re-processing already visited cells.
5. Store the result for each unique query value in a map.
6. For the original query list, return the result from the map.
"""
