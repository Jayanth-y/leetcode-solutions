class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        # Step 1: Initialize adjacency list for graph representation
        g = defaultdict(list)

        # Step 2: Populate graph with bidirectional roads
        for s, d, c in roads:
            g[s].append((c, d))
            g[d].append((c, s))
        
        # Step 3: Create visited list to track visited cities
        visited = [0] * (n + 1)

        # Step 4: Mark city 1 as visited
        visited[1] = 1

        # Step 5: Initialize queue for BFS traversal
        stack = [1]

        # Step 6: Initialize res with infinity to track minimum road score
        res = float('inf')
        
        # Step 7: Process BFS traversal
        while stack:
            s = stack.pop(0)  # Step 7: Pop from the queue
            
            # Step 8: Iterate over all connected roads
            for c, d in g[s]:
                # Step 9: If the destination city is not visited, mark and enqueue it
                if visited[d] == 0:
                    stack.append(d)
                    visited[d] = 1
                
                # Step 10: Update res with the minimum road score encountered
                res = min(res, c)
        
        # Step 12: Return the final minimum score
        return res
"""
Leetcode 2492: Minimum Score of a Path Between Two Cities (https://leetcode.com/problems/minimum-score-of-a-path-between-two-cities/description)

You are given a positive integer n representing n cities numbered from 1 to n. 
You are also given a 2D array roads where roads[i] = [ai, bi, distancei] indicates that there is a bidirectional road between cities ai and bi with a distance equal to distancei. 
The cities graph is not necessarily connected.
The score of a path between two cities is defined as the minimum distance of a road in this path.
Return the minimum possible score of a path between cities 1 and n.

Note:
A path is a sequence of roads between two cities.
It is allowed for a path to contain the same road multiple times, and you can visit cities 1 and n multiple times along the path.
The test cases are generated such that there is at least one path between 1 and n.
 
Example 1:
Input: n = 4, roads = [[1,2,9],[2,3,6],[2,4,5],[1,4,7]]
Output: 5
Explanation: The path from city 1 to 4 with the minimum score is: 1 -> 2 -> 4. The score of this path is min(9,5) = 5.
It can be shown that no other path has less score.

Example 2:
Input: n = 4, roads = [[1,2,2],[1,3,4],[3,4,7]]
Output: 2
Explanation: The path from city 1 to 4 with the minimum score is: 1 -> 2 -> 1 -> 3 -> 4. The score of this path is min(2,2,4,7) = 2.
 
Constraints:
2 <= n <= 105
1 <= roads.length <= 105
roads[i].length == 3
1 <= ai, bi <= n
ai != bi
1 <= distancei <= 104
There are no repeated edges.
There is at least one path between 1 and n.

Approach:
1. Initialize an adjacency list g to store the graph representation of roads.
2. Populate the graph by adding both forward and backward connections for each road.
3. Create a visited list of size n+1 to track visited cities.
4. Mark city 1 as visited since we start from there.
5. Initialize a queue stack with city 1 for BFS traversal.
6. Initialize res as infinity to track the minimum road score.
7. Process nodes in the queue using BFS by popping from the front.
8. Iterate over all connected roads for the current city.
9. If the destination city has not been visited, mark it as visited and add it to the queue.
10. Update res with the minimum road score encountered.
11. Continue processing until all reachable cities have been visited.
12. Return res as the final answer.
"""
